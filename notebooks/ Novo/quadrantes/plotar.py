#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
plotar.py — Gráfico de quadrantes dos planos nacionais de IA (etapa de figura)

Lê coordenadas.csv (gerado por calcular.py) e grava figura.png (300 dpi) e
figura.pdf na pasta deste script. Estilo acadêmico para impressão:
eixos cruzados na origem, limites simétricos [−1, 1], quatro polos
rotulados, PBIA em destaque (cor saturada, borda tracejada, rótulo em
negrito), demais planos em tom pálido da mesma família. A identidade de
cada bolha nunca depende só da cor: todas têm rótulo textual.

Uso:
  python plotar.py                       # versão principal (coordenadas.csv)
  python plotar.py --versao media_uni    # lê a versão de robustez em robustez.csv
  python plotar.py --versao soma_uni_bi  #   → grava figura_<versao>.png/.pdf

Os deslocamentos dos rótulos são manuais (dicionário OFFSETS). Após desenhar,
o script confere se algum rótulo se sobrepõe a outro rótulo ou a outra bolha
e avisa no terminal.
"""

from __future__ import annotations

import argparse
import math
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.transforms import Bbox

DIR_SCRIPT = Path(__file__).resolve().parent

# ------------------------------------------------------------------ estilo
COR_PBIA = "#D7301F"       # saturada
COR_PALIDA = "#F5A98F"     # mesma família, pálida (preenchimento dos demais)
COR_BORDA = "#D7301F"      # borda fina dos demais
INK = "#1a1a1a"
CINZA_EIXO = "#9a9a9a"
CINZA_LINHA = "#e3e3e3"
CINZA_TEXTO = "#4d4d4d"
FONTES = ["Arial", "Liberation Sans", "Helvetica", "DejaVu Sans"]

ESCALA_BOLHA = 6.0                 # pontos² por unidade de massa (área ∝ massa)
REFERENCIAS_TAMANHO = [60, 90, 120]  # massa (por 1.000 tokens) na legenda

# Rótulos dos polos (topo = A = G2; esquerda = B = G4; base = C = G5; direita = D = G3)
POLOS = {
    "topo": "Vocabulário A — Infraestrutura, computação e base material",
    "esquerda": "Vocabulário B — Estado, governança e regulação",
    "base": "Vocabulário C — Ciência, dimensão social, capital humano, inclusão e sustentabilidade",
    "direita": "Vocabulário D — Economia, indústria, difusão de mercado e competição geopolítica",
}
LARGURA_POLO = {"topo": 70, "base": 60, "esquerda": 22, "direita": 24}  # caracteres por linha

# Deslocamento manual de cada rótulo: (dx, dy) em pontos ALÉM da borda da
# bolha (o raio é somado automaticamente), alinhamento horizontal e vertical.
# Edite se as coordenadas mudarem; o script avisa se houver sobreposição.
OFFSETS = {
    "ai_continent_action_plan.json":          (8, 8, "left", "bottom"),    # acima, à direita
    "apply_ai_strategy.json":                 (-6, -7, "right", "top"),    # abaixo, à esquerda
    "americas_ai_action_plan.json":           (6, 0, "left", "center"),    # à direita
    "new_generation_ai_development_plan.json": (6, 0, "left", "center"),   # à direita
    "ai_plus.json":                           (-7, -8, "right", "top"),    # abaixo, à esquerda
    "pbia.json":                              (-7, 0, "right", "center"),  # à esquerda
}
OFFSET_PADRAO = (8, 0, "left", "center")
# Documentos cujo rótulo recebe uma linha-guia fina até a bolha (útil no
# aglomerado de bolhas próximas, onde a adjacência sozinha é ambígua).
COM_GUIA = {"ai_continent_action_plan.json", "apply_ai_strategy.json", "ai_plus.json"}

NOTA = ("X = (G3 − G4)/(G3 + G4);  Y = (G2 − G5)/(G2 + G5);  "
        "Gk = soma das taxas por 1.000 tokens dos unigramas do grupo k (top-50);  "
        "área da bolha proporcional a G2 + G3 + G4 + G5.")


def configurar_estilo() -> None:
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONTES,
        "font.size": 10,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.unicode_minus": True,
        "savefig.facecolor": "white",
    })


def carregar(args) -> pd.DataFrame:
    if args.versao == "soma_uni":
        df = pd.read_csv(args.entrada or DIR_SCRIPT / "coordenadas.csv")
    else:
        rob = pd.read_csv(args.entrada or DIR_SCRIPT / "robustez.csv")
        coord = pd.read_csv(DIR_SCRIPT / "coordenadas.csv")[["arquivo", "rotulo"]]
        v = args.versao
        df = rob[["documento", "arquivo", f"{v}_massa", f"{v}_X", f"{v}_Y"]].rename(
            columns={f"{v}_massa": "massa", f"{v}_X": "X", f"{v}_Y": "Y"})
        df = df.merge(coord, on="arquivo", how="left")
    faltam = {"arquivo", "rotulo", "massa", "X", "Y"} - set(df.columns)
    if faltam:
        raise SystemExit(f"Colunas ausentes na entrada: {sorted(faltam)}")
    return df


def raio_pt(massa: float, escala: float) -> float:
    return math.sqrt(massa * escala / math.pi)


def desenhar(df: pd.DataFrame, versao: str, escala: float) -> tuple[plt.Figure, plt.Axes, list, list]:
    fig = plt.figure(figsize=(11.0, 8.8))
    ax = fig.add_axes([0.215, 0.165, 0.57, 0.72])
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # eixos pela origem, sem moldura, sem grade densa
    for lado in ("left", "bottom"):
        ax.spines[lado].set_position("zero")
        ax.spines[lado].set_color(CINZA_EIXO)
        ax.spines[lado].set_linewidth(1.0)
        ax.spines[lado].set_zorder(1)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for v in (-0.5, 0.5):  # referências discretas em ±0,5
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

    # rótulos dos polos
    pos = {"topo": ((0, 1), (0, 12), "center", "bottom"),
           "base": ((0, -1), (0, -14), "center", "top"),
           "esquerda": ((-1, 0), (-12, 0), "right", "center"),
           "direita": ((1, 0), (12, 0), "left", "center")}
    for chave, texto in POLOS.items():
        xy, dxy, ha, va = pos[chave]
        ax.annotate(textwrap.fill(texto, LARGURA_POLO[chave]), xy=xy, xycoords="data",
                    xytext=dxy, textcoords="offset points", ha=ha, va=va,
                    fontsize=9.5, color=INK, linespacing=1.25, annotation_clip=False,
                    bbox=dict(boxstyle="round,pad=0.45", facecolor="#f4f4f4",
                              edgecolor="#bdbdbd", linewidth=0.6), zorder=5)

    # bolhas e rótulos — as maiores são desenhadas primeiro, para que as
    # menores fiquem por cima; um halo branco fino separa bolhas que se tocam
    bolhas, rotulos = [], []
    for _, r in df.sort_values("massa", ascending=False).iterrows():
        pbia = r["arquivo"] == "pbia.json"
        massa = float(r["massa"])
        rr = raio_pt(massa, escala)
        s_halo = math.pi * (rr + 1.5) ** 2
        ax.scatter(r["X"], r["Y"], s=s_halo, facecolor="white", edgecolor="none", zorder=2.5)
        ax.scatter(r["X"], r["Y"], s=massa * escala,
                   facecolor=COR_PBIA if pbia else COR_PALIDA,
                   edgecolor=COR_PBIA if pbia else COR_BORDA,
                   linewidth=0.9 if pbia else 0.7, zorder=3)
        if pbia:  # anel tracejado externo, como marca redundante (não só cor)
            s_anel = math.pi * (rr + 3.5) ** 2
            ax.scatter(r["X"], r["Y"], s=s_anel, facecolor="none", edgecolor=COR_PBIA,
                       linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=3.1)
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
                        fontweight="bold" if pbia else "normal", color=INK, zorder=4,
                        arrowprops=guia)
        rotulos.append((r["rotulo"], t))

    # legenda de tamanho (três valores de referência)
    handles = [ax.scatter([], [], s=m * escala, facecolor="white", edgecolor="#6f6f6f",
                          linewidth=0.8) for m in REFERENCIAS_TAMANHO]
    leg = ax.legend(handles, [f"{m}" for m in REFERENCIAS_TAMANHO],
                    title="Massa temática\nG2 + G3 + G4 + G5\n(por 1.000 tokens)",
                    loc="lower right", bbox_to_anchor=(0.995, 0.02), frameon=False,
                    labelspacing=1.7, handletextpad=1.0, borderpad=0.4,
                    fontsize=9, title_fontsize=9, scatterpoints=1, ncol=1)
    leg.get_title().set_multialignment("center")
    leg.get_title().set_color(CINZA_TEXTO)
    for txt in leg.get_texts():
        txt.set_color(CINZA_TEXTO)

    # nota de rodapé com as fórmulas (uma linha)
    nota = NOTA if versao == "soma_uni" else NOTA.replace("soma das taxas", {
        "media_uni": "média das taxas", "soma_uni_bi": "soma das taxas (unigramas + bigramas)"}[versao])
    fig.text(0.5, 0.035, nota, ha="center", va="bottom", fontsize=9, color=CINZA_TEXTO)
    return fig, ax, bolhas, rotulos


def conferir_sobreposicao(fig, ax, bolhas, rotulos) -> list[str]:
    """Confere, em pixels, se rótulos se sobrepõem a outros rótulos ou bolhas."""
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


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--versao", choices=["soma_uni", "media_uni", "soma_uni_bi"], default="soma_uni")
    p.add_argument("--entrada", type=Path, default=None, help="CSV de entrada (padrão: coordenadas.csv / robustez.csv)")
    p.add_argument("--saida", type=Path, default=DIR_SCRIPT, help="pasta de saída")
    p.add_argument("--escala", type=float, default=ESCALA_BOLHA, help="pontos² por unidade de massa")
    args = p.parse_args()

    configurar_estilo()
    df = carregar(args)
    fig, ax, bolhas, rotulos = desenhar(df, args.versao, args.escala)

    for aviso in conferir_sobreposicao(fig, ax, bolhas, rotulos):
        print("AVISO:", aviso)

    args.saida.mkdir(parents=True, exist_ok=True)
    base = "figura" if args.versao == "soma_uni" else f"figura_{args.versao}"
    fig.savefig(args.saida / f"{base}.png", dpi=300, bbox_inches="tight", pad_inches=0.2)
    fig.savefig(args.saida / f"{base}.pdf", bbox_inches="tight", pad_inches=0.2)
    print(f"Gravados: {args.saida / (base + '.png')} e {args.saida / (base + '.pdf')}")


if __name__ == "__main__":
    main()
