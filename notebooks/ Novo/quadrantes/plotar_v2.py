#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
plotar_v2.py — Gráfico de quadrantes com estética revisada (versão 2)

É a mesma figura de plotar.py — mesmos dados (coordenadas.csv), mesmos eixos,
limites, linhas de referência, caixas dos quatro vocabulários, rótulos e
deslocamentos dos rótulos — com mudanças apenas estéticas:

  1. sem o parágrafo "Como ler o gráfico";
  2. legenda de documentos junto do gráfico, com a legenda de massa temática
     no mesmo painel, em dois arranjos:
       - "quadrante": painel no canto superior esquerdo, sobre o quadrante
         vazio (legenda de documentos em cima, massa temática logo abaixo);
       - "abaixo": painel compacto sob o gráfico (legenda de documentos à
         esquerda, massa temática ao lado, à direita);
  3. cores: Estados Unidos em azul-escuro, China em vermelho, União Europeia
     em amarelo e Brasil em verde;
  4. gráfico maior (lado de 7,4 pol. em vez de 6,9), já que o espaço antes
     ocupado pelo parágrafo e pela legenda longa foi liberado.

plotar.py, figura.png e figura.pdf NÃO são alterados. Este módulo importa
plotar e reaproveita dele os textos (TITULO, SUBTITULO, POLOS, NOTA,
NOME_LEGENDA), os eixos, as caixas de polo, os deslocamentos dos rótulos
(OFFSETS, COM_GUIA) e as conferências de sobreposição. Qualquer edição feita
nesses textos em plotar.py passa a valer também aqui.

Acessibilidade: as quatro cores foram escolhidas pelo usuário (azul-escuro,
vermelho, amarelo, verde) e os tons foram ajustados para separar vermelho e
verde em daltonismo: separação mínima ΔE 11,5 (OKLab ×100) entre todos os
pares em deuteranopia e protanopia, 22,2 em tritanopia. O amarelo tem pouco
contraste contra o branco (1,9:1), por isso toda bolha tem borda escura e
rótulo textual ao lado; o PBIA mantém anel tracejado e rótulo em negrito.

Uso na linha de comando:
  python plotar_v2.py                      # grava os dois arranjos
  python plotar_v2.py --layout quadrante   # só figura_v2_quadrante.png/.pdf
  python plotar_v2.py --layout abaixo      # só figura_v2_abaixo.png/.pdf

Uso dentro de um notebook (ver a seção 10 de quadrantes_planos_ia.ipynb):
  import plotar_v2
  df = plotar_v2.plotar.carregar_coordenadas()
  fig, ax, avisos = plotar_v2.construir_figura(df, layout="quadrante")
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib.transforms import Affine2D, Bbox

import plotar

DIR_SCRIPT = Path(__file__).resolve().parent

# =============================================================================
# 1. Cores — uma por país/bloco. Edite aqui para trocar a paleta (não afeta
#    plotar.py). Se trocar, revalide a separação para daltonismo.
# =============================================================================
CORES_PAIS = {
    "Brasil": "#2E9E4F",          # verde
    "Estados Unidos": "#1F3F8F",  # azul-escuro
    "União Europeia": "#EDB120",  # amarelo
    "China": "#B2182B",           # vermelho
}
COR_FALLBACK = "#7f7f7f"          # país fora do dicionário acima

COR_BORDA_PAINEL = "#c4c4c4"
COR_SEPARADOR = "#dedede"

# =============================================================================
# 2. Textos próprios desta versão (os demais vêm de plotar.py)
# =============================================================================
TITULO_DOCUMENTOS = "Documentos analisados (país ou bloco — título, ano)"
TITULO_MASSA = "Massa temática"
SUBTITULO_MASSA = "G2 + G3 + G4 + G5, por 1.000 tokens"

# =============================================================================
# 3. Dimensões, em polegadas. As distâncias verticais são medidas a partir do
#    topo da figura. construir_figura avisa se dois blocos se sobrepuserem.
# =============================================================================
LADO_PLOT = 7.4          # lado do quadrado do gráfico (plotar.py usa 6,9)
MARGEM_LATERAL = 1.95    # espaço à esquerda e à direita para as caixas B e D
TOPO_TITULO = 0.15       # topo do título
TOPO_SUBTITULO = 0.53    # topo do subtítulo
TOPO_PLOT = 1.65         # borda superior do gráfico
ALTURA_EXTRA = {"quadrante": 1.35, "abaixo": 3.35}  # espaço abaixo do gráfico
PAD_PAINEL = 0.14        # margem interna do painel de legenda
SEPARACAO_SECOES = 0.24  # distância entre as duas seções do painel
FOLGA_PAINEL_ABAIXO = 0.30  # entre a caixa do vocabulário C e o painel ("abaixo")
FOLGA_NOTA = 0.30        # entre o último bloco e a nota de rodapé

LAYOUTS = ("quadrante", "abaixo")


# =============================================================================
# 4. Utilidades
# =============================================================================
def cor_do_pais(pais: str, cores: dict | None = None) -> str:
    return (cores or CORES_PAIS).get(str(pais).strip(), COR_FALLBACK)


def _pol(fig):
    """Transformação de polegadas (a partir do canto inferior esquerdo da
    figura) para a tela. Passa por fig.transFigure para continuar correta
    quando a figura é gravada com bbox_inches="tight" — fig.dpi_scale_trans
    não acompanha esse recorte e deslocaria o painel e a nota."""
    largura, altura = fig.get_size_inches()
    return Affine2D().scale(1 / largura, 1 / altura) + fig.transFigure


def _extensao_pol(fig, artista, renderer) -> Bbox:
    """Caixa de um artista em polegadas, a partir do canto inferior esquerdo
    da figura (independe do dpi usado ao gravar)."""
    return artista.get_window_extent(renderer).transformed(_pol(fig).inverted())


def _mover_legenda(leg, x: float, y: float) -> None:
    """Reposiciona o canto superior esquerdo de uma legenda (em polegadas)."""
    leg.set_bbox_to_anchor((x, y), transform=_pol(leg.figure))


# =============================================================================
# 5. Desenho
# =============================================================================
def _desenhar_bolhas(ax, df: pd.DataFrame, escala: float, cores: dict) -> tuple[list, list]:
    """Igual a plotar._desenhar_bolhas — mesmas posições, tamanhos, halo, anel
    do PBIA, rótulos, deslocamentos e linhas-guia —, mudando só a cor. Cada
    bolha recebe um gid para que conferir_posicoes possa lê-la de volta."""
    bolhas, rotulos = [], []
    for _, r in df.sort_values("massa", ascending=False).iterrows():
        foco = r["arquivo"] == plotar.DOC_FOCO
        massa = float(r["massa"])
        cor = cor_do_pais(r["país"], cores)
        rr = plotar.raio_pt(massa, escala)

        ax.scatter(r["X"], r["Y"], s=math.pi * (rr + 1.5) ** 2,
                   facecolor="white", edgecolor="none", zorder=2.5)
        ax.scatter(r["X"], r["Y"], s=massa * escala, facecolor=cor,
                   edgecolor=plotar.escurecer(cor), linewidth=0.9, zorder=3,
                   gid=f"bolha:{r['arquivo']}")
        if foco:
            ax.scatter(r["X"], r["Y"], s=math.pi * (rr + 3.5) ** 2, facecolor="none",
                       edgecolor=cor, linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=3.1)
            rr += 3.5

        bolhas.append((r["rotulo"], float(r["X"]), float(r["Y"]), rr))
        dx, dy, ha, va = plotar.OFFSETS.get(r["arquivo"], plotar.OFFSET_PADRAO)
        dx_total = dx + (rr * np.sign(dx) if dx else 0)
        dy_total = dy + (rr * np.sign(dy) if dy else 0)
        guia = None
        if r["arquivo"] in plotar.COM_GUIA:
            guia = dict(arrowstyle="-", color="#8c8c8c", linewidth=0.6,
                        shrinkA=2, shrinkB=rr + 1.0)
        t = ax.annotate(r["rotulo"], xy=(r["X"], r["Y"]), xytext=(dx_total, dy_total),
                        textcoords="offset points", ha=ha, va=va, fontsize=10,
                        fontweight="bold" if foco else "normal", color=plotar.INK,
                        zorder=4, arrowprops=guia)
        rotulos.append((r["rotulo"], t))
    return bolhas, rotulos


def _legenda_documentos(fig, df: pd.DataFrame, cores: dict):
    """Legenda de documentos: país/bloco, título e ano, na ordem de
    plotar.ORDEM_LEGENDA; o PBIA em negrito, como no gráfico."""
    por_arquivo = df.set_index("arquivo")
    ordem = [a for a in plotar.ORDEM_LEGENDA if a in por_arquivo.index]
    ordem += [a for a in por_arquivo.index if a not in ordem]

    handles, rotulos, negrito = [], [], []
    for arquivo in ordem:
        linha = por_arquivo.loc[arquivo]
        cor = cor_do_pais(linha["país"], cores)
        nome = plotar.NOME_LEGENDA.get(arquivo, str(linha["documento"]))
        handles.append(Line2D([], [], marker="o", linestyle="none", markersize=9.5,
                              markerfacecolor=cor, markeredgecolor=plotar.escurecer(cor),
                              markeredgewidth=0.9))
        rotulos.append(f"{linha['país']} — {nome}, {int(linha['ano'])}")
        negrito.append(arquivo == plotar.DOC_FOCO)

    leg = fig.legend(handles, rotulos, loc="upper left", bbox_to_anchor=(0, 0),
                     bbox_transform=_pol(fig), frameon=False, ncol=1,
                     fontsize=9.5, labelspacing=0.55, handletextpad=0.7,
                     handlelength=1.2, borderpad=0.0, borderaxespad=0.0,
                     title=TITULO_DOCUMENTOS, title_fontsize=9.5, alignment="left")
    leg.set_zorder(5)
    leg.get_title().set_fontweight("bold")
    leg.get_title().set_color(plotar.INK)
    for txt, bold in zip(leg.get_texts(), negrito):
        txt.set_color(plotar.INK)
        if bold:
            txt.set_fontweight("bold")
    return leg


def _legenda_massa(fig, escala: float, layout: str, renderer) -> dict:
    """Legenda de tamanho das bolhas, desenhada à mão para que cada círculo
    fique centrado no seu número e não invada o título: em linha no arranjo
    "quadrante", em coluna no arranjo "abaixo".

    O raio de cada círculo é o raio real das bolhas do gráfico — num scatter,
    o marcador de área s (pontos²) tem diâmetro √s pontos —, com a mesma
    escala (ESCALA_BOLHA). Todos os artistas nascem com o canto superior
    esquerdo em (0, 0) e usam a transformação `deslocamento`; quem chama
    posiciona o bloco com deslocamento.translate(x, y) (em polegadas).
    Devolve {"deslocamento", "largura", "altura"}."""
    deslocamento = Affine2D()
    t = deslocamento + _pol(fig)
    por_pol = _pol(fig).inverted()

    def medir(texto):
        return texto.get_window_extent(renderer).transformed(por_pol)

    titulo = fig.text(0, 0, TITULO_MASSA, transform=t, ha="left", va="top",
                      fontsize=9.5, fontweight="bold", color=plotar.INK, zorder=5)
    y = -medir(titulo).height - 0.05
    sub = fig.text(0, y, SUBTITULO_MASSA, transform=t, ha="left", va="top",
                   fontsize=9, color=plotar.CINZA_TEXTO, zorder=5)
    y -= medir(sub).height + 0.12
    largura = max(medir(titulo).width, medir(sub).width)

    raios = [math.sqrt(m * escala) / 2 / 72 for m in plotar.REFERENCIAS_TAMANHO]
    r_max = max(raios)

    def circulo(cx, cy, r, valor):
        fig.add_artist(Circle((cx, cy), r, transform=t, facecolor="white",
                              edgecolor="#6f6f6f", linewidth=0.8, zorder=5))
        return fig.text(cx + r + 0.07, cy, str(valor), transform=t, ha="left",
                        va="center", fontsize=9.5, color=plotar.CINZA_TEXTO, zorder=5)

    if layout == "quadrante":               # círculos lado a lado, centros alinhados
        x, cy = 0.0, y - r_max
        for r, valor in zip(raios, plotar.REFERENCIAS_TAMANHO):
            rotulo = circulo(x + r, cy, r, valor)
            x = x + 2 * r + 0.07 + medir(rotulo).width + 0.30
        largura = max(largura, x - 0.30)
        base = cy - r_max
    else:                                   # círculos empilhados, centros alinhados
        for r, valor in zip(raios, plotar.REFERENCIAS_TAMANHO):
            rotulo = circulo(r_max, y - r, r, valor)
            largura = max(largura, 2 * r_max + 0.07 + medir(rotulo).width)
            y -= 2 * r + 0.06
        base = y + 0.06
    return {"deslocamento": deslocamento, "largura": largura, "altura": -base}


def _moldura(fig, x0: float, y0: float, largura: float, altura: float) -> FancyBboxPatch:
    """Fundo branco e borda fina do painel de legenda (em polegadas). Fica
    acima do gráfico (encobre as linhas pontilhadas de ±0,5 só onde o painel
    está) e abaixo dos textos da legenda."""
    moldura = FancyBboxPatch((x0, y0), largura, altura,
                             boxstyle="round,pad=0,rounding_size=0.06",
                             transform=_pol(fig), facecolor="white",
                             edgecolor=COR_BORDA_PAINEL, linewidth=0.7, zorder=1.5)
    fig.add_artist(moldura)
    return moldura


def _painel_quadrante(fig, ax, df, escala, cores, polos, renderer):
    """Painel no canto superior esquerdo: o topo coincide com a borda superior
    do gráfico e a margem esquerda com a da caixa do vocabulário B."""
    caixa_b = _extensao_pol(fig, polos["polo esquerda"], renderer)
    topo = _extensao_pol(fig, ax, renderer).y1
    x0 = caixa_b.x0

    leg_doc = _legenda_documentos(fig, df, cores)
    _mover_legenda(leg_doc, x0 + PAD_PAINEL, topo - PAD_PAINEL)
    fig.canvas.draw()
    ext_doc = _extensao_pol(fig, leg_doc, renderer)

    massa = _legenda_massa(fig, escala, "quadrante", renderer)
    y_massa = ext_doc.y0 - SEPARACAO_SECOES
    massa["deslocamento"].translate(x0 + PAD_PAINEL, y_massa)

    largura = max(ext_doc.width, massa["largura"]) + 2 * PAD_PAINEL
    base = y_massa - massa["altura"] - PAD_PAINEL
    moldura = _moldura(fig, x0, base, largura, topo - base)
    y_sep = ext_doc.y0 - SEPARACAO_SECOES / 2
    fig.add_artist(Line2D([x0 + PAD_PAINEL, x0 + largura - PAD_PAINEL], [y_sep, y_sep],
                          transform=_pol(fig), color=COR_SEPARADOR,
                          linewidth=0.7, zorder=4))
    return moldura


def _painel_abaixo(fig, ax, df, escala, cores, polos, renderer, largura_fig):
    """Painel sob o gráfico: documentos à esquerda, massa temática ao lado, à
    direita, separados por um filete vertical; o conjunto fica centralizado."""
    caixa_c = _extensao_pol(fig, polos["polo base"], renderer)
    topo = caixa_c.y0 - FOLGA_PAINEL_ABAIXO

    leg_doc = _legenda_documentos(fig, df, cores)
    _mover_legenda(leg_doc, 0, topo - PAD_PAINEL)
    fig.canvas.draw()
    ext_doc = _extensao_pol(fig, leg_doc, renderer)
    massa = _legenda_massa(fig, escala, "abaixo", renderer)

    vao = 2 * SEPARACAO_SECOES + 0.1
    largura = PAD_PAINEL + ext_doc.width + vao + massa["largura"] + PAD_PAINEL
    x0 = (largura_fig - largura) / 2
    _mover_legenda(leg_doc, x0 + PAD_PAINEL, topo - PAD_PAINEL)
    x_sep = x0 + PAD_PAINEL + ext_doc.width + vao / 2
    massa["deslocamento"].translate(x_sep + vao / 2, topo - PAD_PAINEL)

    base = topo - PAD_PAINEL - max(ext_doc.height, massa["altura"]) - PAD_PAINEL
    moldura = _moldura(fig, x0, base, largura, topo - base)
    fig.add_artist(Line2D([x_sep, x_sep], [base + PAD_PAINEL, topo - PAD_PAINEL],
                          transform=_pol(fig), color=COR_SEPARADOR,
                          linewidth=0.7, zorder=4))
    return moldura


# =============================================================================
# 6. Conferências
# =============================================================================
def conferir_posicoes(ax, df: pd.DataFrame) -> list[str]:
    """Lê de volta, da própria figura, a posição de cada bolha desenhada e a
    compara com X e Y do CSV de entrada. Devolve avisos (vazia = idênticas)."""
    desenhadas = {}
    for col in ax.collections:
        gid = col.get_gid() or ""
        if gid.startswith("bolha:"):
            desenhadas[gid[len("bolha:"):]] = np.asarray(col.get_offsets(), dtype=float)[0]
    avisos = []
    for _, r in df.iterrows():
        xy = desenhadas.get(r["arquivo"])
        esperado = np.array([float(r["X"]), float(r["Y"])])
        if xy is None:
            avisos.append(f"o documento '{r['rotulo']}' não foi desenhado")
        elif not np.array_equal(xy, esperado):
            avisos.append(f"'{r['rotulo']}' desenhado em {tuple(xy)}, "
                          f"mas o CSV diz {tuple(esperado)}")
    return avisos


def conferir_painel(fig, ax, moldura, bolhas, rotulos) -> list[str]:
    """Confere se o painel de legenda encobre alguma bolha, rótulo de bolha
    ou valor dos eixos."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    painel = moldura.get_window_extent(renderer)
    avisos = []
    for nome, x, y, r_pt in bolhas:
        px, py = ax.transData.transform((x, y))
        r = r_pt * fig.dpi / 72
        if painel.overlaps(Bbox.from_extents(px - r, py - r, px + r, py + r)):
            avisos.append(f"o painel de legenda encobre a bolha '{nome}'")
    for nome, t in rotulos:
        if painel.overlaps(t.get_window_extent(renderer)):
            avisos.append(f"o painel de legenda encobre o rótulo '{nome}'")
    for t in ax.get_xticklabels() + ax.get_yticklabels():
        if t.get_text() and painel.overlaps(t.get_window_extent(renderer)):
            avisos.append(f"o painel de legenda encobre o valor de eixo '{t.get_text()}'")
    return avisos


# =============================================================================
# 7. Figura
# =============================================================================
def construir_figura(df: pd.DataFrame, layout: str = "quadrante",
                     versao: str = "soma_uni", escala: float = plotar.ESCALA_BOLHA,
                     cores: dict | None = None, titulo: str = plotar.TITULO,
                     subtitulo: str = plotar.SUBTITULO, mostrar_titulo: bool = True,
                     ) -> tuple[plt.Figure, plt.Axes, list[str]]:
    """Monta a figura e devolve (fig, ax, avisos).

    layout: "quadrante" (legenda no canto superior esquerdo) ou "abaixo"
    (legenda compacta sob o gráfico, com a massa temática ao lado).

    `avisos` reúne quatro conferências automáticas: posição de cada bolha
    igual à do CSV; rótulos sem colisão com rótulos ou bolhas; painel de
    legenda sem encobrir bolhas, rótulos ou valores dos eixos; blocos de
    texto sem sobreposição. Lista vazia = tudo certo."""
    if layout not in LAYOUTS:
        raise ValueError(f"layout deve ser um de {LAYOUTS}, não {layout!r}")
    cores = cores or CORES_PAIS
    plotar.configurar_estilo()

    largura_fig = LADO_PLOT + 2 * MARGEM_LATERAL
    altura_fig = TOPO_PLOT + LADO_PLOT + ALTURA_EXTRA[layout]
    fig = plt.figure(figsize=(largura_fig, altura_fig))
    ax = fig.add_axes([MARGEM_LATERAL / largura_fig,
                       (altura_fig - TOPO_PLOT - LADO_PLOT) / altura_fig,
                       LADO_PLOT / largura_fig, LADO_PLOT / altura_fig])

    plotar._desenhar_eixos(ax)
    polos = plotar._desenhar_polos(ax)
    bolhas, rotulos = _desenhar_bolhas(ax, df, escala, cores)

    blocos = dict(polos)
    if mostrar_titulo:
        blocos["título"] = fig.text(0.5, 1 - TOPO_TITULO / altura_fig, titulo,
                                    ha="center", va="top", fontsize=15.5,
                                    fontweight="bold", color=plotar.INK)
        blocos["subtítulo"] = fig.text(0.5, 1 - TOPO_SUBTITULO / altura_fig, subtitulo,
                                       ha="center", va="top", fontsize=10.5,
                                       color=plotar.CINZA_TEXTO, linespacing=1.45)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    if layout == "quadrante":
        moldura = _painel_quadrante(fig, ax, df, escala, cores, polos, renderer)
    else:
        moldura = _painel_abaixo(fig, ax, df, escala, cores, polos, renderer, largura_fig)
    blocos["painel de legenda"] = moldura

    # nota de rodapé logo abaixo do bloco mais baixo (caixa C ou painel)
    fig.canvas.draw()
    base = min(_extensao_pol(fig, polos["polo base"], renderer).y0,
               _extensao_pol(fig, moldura, renderer).y0)
    nota = plotar.NOTA if versao == "soma_uni" else plotar.NOTA.replace("soma das taxas", {
        "media_uni": "média das taxas",
        "soma_uni_bi": "soma das taxas (unigramas + bigramas)"}[versao])
    blocos["nota de rodapé"] = fig.text(largura_fig / 2, base - FOLGA_NOTA, nota,
                                        transform=_pol(fig), ha="center",
                                        va="top", fontsize=9, color=plotar.CINZA_TEXTO)

    avisos = conferir_posicoes(ax, df)
    avisos += plotar.conferir_sobreposicao(fig, ax, bolhas, rotulos)
    avisos += conferir_painel(fig, ax, moldura, bolhas, rotulos)
    avisos += plotar.conferir_blocos(fig, blocos)
    return fig, ax, avisos


def salvar(fig, saida: Path | str = DIR_SCRIPT, base: str = "figura_v2_quadrante"):
    """Grava PNG em 300 dpi e PDF vetorial (mesmo padrão de plotar.salvar)."""
    return plotar.salvar(fig, saida, base)


def main() -> None:
    matplotlib.use("Agg")
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--layout", choices=LAYOUTS + ("ambos",), default="ambos")
    p.add_argument("--versao", choices=["soma_uni", "media_uni", "soma_uni_bi"], default="soma_uni")
    p.add_argument("--entrada", type=Path, default=None,
                   help="CSV de entrada (padrão: coordenadas.csv / robustez.csv)")
    p.add_argument("--saida", type=Path, default=DIR_SCRIPT, help="pasta de saída")
    p.add_argument("--sem-titulo", action="store_true", help="não desenha título e subtítulo")
    args = p.parse_args()

    df = plotar.carregar_coordenadas(DIR_SCRIPT, args.versao, args.entrada)
    layouts = LAYOUTS if args.layout == "ambos" else (args.layout,)
    for layout in layouts:
        fig, _, avisos = construir_figura(df, layout, args.versao,
                                          mostrar_titulo=not args.sem_titulo)
        for aviso in avisos:
            print(f"AVISO ({layout}):", aviso)
        base = f"figura_v2_{layout}"
        if args.versao != "soma_uni":
            base += f"_{args.versao}"
        png, pdf = salvar(fig, args.saida, base)
        plt.close(fig)
        print(f"Gravados: {png} e {pdf}")


if __name__ == "__main__":
    main()
