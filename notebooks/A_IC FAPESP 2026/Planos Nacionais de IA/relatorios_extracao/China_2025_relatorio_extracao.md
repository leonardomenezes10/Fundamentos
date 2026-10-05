# Relatório de extração — Opinions of the State Council on Deepening the Implementation of the “Artificial Intelligence+” Initiative

**Arquivo-fonte:** t0652_AI_plus_opinions_EN (2).pdf (10 páginas) · **JSON:** `China_2025_extracao.json` · **Data:** 2026-10-04

## 1. Resumo

Primeira extração deste plano. O JSON traz o texto integral das *Opinions* do Conselho de Estado da China sobre a iniciativa "AI+", com data de 21 de agosto de 2025. O texto extraído é a tradução para o inglês publicada pelo CSET, que é o próprio arquivo-fonte. Foram extraídas **64 unidades** (35 títulos internos, 29 parágrafos e nenhum item de lista), com **2.866 palavras** e 21.983 caracteres, das páginas 1 a 10. O arquivo-fonte foi recebido só como anexo da conversa. Por isso `source_sha256 = null`, e recomenda-se gravá-lo nesta pasta para que a extração possa ser reproduzida.

## 2. O que foi incluído

- **Título** (`document.title`): tirado do cabeçalho do texto na p. 1. Não há subtítulo (`subtitle = null`).
- **Parágrafo de abertura** (p. 1–2): expõe a finalidade das *Opinions* e fica antes da parte I (`path = []`).
- **Partes I a IV** (p. 2–10), todas em `Body`:
  - nível 1: I *Overall Requirements*, II, III e IV;
  - nível 2: os eixos (1) a (6) da parte II e os itens (7) a (14) da parte III;
  - nível 3: os itens 1., 2., 3. e 4. dentro de cada eixo (1) a (6), num total de 17.
- **Títulos corridos:** os itens de nível 3 e os itens (7) a (14) começam com uma frase em negrito que funciona como título, seguida do texto no mesmo parágrafo. Cada um foi registrado como `heading` (com o ponto final original), seguido de um `paragraph` com o restante. Nenhuma palavra foi alterada ou repetida. A divisão só permite agrupar o texto por eixo.
- **"(“compute”)"** (p. 7) foi mantido, porque é texto em inglês que faz parte da frase.

## 3. O que foi excluído e por quê

- **Quadro editorial do CSET** (p. 1): resumo do tradutor, título repetido em inglês e em chinês, autor, fonte, URLs, data da tradução, tradutor e editor. É moldura editorial e não texto do plano.
- **Número do documento** "State Council [2025] Document No. 11" (p. 1): é um identificador e não um subtítulo. Não foi para `subtitle` porque a skill 02 conta o subtítulo como texto.
- **Destinatários** "To the people’s governments of all provinces, … and their respective agencies:" (p. 1, 25 palavras): é a fórmula protocolar de endereçamento do ofício.
- **Assinatura e data do fecho** "State Council / August 21, 2025" (p. 10). A data foi para `document.date`.
- **4 notas de rodapé** (notas do tradutor, p. 5, 6 e 8) e os 4 marcadores delas no corpo: em "good houses" (p. 5), no título do item 2 de (5) (p. 6), no título de (9) e em "East-West Compute Transfer" (p. 8).
- **15 termos chineses entre parênteses** que o tradutor pôs ao lado do termo inglês, por exemplo "productive forces (生产力)", "new quality productive forces (新质生产力)" e "intelligent agents (智能体)". Estão nas p. 1 (1), 2 (6), 3 (2), 4 (4), 5 (1) e 8 (1). Esses termos são anotações da tradução e repetem em chinês um termo que já está em inglês. Na análise, contariam como palavras estranhas ao corpus. Foi retirado só o parêntese com o termo chinês e o espaço antes dele, e o restante da frase não mudou. É o mesmo tratamento que a skill dá aos marcadores de nota e às URLs.
- **Numeração de página** (p. 1–10). O documento não tem tabelas, figuras, sumário nem referências.

## 4. Normalizações aplicadas

- **Quebras de linha internas** foram removidas em todos os parágrafos com mais de uma linha.
- **Hífens originais restaurados (6 casos):** nos compostos quebrados em fim de linha, a camada de texto do PDF apagou o hífen (*largescale*, *platformbased*, *intelligencedriven*, *wholeprocess*, *EastWest*, *selfdiscipline*). O hífen é da própria palavra: aparece na página e nos mesmos compostos em outros trechos. Por isso ficou *large-scale*, *platform-based*, *intelligence-driven*, *whole-process*, *East-West* e *self-discipline*. Não houve hifenização de diagramação a desfazer.
- **Mantido como no original, sem correção:** "equal right" (p. 7), "giving rise new AI-native industry formats" (p. 3) e "“Artificial intelligence+”" com minúscula (p. 1).

## 5. Pontos que podem precisar de revisão

- **Termos chineses retirados (15).** Esta é a única intervenção dentro das frases além das previstas na skill. Se o pesquisador preferir mantê-los, é preciso reextrair.
- **Títulos corridos como `heading`.** Com a configuração padrão da skill 02, os títulos internos entram na contagem, e nada muda. Se o pesquisador desligar os títulos (`INCLUIR_TITULOS_INTERNOS = False`), saem também os 25 títulos corridos (174 palavras, de 209 em títulos). Eles têm conteúdo programático, como "Promote inclusive sharing of AI.".
- **Destinatários excluídos** (25 palavras): podem ser incluídos por comando do pesquisador.
- **`period = null`:** o documento fixa metas para 2027, 2030 e 2035, mas não declara um período de vigência.
- **Arquivo-fonte fora da pasta:** ver a seção 1.
