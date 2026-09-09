#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
calcular.py — Gráfico de quadrantes dos planos nacionais de IA (etapa de cálculo)

Aplica o CODEBOOK (abaixo, editável) às tabelas de vocabulário de cada
documento e grava, na pasta deste script:

  coordenadas.csv     versão principal: soma das taxas por 1.000 tokens,
                      só unigramas — colunas documento, país, ano, G2, G3,
                      G4, G5, massa, X, Y (+ arquivo e rótulo, para o plotar.py)
  robustez.csv        três versões lado a lado: soma/unigramas,
                      média/unigramas, soma/unigramas+bigramas, com o
                      quadrante de cada uma e a indicação de mudança
  termos_ausentes.md  termos do codebook não encontrados em cada documento,
                      termos do top-N que ficaram fora do codebook (para
                      revisão) e os casamentos por variante ortográfica/plural

Fonte dos dados (argumento --fonte):
  json  (padrão) regenera as tabelas de vocabulário a partir dos seis JSONs,
        com o MESMO pipeline do notebook analise_lexical_planos_ia.ipynb
        (spaCy en_core_web_sm; o bloco "PIPELINE" abaixo é cópia literal).
        Permite --top 100 ou --top 0 (vocabulário inteiro).
  csv   lê os *_top50_vocabulario.csv exportados pelo notebook (sem spaCy).
        Só serve para --top 50.

Uso típico:
  python calcular.py                 # top-50, a partir dos JSONs
  python calcular.py --fonte csv     # top-50, a partir dos CSVs do notebook
  python calcular.py --top 100       # expansão para o top-100
  python calcular.py --top 0         # documento inteiro (todos os termos elegíveis)
  python calcular.py --bigramas dividir   # regra alternativa para bigramas

Com --fonte json e --top 50 o script confere, termo a termo, se as tabelas
regeneradas coincidem com os CSVs do notebook e avisa se houver diferença.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

import pandas as pd

# =============================================================================
# 1. CODEBOOK — edite aqui. Lemas em inglês; a comparação é case-insensitive
#    e feita por igualdade exata do lema (nunca por prefixo/substring: "Act"
#    não casa com "Action", "Open" não casa com "Open-source").
#    Singular/plural: as tabelas já vêm lematizadas pelo notebook; como
#    segurança extra, um termo que NÃO case exatamente é testado na forma
#    singular (ies→y, -es, -s) e o casamento fica registrado no relatório.
#    Um mesmo lema não pode aparecer em dois grupos — o script aborta.
# =============================================================================
CODEBOOK: "OrderedDict[str, list[str]]" = OrderedDict([
    ("G1", [  # descartado: vocabulário genérico de IA / verbos de política
        "AI", "Artificial", "Intelligence", "Technology", "Technological",
        "Development", "Develop", "Model", "Application", "Solution", "Use",
        "Tool", "Action", "Plan", "Initiative", "Effort", "Process", "Method",
        "Build", "Create", "Establish", "Improve", "Improvement", "Enhance",
        "Strengthen", "Promote", "Accelerate", "Expand", "Foster", "Enable",
        "Encourage", "Achieve", "Explore", "Address", "Focus", "Aim", "Refine",
        "Increase", "Launch", "Role", "Core", "Generation", "Future",
        "Potential", "Impact", "Challenge", "Capability", "Digital",
    ]),
    ("G2", [  # Infraestrutura, computação e base material
        "Data", "Information", "Infrastructure", "Compute", "Computing",
        "Cloud", "Platform", "System", "Intelligent", "Smart", "Factory",
        "Gigafactory", "Semiconductor", "Device", "Energy", "Grid", "Power",
        "Center", "Centre", "Hub", "Resource", "Access", "Open", "Open-source",
        "Autonomous", "Learning", "Frontier", "Construction",
    ]),
    ("G3", [  # Economia, indústria, difusão de mercado e competição geopolítica
        "Sector", "Sectoral", "Market", "Industry", "Industrial", "Innovation",
        "Startup", "Enterprise", "Investment", "Competitiveness", "Adoption",
        "Uptake", "Deployment", "Manufacturing", "Production", "Product",
        "Consumption", "Agricultural", "Facilitate", "Help", "Global",
        "Strategy", "Strategic", "Management", "Coordination", "Collaboration",
        "Control", "Security", "Defence", "Adversary", "Export", "Critical",
        "Lead",
    ]),
    ("G4", [  # Estado, governança e regulação
        "Governance", "Act", "Policy", "Standard", "Risk", "Public",
        "Government", "Federal", "Agency", "National", "Country",
    ]),
    ("G5", [  # Ciência, dimensão social, capital humano, inclusão e sustentabilidade
        "Research", "Science", "Scientific", "Theory", "Knowledge",
        "Breakthrough", "Education", "Training", "Skill", "Talent",
        "Workforce", "Worker", "Health", "Healthcare", "Social", "Society",
        "Service", "Sustainable", "Program", "Reduction", "Basic", "Capacity",
        "Integration",
    ]),
])

# Variantes ortográficas/lemas alternativos que devem ser tratados como o
# mesmo termo do codebook (chave → termo do codebook). Só produzem efeito
# se a variante aparecer na tabela; hoje só "datum" (lema que o spaCy dá a
# "data", exibido como "Data" no notebook) ocorre no top-50.
VARIANTES = {
    "datum": "data",
    "defense": "defence",     # grafia americana
    "programme": "program",   # grafia britânica
}

NOMES_GRUPOS = {
    "G1": "descartado",
    "G2": "Infraestrutura, computação e base material",
    "G3": "Economia, indústria, difusão de mercado e competição geopolítica",
    "G4": "Estado, governança e regulação",
    "G5": "Ciência, dimensão social, capital humano, inclusão e sustentabilidade",
}
GRUPOS_ATIVOS = ["G2", "G3", "G4", "G5"]

# Bigramas (só na versão de robustez "soma_uni_bi"):
#   "nucleo"  → o bigrama herda o grupo do núcleo (última palavra); se o
#               núcleo for G1/desconhecido, herda o do modificador; se nenhum
#               dos dois estiver em G2–G5, é descartado.  Ex.: "Public Sector"
#               → G3, "AI Act" → G4, "AI Model" → descartado.
#   "dividir" → a taxa do bigrama é repartida igualmente entre os grupos
#               (G2–G5) das duas palavras. Ex.: "Public Sector" → ½ G4, ½ G3.
REGRA_BIGRAMAS_PADRAO = "nucleo"

# Valores de referência dados no enunciado (versão soma, só unigramas, top-50)
REFERENCIA = {
    "pbia.json": (-0.12, -0.23),
    "americas_ai_action_plan.json": (0.08, 0.36),
    "new_generation_ai_development_plan.json": (0.73, 0.13),
}

# =============================================================================
# 2. Documentos (ordem de saída = ordem desta lista)
# =============================================================================
DOCUMENTOS = OrderedDict([
    ("ai_continent_action_plan.json", dict(
        documento="AI Continent Action Plan", pais="União Europeia", ano=2025,
        rotulo="UE 2025 — AI Continent")),
    ("apply_ai_strategy.json", dict(
        documento="Apply AI Strategy", pais="União Europeia", ano=2025,
        rotulo="UE 2025 — Apply AI")),
    ("americas_ai_action_plan.json", dict(
        documento="America's AI Action Plan", pais="Estados Unidos", ano=2025,
        rotulo="EUA 2025")),
    ("new_generation_ai_development_plan.json", dict(
        documento="New Generation AI Development Plan", pais="China", ano=2017,
        rotulo="China 2017")),
    ("ai_plus.json", dict(
        documento='Opinions on Deepening the "Artificial Intelligence+" Initiative',
        pais="China", ano=2025, rotulo="China 2025 — AI+")),
    ("pbia.json", dict(
        documento="Plano Brasileiro de IA (PBIA) — AI for the Good of All",
        pais="Brasil", ano=2024, rotulo="Brasil 2024 — PBIA")),
])

DIR_SCRIPT = Path(__file__).resolve().parent
DIR_DADOS_PADRAO = DIR_SCRIPT.parent          # onde estão os JSONs e os CSVs


# =============================================================================
# 3. Índice do codebook e classificação de termos
# =============================================================================
def normalizar(termo: str) -> str:
    t = str(termo).strip().lower()
    return VARIANTES.get(t, t)


def montar_indice() -> dict[str, str]:
    indice: dict[str, str] = {}
    for grupo, termos in CODEBOOK.items():
        for termo in termos:
            chave = normalizar(termo)
            if chave in indice and indice[chave] != grupo:
                sys.exit(f"ERRO no codebook: '{termo}' está em {indice[chave]} e em {grupo}.")
            indice[chave] = grupo
    return indice


INDICE = montar_indice()


def candidatos_singular(t: str) -> list[str]:
    c = []
    if t.endswith("ies") and len(t) > 4:
        c.append(t[:-3] + "y")
    if t.endswith("es") and len(t) > 3:
        c.append(t[:-2])
    if t.endswith("s") and len(t) > 2:
        c.append(t[:-1])
    return c


def classificar_unigrama(termo: str) -> tuple[str | None, str, str | None]:
    """Devolve (grupo, chave_usada, tipo_de_casamento).
    tipo_de_casamento: 'exato', 'variante', 'plural' ou None (fora do codebook)."""
    bruto = str(termo).strip().lower()
    chave = normalizar(termo)
    if chave in INDICE:
        return INDICE[chave], chave, ("variante" if chave != bruto else "exato")
    for s in candidatos_singular(chave):
        s = VARIANTES.get(s, s)
        if s in INDICE:
            return INDICE[s], s, "plural"
    return None, chave, None


def classificar_bigrama(termo: str, regra: str) -> dict[str, float]:
    """Devolve {grupo: fração da taxa} para um bigrama (só grupos ativos)."""
    palavras = str(termo).split()
    grupos = [classificar_unigrama(p)[0] for p in palavras]
    ativos = [g for g in grupos if g in GRUPOS_ATIVOS]
    if regra == "nucleo":
        for g in reversed(grupos):          # núcleo primeiro, depois modificador
            if g in GRUPOS_ATIVOS:
                return {g: 1.0}
        return {}
    if regra == "dividir":
        if not ativos:
            return {}
        return {g: ativos.count(g) / len(grupos) for g in set(ativos)}
    sys.exit(f"Regra de bigramas desconhecida: {regra}")


# =============================================================================
# 4. PIPELINE — cópia literal do notebook analise_lexical_planos_ia.ipynb
#    (usado só com --fonte json). Qualquer alteração aqui precisa ser
#    replicada no notebook, e vice-versa, para que as tabelas coincidam.
# =============================================================================
STRUCTURAL_CLEAN = {
    "pbia.json": [
        (r"\bImpact Action \d+:\s*", " "),
        (r"\bAction \d+:\s*", " "),
        (r"\bChallenge:\s*", " "),
        (r"\bExpected impacts?:\s*", " "),
    ],
    "americas_ai_action_plan.json": [
        (r"\bRecommended Policy Actions\b", " "),
        (r"\bLed by\b", " "),
    ],
    "ai_continent_action_plan.json": [
        (r"Key Commission(?:\s*/\s*EuroHPC)?\s+[Aa]ctions:?", " "),
    ],
}

GENERAL_EXTRA_STOPWORDS = {
    "include", "ensure", "provide", "support", "need", "new", "key",
    "major", "relevant", "set", "work", "well", "particular", "certain",
    "various", "significant", "given", "existing", "exist",
}

CUSTOM_STOPWORDS = {
    "ai_continent_action_plan.json": {
        "european", "europe", "eu", "union", "commission", "member",
        "communication", "state", "apply",
    },
    "apply_ai_strategy.json": {
        "european", "europe", "eu", "union", "commission", "member",
        "communication", "state", "apply",
    },
    "ai_plus.json": {"china", "chinese", "council", "state"},
    "new_generation_ai_development_plan.json": {
        "china", "chinese", "council", "party", "committee",
    },
    "americas_ai_action_plan.json": {
        "america", "american", "united", "states", "trump", "administration",
        "doc", "doe", "nsf", "caisi", "ostp", "dol", "dod", "nsc", "dos",
        "cte", "dhs", "nairr", "ftc", "ntia", "bls", "bea", "nstc", "nist",
        "gsa", "nepa", "odni", "cbrne",
    },
    "pbia.json": {
        "brazil", "brazilian", "mcti", "cgee", "cct", "abc", "pbia", "finep", "mgi",
    },
}

ALLOWED_POS = {"NOUN", "PROPN", "VERB", "ADJ"}
WORD_RE = re.compile(r"^[a-z][a-z\-]*[a-z]$|^[a-z]$")
MIN_LEN = 2
MIN_COUNT_UNI = 3
MIN_COUNT_BI = 2

LEMMA_FIX = {
    "gigafactorie": "gigafactory",
    "giga-factorie": "gigafactory",
    "specie": "species",
}

DISPLAY_OVERRIDES = {
    "ai": "AI", "eu": "EU", "us": "US", "gdp": "GDP", "r&d": "R&D",
    "nist": "NIST", "hpc": "HPC", "gpu": "GPU", "gpus": "GPU", "ict": "ICT",
    "sme": "SME", "smes": "SMEs", "sus": "SUS", "llm": "LLM", "llms": "LLMs",
    "5g": "5G", "eurohpc": "EuroHPC", "iot": "IoT", "api": "API",
    "datum": "Data",
}


def display_term(term: str) -> str:
    return " ".join(DISPLAY_OVERRIDES.get(w, w.capitalize()) for w in term.split(" "))


_NLP = None


def carregar_nlp():
    global _NLP
    if _NLP is None:
        import spacy
        from spacy.util import compile_infix_regex
        try:
            nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
        except OSError:
            from spacy.cli import download
            download("en_core_web_sm")
            nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
        nlp.add_pipe("sentencizer")
        infixes = [pat for pat in nlp.Defaults.infixes if "-" not in pat]
        nlp.tokenizer.infix_finditer = compile_infix_regex(infixes).finditer
        _NLP = nlp
    return _NLP


def clean_lemma(tok) -> str:
    lemma = tok.lemma_.lower()
    return LEMMA_FIX.get(lemma, lemma)


def is_content(tok, stop_extra) -> bool:
    if tok.pos_ not in ALLOWED_POS or tok.is_stop:
        return False
    lemma = clean_lemma(tok)
    if not WORD_RE.match(lemma) or len(lemma) < MIN_LEN:
        return False
    if lemma in GENERAL_EXTRA_STOPWORDS or lemma in stop_extra:
        return False
    return True


def analisar_json(caminho: Path, fname: str) -> pd.DataFrame:
    """Reproduz analyze() do notebook: tabela completa de termos elegíveis,
    ordenada por taxa/1.000 tokens, com attrs['total_words']."""
    with open(caminho, encoding="utf-8") as fh:
        texto = json.load(fh)["texto_completo"]
    for pat, repl in STRUCTURAL_CLEAN.get(fname, []):
        texto = re.sub(pat, repl, texto)
    text = texto.lower()
    stop_extra = CUSTOM_STOPWORDS.get(fname, set())
    doc = carregar_nlp()(text)

    total_words = sum(1 for t in doc if WORD_RE.match(t.text) and len(t.text) >= MIN_LEN)

    uni, bi = Counter(), Counter()
    for sent in doc.sents:
        toks = list(sent)
        flags = [is_content(t, stop_extra) for t in toks]
        lemmas = [clean_lemma(t) for t in toks]
        for i, ok in enumerate(flags):
            if ok:
                uni[lemmas[i]] += 1
        for i in range(len(toks) - 1):
            if flags[i] and flags[i + 1]:
                bi[f"{lemmas[i]} {lemmas[i+1]}"] += 1

    rows = [(t, "unigrama", n) for t, n in uni.items() if n >= MIN_COUNT_UNI]
    rows += [(t, "bigrama", n) for t, n in bi.items() if n >= MIN_COUNT_BI]
    df = pd.DataFrame(rows, columns=["termo", "tipo", "ocorrencias"])
    df["por_1000_tokens"] = df["ocorrencias"] / total_words * 1000
    df["termo_exibicao"] = df["termo"].apply(display_term)
    df = df.sort_values("por_1000_tokens", ascending=False).reset_index(drop=True)
    df.attrs["total_words"] = total_words
    return df


# =============================================================================
# 5. Carregamento das tabelas (json ou csv) → DataFrame padronizado
#    colunas: termo_exibicao, tipo, ocorrencias, por_1000_tokens
# =============================================================================
def carregar_csv_top50(dir_dados: Path, fname: str) -> pd.DataFrame:
    caminho = dir_dados / f"{fname.replace('.json', '')}_top50_vocabulario.csv"
    if not caminho.exists():
        sys.exit(f"Arquivo não encontrado: {caminho}")
    df = pd.read_csv(caminho, encoding="utf-8-sig")
    df = df.rename(columns={"Termo": "termo_exibicao", "Tipo": "tipo",
                            "Ocorrências": "ocorrencias", "Por 1.000 tokens": "por_1000_tokens"})
    df["termo"] = df["termo_exibicao"].str.lower()
    return df[["termo", "termo_exibicao", "tipo", "ocorrencias", "por_1000_tokens"]]


def carregar_tabelas(dir_dados: Path, fonte: str, top: int) -> dict[str, pd.DataFrame]:
    tabelas = {}
    for fname in DOCUMENTOS:
        if fonte == "csv":
            if top != 50:
                sys.exit("--fonte csv só está disponível para --top 50 (os CSVs do notebook são top-50).")
            tabelas[fname] = carregar_csv_top50(dir_dados, fname)
        else:
            caminho = dir_dados / fname
            if not caminho.exists():
                sys.exit(f"Arquivo não encontrado: {caminho}")
            df = analisar_json(caminho, fname)
            total = df.attrs["total_words"]
            if top > 0:
                df = df.head(top).copy()
            df.attrs["total_words"] = total
            tabelas[fname] = df
    return tabelas


def conferir_com_csv(dir_dados: Path, tabelas: dict[str, pd.DataFrame]) -> None:
    """Com --fonte json --top 50: confere termo a termo contra os CSVs do notebook."""
    print("\nConferência das tabelas regeneradas contra os CSVs do notebook:")
    for fname, df in tabelas.items():
        caminho = dir_dados / f"{fname.replace('.json', '')}_top50_vocabulario.csv"
        if not caminho.exists():
            print(f"  {fname}: CSV não encontrado, conferência pulada")
            continue
        ref = carregar_csv_top50(dir_dados, fname)
        a = list(zip(df["termo_exibicao"], df["tipo"], df["ocorrencias"], df["por_1000_tokens"].round(2)))
        b = list(zip(ref["termo_exibicao"], ref["tipo"], ref["ocorrencias"], ref["por_1000_tokens"].round(2)))
        if a == b:
            print(f"  {fname}: idêntico ({len(a)} linhas)")
        else:
            dif = [(i + 1, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
            print(f"  {fname}: DIFERENÇAS em {len(dif)} linha(s) (rank, regenerado, csv):")
            for d in dif[:10]:
                print("     ", d)


# =============================================================================
# 6. Agregação por grupo e coordenadas
# =============================================================================
def agregar(df: pd.DataFrame, regra_bigramas: str) -> dict:
    """Soma as taxas por grupo; devolve dicionário com as três versões e os
    diagnósticos (termos encontrados, fora do codebook, casamentos)."""
    soma_uni = {g: 0.0 for g in GRUPOS_ATIVOS}
    soma_bi = {g: 0.0 for g in GRUPOS_ATIVOS}
    encontrados = {g: {} for g in CODEBOOK}          # grupo → {chave: taxa}
    linhas = {g: Counter() for g in CODEBOOK}         # grupo → {chave: nº de linhas somadas}
    fora = []                                         # unigramas fora do codebook
    casamentos = []                                   # (termo, chave, tipo)
    bigramas = []                                     # (termo, taxa, {grupo: fração})

    for _, r in df.iterrows():
        taxa = float(r["por_1000_tokens"])
        termo = str(r["termo_exibicao"])
        if r["tipo"] == "unigrama":
            grupo, chave, tipo = classificar_unigrama(termo)
            if grupo is None:
                fora.append((termo, taxa))
                continue
            if tipo != "exato":
                casamentos.append((termo, chave, tipo))
            encontrados[grupo][chave] = encontrados[grupo].get(chave, 0.0) + taxa
            linhas[grupo][chave] += 1
            if grupo in GRUPOS_ATIVOS:
                soma_uni[grupo] += taxa
        else:
            fracoes = classificar_bigrama(termo, regra_bigramas)
            bigramas.append((termo, taxa, fracoes))
            for g, f in fracoes.items():
                soma_bi[g] += taxa * f

    n_termos = {g: len(CODEBOOK[g]) for g in GRUPOS_ATIVOS}
    versoes = {
        "soma_uni": dict(soma_uni),
        "media_uni": {g: soma_uni[g] / n_termos[g] for g in GRUPOS_ATIVOS},
        "soma_uni_bi": {g: soma_uni[g] + soma_bi[g] for g in GRUPOS_ATIVOS},
    }
    return dict(versoes=versoes, encontrados=encontrados, linhas=linhas, fora=fora,
                casamentos=casamentos, bigramas=bigramas,
                massa_descartada=sum(encontrados["G1"].values()))


def coordenadas(G: dict[str, float]) -> tuple[float, float]:
    def indice(a, b):
        return (a - b) / (a + b) if (a + b) > 0 else 0.0
    return indice(G["G3"], G["G4"]), indice(G["G2"], G["G5"])


def quadrante(x: float, y: float) -> str:
    v = "superior" if y >= 0 else "inferior"
    h = "direito" if x >= 0 else "esquerdo"
    return f"{v}-{h}"


# =============================================================================
# 7. Saídas
# =============================================================================
def escrever_saidas(resultados: dict, tabelas: dict, args, dir_saida: Path) -> None:
    linhas_coord, linhas_rob = [], []
    for fname, meta in DOCUMENTOS.items():
        res = resultados[fname]
        G = res["versoes"]["soma_uni"]
        x, y = coordenadas(G)
        linhas_coord.append({
            "documento": meta["documento"], "país": meta["pais"], "ano": meta["ano"],
            "G2": round(G["G2"], 4), "G3": round(G["G3"], 4),
            "G4": round(G["G4"], 4), "G5": round(G["G5"], 4),
            "massa": round(sum(G.values()), 4), "X": round(x, 4), "Y": round(y, 4),
            "arquivo": fname, "rotulo": meta["rotulo"],
        })
        linha = {"documento": meta["documento"], "arquivo": fname}
        quads = {}
        for versao, Gv in res["versoes"].items():
            xv, yv = coordenadas(Gv)
            quads[versao] = quadrante(xv, yv)
            for g in GRUPOS_ATIVOS:
                linha[f"{versao}_{g}"] = round(Gv[g], 4)
            linha[f"{versao}_massa"] = round(sum(Gv.values()), 4)
            linha[f"{versao}_X"] = round(xv, 4)
            linha[f"{versao}_Y"] = round(yv, 4)
            linha[f"{versao}_quadrante"] = quads[versao]
        linha["muda_quadrante"] = "sim" if len(set(quads.values())) > 1 else "não"
        linhas_rob.append(linha)

    df_coord = pd.DataFrame(linhas_coord)
    df_rob = pd.DataFrame(linhas_rob)
    df_coord.to_csv(dir_saida / "coordenadas.csv", index=False, encoding="utf-8")
    df_rob.to_csv(dir_saida / "robustez.csv", index=False, encoding="utf-8")

    # ---------------- termos_ausentes.md ----------------
    descr_top = "documento inteiro (todos os termos elegíveis)" if args.top == 0 else f"top-{args.top}"
    md = [f"# Termos do codebook ausentes por documento\n",
          f"Base: {descr_top} de cada documento, fonte `{args.fonte}`. "
          "Um termo do codebook ausente vale 0 na soma do grupo.\n"]
    for fname, meta in DOCUMENTOS.items():
        res = resultados[fname]
        md.append(f"\n## {meta['rotulo']} — {meta['documento']}\n")
        tot = tabelas[fname].attrs.get("total_words")
        if tot:
            md.append(f"Total de tokens do documento: {tot}. ")
        md.append(f"Massa descartada (G1): {res['massa_descartada']:.2f} por 1.000 tokens.\n")
        for g in GRUPOS_ATIVOS:
            presentes = set(res["encontrados"][g])
            todos = [normalizar(t) for t in CODEBOOK[g]]
            ausentes = [t for t in CODEBOOK[g] if normalizar(t) not in presentes]
            md.append(f"\n**{g} — {NOMES_GRUPOS[g]}** "
                      f"({len(todos) - len(ausentes)} de {len(todos)} termos presentes; "
                      f"soma = {res['versoes']['soma_uni'][g]:.2f}/1.000 tokens)\n")
            md.append("- presentes: " + (", ".join(
                f"{t} ({res['encontrados'][g][normalizar(t)]:.2f}"
                + (f", {res['linhas'][g][normalizar(t)]} linhas somadas" if res['linhas'][g][normalizar(t)] > 1 else "")
                + ")" for t in CODEBOOK[g] if normalizar(t) in presentes) or "nenhum") + "\n")
            md.append("- ausentes: " + (", ".join(ausentes) or "nenhum") + "\n")

    md.append("\n\n# Termos do top-N fora do codebook (revisar e classificar)\n")
    md.append("Unigramas presentes na tabela do documento que não constam em nenhum grupo "
              "(nem em G1). Ficaram fora de todas as somas.\n")
    algum = False
    for fname, meta in DOCUMENTOS.items():
        fora = resultados[fname]["fora"]
        if fora:
            algum = True
            md.append(f"\n**{meta['rotulo']}**: " + ", ".join(f"{t} ({v:.2f})" for t, v in fora) + "\n")
    if not algum:
        md.append("\nNenhum: todos os unigramas das tabelas estão cobertos pelo codebook.\n")

    md.append("\n\n# Casamentos por variante ortográfica ou plural\n")
    md.append("Termos que não casaram exatamente com o codebook e foram aceitos por "
              "variante (tabela `VARIANTES`) ou por redução ao singular. Confira.\n")
    algum = False
    for fname, meta in DOCUMENTOS.items():
        cas = resultados[fname]["casamentos"]
        if cas:
            algum = True
            md.append(f"\n**{meta['rotulo']}**: " + ", ".join(
                f"{t} → {c} [{tipo}]" for t, c, tipo in cas) + "\n")
    if not algum:
        md.append("\nNenhum.\n")

    md.append("\n\n# Bigramas e sua classificação (só na versão de robustez soma_uni_bi)\n")
    md.append(f"Regra: `{args.bigramas}`. Bigramas cujo núcleo e modificador estão em G1 "
              "(ex.: \"AI Model\") são descartados.\n")
    for fname, meta in DOCUMENTOS.items():
        bg = resultados[fname]["bigramas"]
        if bg:
            md.append(f"\n**{meta['rotulo']}**: " + ", ".join(
                f"{t} ({v:.2f}) → " + (", ".join(f"{g}×{f:g}" for g, f in fr.items()) or "descartado")
                for t, v, fr in bg) + "\n")
    (dir_saida / "termos_ausentes.md").write_text("".join(md), encoding="utf-8")

    # ---------------- terminal ----------------
    pd.set_option("display.width", 160)
    print("\ncoordenadas.csv (soma, só unigramas):")
    print(df_coord[["rotulo", "G2", "G3", "G4", "G5", "massa", "X", "Y"]].round(2).to_string(index=False))

    print("\nrobustez.csv — coordenadas nas três versões:")
    cols = ["rotulo"] + [f"{v}_{c}" for v in ("soma_uni", "media_uni", "soma_uni_bi") for c in ("X", "Y")] + ["muda_quadrante"]
    df_rob2 = df_rob.copy()
    df_rob2["rotulo"] = [DOCUMENTOS[f]["rotulo"] for f in df_rob2["arquivo"]]
    print(df_rob2[cols].round(2).to_string(index=False))

    print("\nConferência com os valores de referência do enunciado (soma, unigramas, top-50):")
    for fname, (xr, yr) in REFERENCIA.items():
        row = df_coord[df_coord["arquivo"] == fname].iloc[0]
        ok = abs(row["X"] - xr) < 0.01 and abs(row["Y"] - yr) < 0.01
        print(f"  {DOCUMENTOS[fname]['rotulo']:<22} X={row['X']:+.2f} (ref {xr:+.2f})  "
              f"Y={row['Y']:+.2f} (ref {yr:+.2f})  {'ok' if ok else 'DIFERE'}")
    if args.top != 50:
        print("  (a base atual não é o top-50; diferenças em relação à referência são esperadas)")

    print(f"\nArquivos gravados em {dir_saida}: coordenadas.csv, robustez.csv, termos_ausentes.md")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fonte", choices=["json", "csv"], default="json")
    p.add_argument("--top", type=int, default=50, help="N termos por documento (0 = todos)")
    p.add_argument("--bigramas", choices=["nucleo", "dividir"], default=REGRA_BIGRAMAS_PADRAO)
    p.add_argument("--dados", type=Path, default=DIR_DADOS_PADRAO, help="pasta com os JSONs/CSVs")
    p.add_argument("--saida", type=Path, default=DIR_SCRIPT, help="pasta de saída")
    args = p.parse_args()

    tabelas = carregar_tabelas(args.dados, args.fonte, args.top)
    if args.fonte == "json" and args.top == 50:
        conferir_com_csv(args.dados, tabelas)

    resultados = {fname: agregar(df, args.bigramas) for fname, df in tabelas.items()}
    args.saida.mkdir(parents=True, exist_ok=True)
    escrever_saidas(resultados, tabelas, args, args.saida)


if __name__ == "__main__":
    main()
