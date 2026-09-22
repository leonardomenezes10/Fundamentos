#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
plotar.py — Gráfico de quadrantes dos planos nacionais de IA (etapa de figura)

Lê coordenadas.csv (gerado por calcular.py) e grava figura.png (300 dpi) e
figura.pdf na pasta deste script. Estilo acadêmico para impressão: título e
subtítulo, eixos cruzados na origem, limites simétricos [−1, 1], quatro polos
rotulados, uma cor por país/bloco (Brasil, Estados Unidos, União Europeia,
China), legenda de documentos com nome e ano, legenda de tamanho das bolhas e
nota de rodapé com as fórmulas.

Acessibilidade: a paleta foi verificada para daltonismo (separação mínima
ΔE 9,8 em deuteranopia e 11,2 em tritanopia entre todos os pares, no espaço
OKLab). Nenhuma informação depende só da cor — cada bolha tem rótulo textual
junto a si, a legenda repete país, documento e ano, e o PBIA, documento em
foco, recebe anel tracejado e rótulo em negrito.

Uso na linha de comando:
  python plotar.py                       # versão principal (coordenadas.csv)
  python plotar.py --versao media_uni    # lê a versão de robustez em robustez.csv
  python plotar.py --versao soma_uni_bi  #   → grava figura_<versao>.png/.pdf
  python plotar.py --sem-titulo          # sem título/subtítulo (p. ex. quando a
                                         #   legenda do artigo já os traz)

Uso dentro de um notebook (ver quadrantes_planos_ia.ipynb):
  import plotar
  df = plotar.carregar_coordenadas()
  fig, ax, avisos = plotar.construir_figura(df)

Os deslocamentos dos rótulos são manuais (dicionário OFFSETS). Após desenhar,
construir_figura confere se algum rótulo se sobrepõe a outro rótulo ou a outra
bolha e devolve a lista de avisos.
"""

from __future__ import annotations

import argparse
import math
import textwrap
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.transforms import Bbox

DIR_SCRIPT = Path(__file__).resolve().parent

# =============================================================================
# 1. Cores — uma por país/bloco. Edite aqui para trocar a paleta; se trocar,
#    revalide a separação para daltonismo antes de publicar.
# =============================================================================
CORES_PAIS = {
    "Brasil": "#D7301F",          # vermelho
    "Estados Unidos": "#56B4E9",  # azul-claro
    "União Europeia": "#005F99",  # azul-escuro
    "China": "#009E73",           # verde
}
ORDEM_PAISES = ["Brasil", "Estados Unidos", "União Europeia", "China"]
COR_FALLBACK = "#7f7f7f"          # país fora do dicionário acima

INK = "#1a1a1a"
CINZA_EIXO = "#9a9a9a"
CINZA_LINHA = "#e3e3e3"
CINZA_TEXTO = "#4d4d4d"
FONTES = ["Arial", "Liberation Sans", "Helvetica", "DejaVu Sans"]

ESCALA_BOLHA = 6.0                   # pontos² por unidade de massa (área ∝ massa)
REFERENCIAS_TAMANHO = [60, 90, 120]  # massa (por 1.000 tokens) na legenda

DOC_FOCO = "pbia.json"               # recebe anel tracejado e rótulo em negrito

# =============================================================================
# 2. Textos da figura — edite à vontade
# =============================================================================
TITULO = "Perfis de vocabulário dos planos nacionais de inteligência artificial"

SUBTITULO = (
    "Seis documentos oficiais de política de IA (2017–2025) posicionados pelo peso relativo de quatro campos lexicais.\n"
    "Cada eixo contrapõe dois vocabulários: quanto mais distante do centro, mais desequilibrado é o par naquele documento."
)

COMO_LER = (
    "Como ler o gráfico: cada círculo é um documento oficial de política de inteligência artificial; a cor indica o país ou bloco que o publicou e a "
    "área é proporcional à massa temática total do texto. A posição horizontal mostra se o vocabulário do documento pende para a economia, a "
    "indústria e a competição internacional (à direita) ou para o Estado, a governança e a regulação (à esquerda); a posição vertical, se pende "
    "para a infraestrutura e a base material da computação (acima) ou para a ciência, o capital humano e a dimensão social (abaixo). O cruzamento "
    "dos eixos representa equilíbrio entre os dois polos de cada eixo, e os valores são índices limitados ao intervalo [−1, +1]."
)

# Rótulos dos polos (topo = A = G2; esquerda = B = G4; base = C = G5; direita = D = G3)
POLOS = {
    "topo": "Vocabulário A — Infraestrutura, computação e base material",
    "esquerda": "Vocabulário B — Estado, governança e regulação",
    "base": "Vocabulário C — Ciência, dimensão social, capital humano, inclusão e sustentabilidade",
    "direita": "Vocabulário D — Economia, indústria, difusão de mercado e competição geopolítica",
}
LARGURA_POLO = {"topo": 70, "base": 60, "esquerda": 22, "direita": 24}  # caracteres por linha

# Nome do documento como aparece na legenda (o título completo do CSV é longo
# demais para uma linha). A chave é o nome do arquivo JSON de origem.
NOME_LEGENDA = {
    "pbia.json": "Plano Brasileiro de Inteligência Artificial (PBIA)",
    "americas_ai_action_plan.json": "America’s AI Action Plan",
    "ai_continent_action_plan.json": "AI Continent Action Plan",
    "apply_ai_strategy.json": "Apply AI Strategy",
    "new_generation_ai_development_plan.json": "New Generation AI Development Plan",
    "ai_plus.json": "Opinions on the “Artificial Intelligence+” Initiative",
}
# Ordem das entradas na legenda de documentos
ORDEM_LEGENDA = [
    "pbia.json",
    "americas_ai_action_plan.json",
    "ai_continent_action_plan.json",
    "apply_ai_strategy.json",
    "new_generation_ai_development_plan.json",
    "ai_plus.json",
]

# Deslocamento manual de cada rótulo: (dx, dy) em pontos ALÉM da borda da
# bolha (o raio é somado automaticamente), alinhamento horizontal e vertical.
# Edite se as coordenadas mudarem; construir_figura avisa se houver sobreposição.
OFFSETS = {
    "ai_continent_action_plan.json":           (8, 8, "left", "bottom"),   # acima, à direita
    "apply_ai_strategy.json":                  (-6, -7, "right", "top"),   # abaixo, à esquerda
    "americas_ai_action_plan.json":            (6, 0, "left", "center"),   # à direita
    "new_generation_ai_development_plan.json": (6, 0, "left", "center"),   # à direita
    "ai_plus.json":                            (-7, -8, "right", "top"),   # abaixo, à esquerda
    "pbia.json":                               (-7, 0, "right", "center"), # à esquerda
}
OFFSET_PADRAO = (8, 0, "left", "center")
# Documentos cujo rótulo recebe uma linha-guia fina até a bolha (útil no
# aglomerado de bolhas próximas, onde a adjacência sozinha é ambígua).
COM_GUIA = {"ai_continent_action_plan.json", "apply_ai_strategy.json", "ai_plus.json"}

NOTA = ("X = (G3 − G4)/(G3 + G4);  Y = (G2 − G5)/(G2 + G5);  "
        "Gk = soma das taxas por 1.000 tokens dos unigramas do grupo k (top-50);  "
        "área da bolha proporcional a G2 + G3 + G4 + G5.")

# Posição dos blocos da figura, em fração da altura (de baixo para cima).
# Ajuste aqui se mudar o tamanho da figura ou o comprimento dos textos; a
# função construir_figura avisa se dois blocos passarem a se sobrepor.
FIGSIZE = (11.0, 12.9)
LADO_PLOT = 6.9        # lado do quadrado do gráfico, em polegadas
Y_TITULO = 0.988       # título (topo do texto)
Y_SUBTITULO = 0.958    # subtítulo
Y_PLOT = 0.345         # borda inferior do gráfico
CAIXA_LEGENDA = [0.08, 0.158, 0.84, 0.125]   # legenda de documentos [esq, base, larg, alt]
Y_COMO_LER = 0.152     # parágrafo "Como ler o gráfico"
Y_NOTA = 0.030         # nota com as fórmulas
MARGEM_BLOCOS_PT = 4   # folga mínima exigida entre dois blocos de texto, em pontos
LARGURA_COMO_LER = 118  # caracteres por linha do parágrafo


# =============================================================================
# 3. Utilidades
# =============================================================================
def configurar_estilo() -> None:
    """Aplica o estilo tipográfico da figura (fonte sem serifa, texto vetorial
    no PDF, sinal de menos unicode)."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONTES,
        "font.size": 10,
        "pdf.fonttype": 42,   # fontes como texto (editável/pesquisável no PDF)
        "ps.fonttype": 42,
        "axes.unicode_minus": True,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    })


def escurecer(cor: str, fator: float = 0.72) -> str:
    """Versão mais escura da cor, usada na borda da bolha — dá contraste
    suficiente mesmo nos tons claros da paleta."""
    r, g, b = matplotlib.colors.to_rgb(cor)
    return matplotlib.colors.to_hex((r * fator, g * fator, b * fator))


def cor_do_pais(pais: str) -> str:
    return CORES_PAIS.get(str(pais).strip(), COR_FALLBACK)


def raio_pt(massa: float, escala: float) -> float:
    """Raio da bolha em pontos, para área proporcional à massa."""
    return math.sqrt(massa * escala / math.pi)


def carregar_coordenadas(dir_base: Path | str = DIR_SCRIPT,
                         versao: str = "soma_uni",
                         entrada: Path | str | None = None) -> pd.DataFrame:
    """Lê coordenadas.csv (versão principal) ou robustez.csv (demais versões).
    Devolve um DataFrame com, ao menos: arquivo, rotulo, documento, país, ano,
    massa, X, Y."""
    dir_base = Path(dir_base)
    coord = pd.read_csv(dir_base / "coordenadas.csv")
    if versao == "soma_uni":
        df = pd.read_csv(entrada) if entrada else coord
    else:
        rob = pd.read_csv(entrada or dir_base / "robustez.csv")
        v = versao
        df = rob[["arquivo", f"{v}_massa", f"{v}_X", f"{v}_Y"]].rename(
            columns={f"{v}_massa": "massa", f"{v}_X": "X", f"{v}_Y": "Y"})
        df = df.merge(coord[["arquivo", "documento", "país", "ano", "rotulo"]],
                      on="arquivo", how="left")
    faltam = {"arquivo", "rotulo", "país", "ano", "massa", "X", "Y"} - set(df.columns)
    if faltam:
        raise ValueError(f"Colunas ausentes na entrada: {sorted(faltam)}")
    return df


# =============================================================================
# 4. Desenho
# =============================================================================
def _desenhar_eixos(ax) -> None:
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    for lado in ("left", "bottom"):                 # eixos cruzando a origem
        ax.spines[lado].set_position("zero")
        ax.spines[lado].set_color(CINZA_EIXO)
        ax.spines[lado].set_linewidth(1.0)
        ax.spines[lado].set_zorder(1)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for v in (-0.5, 0.5):                           # referências discretas em ±0,5
        ax.axhline(v, color=CINZA_LINHA, linewidth=0.6, linestyle=(0, (2, 4)), zorder=0)
        ax.axvline(v, color=CINZA_LINHA, linewidth=0.6, linestyle=(0, (2, 4)), zorder=0)
    ticks = [-1, -0.5, 0.5, 1]
    rot = {-1: "−1", -0.5: "−0,5", 0.5: "0,5", 1: "1"}
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels([rot[t] for t in ticks])
    ax.set_yticklabels([rot[t] for t in ticks])
    ax.tick_params(axis="both", length=3, width=0.8, color=CINZA_EIXO,
                   labelsize=9, labelcolor=CINZA_TEXTO, pad=3)


def _desenhar_polos(ax) -> dict:
    """Desenha as quatro caixas de polo e devolve {nome: objeto de texto}, para
    que entrem na conferência de sobreposição."""
    pos = {"topo": ((0, 1), (0, 12), "center", "bottom"),
           "base": ((0, -1), (0, -14), "center", "top"),
           "esquerda": ((-1, 0), (-12, 0), "right", "center"),
           "direita": ((1, 0), (12, 0), "left", "center")}
    caixas = {}
    for chave, texto in POLOS.items():
        xy, dxy, ha, va = pos[chave]
        caixas[f"polo {chave}"] = ax.annotate(
            textwrap.fill(texto, LARGURA_POLO[chave]), xy=xy, xycoords="data",
            xytext=dxy, textcoords="offset points", ha=ha, va=va,
            fontsize=9.5, color=INK, linespacing=1.25, annotation_clip=False,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#f4f4f4",
                      edgecolor="#bdbdbd", linewidth=0.6), zorder=5)
    return caixas


def _desenhar_bolhas(ax, df: pd.DataFrame, escala: float) -> tuple[list, list]:
    """Desenha as bolhas (maiores primeiro, para que as menores fiquem por cima)
    e os rótulos. Devolve (bolhas, rotulos) para a conferência de sobreposição."""
    bolhas, rotulos = [], []
    for _, r in df.sort_values("massa", ascending=False).iterrows():
        foco = r["arquivo"] == DOC_FOCO
        massa = float(r["massa"])
        cor = cor_do_pais(r["país"])
        rr = raio_pt(massa, escala)

        # halo branco: separa bolhas que se tocam (2 px de superfície entre marcas)
        ax.scatter(r["X"], r["Y"], s=math.pi * (rr + 1.5) ** 2,
                   facecolor="white", edgecolor="none", zorder=2.5)
        ax.scatter(r["X"], r["Y"], s=massa * escala, facecolor=cor,
                   edgecolor=escurecer(cor), linewidth=0.9, zorder=3)
        if foco:  # anel tracejado: marca redundante, não codificada só por cor
            ax.scatter(r["X"], r["Y"], s=math.pi * (rr + 3.5) ** 2, facecolor="none",
                       edgecolor=cor, linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=3.1)
            rr += 3.5

        bolhas.append((r["rotulo"], float(r["X"]), float(r["Y"]), rr))
        dx, dy, ha, va = OFFSETS.get(r["arquivo"], OFFSET_PADRAO)
        dx_total = dx + (rr * np.sign(dx) if dx else 0)
        dy_total = dy + (rr * np.sign(dy) if dy else 0)
        guia = None
        if r["arquivo"] in COM_GUIA:
            guia = dict(arrowstyle="-", color="#8c8c8c", linewidth=0.6,
                        shrinkA=2, shrinkB=rr + 1.0)
        t = ax.annotate(r["rotulo"], xy=(r["X"], r["Y"]), xytext=(dx_total, dy_total),
                        textcoords="offset points", ha=ha, va=va, fontsize=10,
                        fontweight="bold" if foco else "normal", color=INK, zorder=4,
                        arrowprops=guia)
        rotulos.append((r["rotulo"], t))
    return bolhas, rotulos


def _legenda_tamanho(ax, escala: float) -> None:
    """Legenda de tamanho das bolhas, com três valores de referência. Fica no
    quadrante inferior direito, vazio nesta versão dos dados."""
    handles = [ax.scatter([], [], s=m * escala, facecolor="white",
                          edgecolor="#6f6f6f", linewidth=0.8)
               for m in REFERENCIAS_TAMANHO]
    leg = ax.legend(handles, [str(m) for m in REFERENCIAS_TAMANHO],
                    title="Massa temática\nG2 + G3 + G4 + G5\n(por 1.000 tokens)",
                    loc="lower right", bbox_to_anchor=(0.995, 0.02), frameon=False,
                    labelspacing=1.7, handletextpad=1.0, borderpad=0.4,
                    fontsize=9, title_fontsize=9, scatterpoints=1, ncol=1)
    leg.get_title().set_multialignment("center")
    leg.get_title().set_color(CINZA_TEXTO)
    for txt in leg.get_texts():
        txt.set_color(CINZA_TEXTO)


def _legenda_documentos(fig, df: pd.DataFrame):
    """Legenda que identifica cada bolha: país/bloco, nome do documento e ano.
    O documento em foco (PBIA) aparece em negrito, como na figura."""
    ax_leg = fig.add_axes(CAIXA_LEGENDA)
    ax_leg.axis("off")

    por_arquivo = df.set_index("arquivo")
    ordem = [a for a in ORDEM_LEGENDA if a in por_arquivo.index]
    ordem += [a for a in por_arquivo.index if a not in ordem]  # documentos novos

    handles, rotulos, negrito = [], [], []
    for arquivo in ordem:
        linha = por_arquivo.loc[arquivo]
        cor = cor_do_pais(linha["país"])
        nome = NOME_LEGENDA.get(arquivo, str(linha["documento"]))
        handles.append(Line2D([], [], marker="o", linestyle="none", markersize=10,
                              markerfacecolor=cor, markeredgecolor=escurecer(cor),
                              markeredgewidth=0.9))
        rotulos.append(f"{linha['país']} — {nome}, {int(linha['ano'])}")
        negrito.append(arquivo == DOC_FOCO)

    leg = ax_leg.legend(
        handles, rotulos, loc="upper center", bbox_to_anchor=(0.5, 1.0),
        frameon=False, ncol=1, fontsize=9.5, labelspacing=0.62,
        handletextpad=0.9, borderpad=0.0,
        title="Documentos analisados — país ou bloco, título do documento e ano de publicação",
        title_fontsize=9.5)
    leg.get_title().set_color(INK)
    leg.get_title().set_fontweight("bold")
    for txt, bold in zip(leg.get_texts(), negrito):
        txt.set_color(INK)
        if bold:
            txt.set_fontweight("bold")
    return leg


def conferir_sobreposicao(fig, ax, bolhas, rotulos) -> list[str]:
    """Confere, em pixels, se algum rótulo se sobrepõe a outro rótulo ou a uma
    bolha que não seja a sua. Devolve a lista de avisos (vazia se tudo certo)."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    dpi = fig.dpi
    caixas = {nome: t.get_window_extent(renderer) for nome, t in rotulos}
    circulos = {}
    for nome, x, y, r_pt in bolhas:
        px, py = ax.transData.transform((x, y))
        r = r_pt * dpi / 72
        circulos[nome] = Bbox.from_extents(px - r, py - r, px + r, py + r)
    avisos = []
    nomes = list(caixas)
    for i, a in enumerate(nomes):
        for b in nomes[i + 1:]:
            if caixas[a].overlaps(caixas[b]):
                avisos.append(f"rótulo '{a}' sobrepõe rótulo '{b}'")
        for b, c in circulos.items():
            if b != a and caixas[a].overlaps(c):
                avisos.append(f"rótulo '{a}' sobrepõe a bolha '{b}'")
    return avisos


def conferir_blocos(fig, blocos: dict) -> list[str]:
    """Confere se dois blocos de texto da figura (título, subtítulo, caixas de
    polo, legenda, parágrafo explicativo, nota) se sobrepõem — útil ao editar
    os textos ou o espaçamento. Cada caixa é ampliada em MARGEM_BLOCOS_PT para
    exigir também uma folga visual mínima entre blocos vizinhos."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    margem = MARGEM_BLOCOS_PT * fig.dpi / 72.0
    caixas = {}
    for nome, obj in blocos.items():
        if obj is None:
            continue
        try:
            caixas[nome] = obj.get_window_extent(renderer).padded(margem)
        except Exception:                     # objeto sem extensão mensurável
            continue
    avisos, nomes = [], list(caixas)
    for i, a in enumerate(nomes):
        for b in nomes[i + 1:]:
            if caixas[a].overlaps(caixas[b]):
                avisos.append(f"o bloco '{a}' sobrepõe o bloco '{b}'")
    return avisos


def construir_figura(df: pd.DataFrame, versao: str = "soma_uni",
                     escala: float = ESCALA_BOLHA, titulo: str = TITULO,
                     subtitulo: str = SUBTITULO, mostrar_titulo: bool = True,
                     ) -> tuple[plt.Figure, plt.Axes, list[str]]:
    """Monta a figura completa e devolve (fig, ax, avisos).

    `avisos` lista sobreposições detectadas automaticamente: entre rótulos e
    bolhas dentro do gráfico e entre os blocos de texto da figura. Uma lista
    vazia significa que nada colidiu."""
    configurar_estilo()
    fig = plt.figure(figsize=FIGSIZE)
    larg = LADO_PLOT / FIGSIZE[0]
    alt = LADO_PLOT / FIGSIZE[1]
    ax = fig.add_axes([(1 - larg) / 2, Y_PLOT, larg, alt])

    _desenhar_eixos(ax)
    polos = _desenhar_polos(ax)
    bolhas, rotulos = _desenhar_bolhas(ax, df, escala)
    _legenda_tamanho(ax, escala)
    legenda = _legenda_documentos(fig, df)

    blocos = {"legenda de documentos": legenda, **polos}
    if mostrar_titulo:
        blocos["título"] = fig.text(0.5, Y_TITULO, titulo, ha="center", va="top",
                                    fontsize=15.5, fontweight="bold", color=INK)
        blocos["subtítulo"] = fig.text(0.5, Y_SUBTITULO, subtitulo, ha="center", va="top",
                                       fontsize=10.5, color=CINZA_TEXTO, linespacing=1.45)

    blocos["como ler"] = fig.text(
        0.5, Y_COMO_LER, textwrap.fill(COMO_LER, LARGURA_COMO_LER),
        ha="center", va="top", fontsize=9.5, color=INK, linespacing=1.45)

    nota = NOTA if versao == "soma_uni" else NOTA.replace("soma das taxas", {
        "media_uni": "média das taxas",
        "soma_uni_bi": "soma das taxas (unigramas + bigramas)"}[versao])
    blocos["nota de rodapé"] = fig.text(0.5, Y_NOTA, nota, ha="center", va="bottom",
                                        fontsize=9, color=CINZA_TEXTO)

    avisos = conferir_sobreposicao(fig, ax, bolhas, rotulos)
    avisos += conferir_blocos(fig, blocos)
    return fig, ax, avisos


def salvar(fig, saida: Path | str = DIR_SCRIPT, base: str = "figura") -> tuple[Path, Path]:
    """Grava PNG em 300 dpi e PDF vetorial; devolve os dois caminhos."""
    saida = Path(saida)
    saida.mkdir(parents=True, exist_ok=True)
    png, pdf = saida / f"{base}.png", saida / f"{base}.pdf"
    fig.savefig(png, dpi=300, bbox_inches="tight", pad_inches=0.2)
    fig.savefig(pdf, bbox_inches="tight", pad_inches=0.2)
    return png, pdf


def main() -> None:
    matplotlib.use("Agg")  # só na linha de comando; no notebook usa o backend inline
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--versao", choices=["soma_uni", "media_uni", "soma_uni_bi"], default="soma_uni")
    p.add_argument("--entrada", type=Path, default=None,
                   help="CSV de entrada (padrão: coordenadas.csv / robustez.csv)")
    p.add_argument("--saida", type=Path, default=DIR_SCRIPT, help="pasta de saída")
    p.add_argument("--escala", type=float, default=ESCALA_BOLHA, help="pontos² por unidade de massa")
    p.add_argument("--sem-titulo", action="store_true", help="não desenha título e subtítulo")
    args = p.parse_args()

    df = carregar_coordenadas(DIR_SCRIPT, args.versao, args.entrada)
    fig, ax, avisos = construir_figura(df, args.versao, args.escala,
                                       mostrar_titulo=not args.sem_titulo)
    for aviso in avisos:
        print("AVISO:", aviso)

    base = "figura" if args.versao == "soma_uni" else f"figura_{args.versao}"
    png, pdf = salvar(fig, args.saida, base)
    print(f"Gravados: {png} e {pdf}")


if __name__ == "__main__":
    main()
