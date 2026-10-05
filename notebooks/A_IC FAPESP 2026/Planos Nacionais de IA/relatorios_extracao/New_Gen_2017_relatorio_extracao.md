# Relatório de extração — A New Generation of Artificial Intelligence Development Plan

**Arquivo-fonte:** A-New-Generation-of-Artificial-Intelligence-Development-Plan-1 (1).pdf (28 páginas; anexado à conversa, não gravado na pasta) · **JSON:** `New_Gen_2017_extracao.json` · **Data:** 2026-10-05

## 1. Resumo

Primeira extração deste plano, emitido pelo Conselho de Estado da China em 8 de julho de 2017. O texto extraído é a tradução para o inglês da Foundation for Law and International Affairs (FLIA), que é o próprio arquivo-fonte. A autoria da tradução consta na nota 1, que foi excluída. Foram extraídas **179 unidades** (45 títulos internos, 101 parágrafos e 33 itens de lista), com **11.359 palavras** e 85.475 caracteres, das páginas 1 a 28. O corpo (`Body`) tem 151 unidades e 10.112 palavras. Os quatro quadros (`Box`) têm 28 unidades e 1.247 palavras. O nome do JSON foi indicado pelo pesquisador.

## 2. O que foi incluído

- **Título** "A New Generation of Artificial Intelligence Development Plan" (p. 1) em `document.title`. Não há subtítulo (`subtitle = null`).
- **Parágrafo de abertura** do plano (p. 1, `path = []`), que expõe a finalidade do plano.
- **Partes I a VI** (p. 1–28, `Body`), com a hierarquia do original:
  - nível 1: algarismos romanos (I a VI);
  - nível 2: letras, de (A) a (F);
  - nível 3: os itens 1. a 4. das partes III(A), III(B) e III(C).
- **Metas da parte II(C):** os três *steps* (2020, 2025 e 2030) ficaram como parágrafos, e os 9 objetivos marcados com travessão como `list_item` (`number = "-"`).
- **Rótulos corridos** no início dos parágrafos (por exemplo, "Leadership of technology.", "Smart robots." e "Wisdom court.") ficaram dentro do parágrafo. Nesta tradução eles não têm destaque tipográfico. Nas *Opinions* de 2025 (`IA_Plus_2025`), ao contrário, os títulos corridos vêm em negrito e foram registrados como `heading`.
- **Quatro quadros** (`Box`): Box 1 *Basic Theory* (p. 9–10; 8 itens), Box 2 *Key Common Technology* (p. 11–12; 8 itens), Box 3 *Basic Support Platform* (p. 13; 5 itens) e Box 4 *Intelligent infrastructure* (p. 22; 3 itens). O título de cada quadro é um `heading` um nível abaixo da seção em que o quadro está, e os itens numerados são `list_item`. Os quadros entram porque detalham as tarefas do plano e não copiam o corpo literalmente. O Box 3, por exemplo, traz o centro de supercomputação de IA e a plataforma de segurança para usinas nucleares, que não aparecem no corpo.
- **Repetições do próprio original** foram mantidas: "incremental incremental" (p. 10), "acquisition and acquisition" (p. 11) e "to to" (p. 15).

## 3. O que foi excluído e por quê

- **Notice de publicação** (p. 1): é o ofício que publica o plano, e não o plano. Saíram:
  - o título do ato, "Notice of the State Council Issuing the New Generation of Artificial Intelligence Development Plan", com o marcador da nota 1;
  - o número do documento, "State Council Document [2017] No. 35";
  - os destinatários, "To all people’s governments of provinces, … institutions:" (24 palavras);
  - a frase de encaminhamento, "The "next generation of artificial intelligence development plan" is hereby issued to you, please carefully implement." (16 palavras);
  - a assinatura e a data, "State Council / July 8, 2017". A data foi para `document.date`.
- **1 nota de rodapé** (p. 1): os créditos dos tradutores.
- **Cabeçalho da FLIA** "The Foundation for Law and International Affairs", repetido nas 28 páginas, e a **numeração de página**.
- O documento não tem tabelas, figuras, sumário, lista de siglas, referências nem anexos.

## 4. Normalizações aplicadas

- **Quebras de linha internas** foram removidas em todas as unidades com mais de uma linha.
- **Espaços múltiplos** foram reduzidos a um. Exemplos: "theories and  technologies" (p. 1), "III.  Key Tasks" (p. 7) e os espaços duplos depois do ponto, frequentes nas p. 14–28.
- **Hífens originais restaurados (27 casos).** O documento não tem hifenização automática: as linhas são justificadas com espaços esticados, e nenhuma palavra simples aparece partida. A camada de texto, porém, apagou o hífen dos compostos partidos em fim de linha. Exemplos: *coprocessing* → *co-processing* (p. 1), *worldleading* → *world-leading* (p. 5), *humancomputer* → *human-computer* (p. 10 e 19), *decisionmaking* → *decision-making* (p. 20 e 23), *BeijingTianjin-Hebei* → *Beijing-Tianjin-Hebei* (p. 20), *command-anddecision* → *command-and-decision* (p. 21) e *forwardlooking* → *forward-looking* (p. 27).
- **Ponto final isolado** numa linha própria, ao fim do último objetivo do terceiro *step* (p. 6): foi unido à palavra anterior ("…of artificial intelligence.").
- Os espaços antes de ponto ou vírgula que estão no original foram mantidos. Por exemplo, "artificial intelligence ." no título de III(A) e "support" , we shall" (p. 6).

## 5. Pontos que podem precisar de revisão

- **Troca de terminologia na tradução, importante para as contagens.** Da abertura até III(A).4 (unidades 1–88, p. 1–14), o texto diz sempre "artificial intelligence" (161 ocorrências). A partir de III(B) (unidades 90–179, p. 14–28), diz sempre "AI" (178 ocorrências). A mesma troca acontece com "R & D" (4 ocorrências, p. 4–10), que passa a "R&D" (9, p. 17–26), e, em grande parte, com "large data" (8, sendo 7 nas p. 1–13), que passa a "big data" (9, p. 17–23). O texto ficou literal. Sem agrupar essas variantes na análise, porém, a frequência do termo central se divide entre "artificial"/"intelligence" e "AI", e "R & D" vira dois tokens soltos.
- **Quadros (1.247 palavras).** Os Boxes 1 e 2 retomam, com redação parecida, os temas das seções III(A).1 e III(A).2. O item 2 do Box 2, por exemplo, é quase igual ao parágrafo "Cross-media analysis reasoning technology". Isso reforça termos como *intelligence*, *theory* e *technology*. Para analisar só o corpo, basta filtrar `category = "Box"`, sem nova extração.
- **Artefatos da tradução mantidos:** "This paper studies" (3 vezes, nos Boxes 1 e 2) e grafias como *accumulatedby*, *violateng*, *systeic*, *techologies*, *reaising*, *perceptiblity*, *dat-driven*, "s supported" e "step:by".
- **Notice excluído:** os destinatários e a frase de encaminhamento (40 palavras) podem ser incluídos por comando do pesquisador.
- **`period = null`:** o plano fixa metas para 2020, 2025 e 2030, mas não declara um período de vigência.
- **Arquivo-fonte fora da pasta:** por isso `source_sha256 = null`. Recomenda-se gravar o PDF nesta pasta para que a extração possa ser reproduzida.
