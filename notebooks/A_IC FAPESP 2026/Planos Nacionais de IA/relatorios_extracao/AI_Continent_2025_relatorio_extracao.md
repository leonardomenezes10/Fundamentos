# Relatório de extração — AI Continent Action Plan

**Arquivo-fonte:** AI CONTINENT ACTION PLAN.pdf (25 páginas; anexado à conversa, não gravado na pasta) · **JSON:** `AI_Continent_2025.json` · **Data:** 2026-10-04

## 1. Resumo

Em 2026-10-05, por comando do pesquisador, o JSON foi renomeado de `UE_2025_extracao.json` para `AI_Continent_2025.json`, e este relatório acompanhou a mudança. O conteúdo não foi alterado.

Extração inicial da Comunicação da Comissão Europeia COM(2025) 165 final (Bruxelas, 9.4.2025). Foram extraídas 146 unidades (18 títulos internos, 87 parágrafos e 41 itens de lista), com 9.090 palavras, das páginas 2 a 25. O corpo (`Body`) tem 102 unidades e 8.046 palavras. Os quadros (`Box`) têm 44 unidades e 1.044 palavras.

## 2. O que foi incluído

- **Título** "AI Continent Action Plan" em `document.title`. O documento não tem subtítulo (`subtitle = null`): a linha "COMMUNICATION FROM THE COMMISSION TO THE EUROPEAN PARLIAMENT, …" da capa é a designação do ato e dos destinatários, e não um complemento do título.
- **Introdução sem número** (p. 2–4; 13 parágrafos; 1.117 palavras), incluindo os cinco domínios ("First, …" a "Fifth, …"), como `Body`. Não foi tratada como sumário executivo porque é a abertura da própria Comunicação e traz conteúdo que não reaparece adiante (por exemplo, o InvestAI de EUR 200 bilhões).
- **Seções 1 a 6**, com as subseções 1.1–1.3, 3.1–3.3 e 4.1–4.2 (p. 5–25, `Body`). Os títulos têm `level` 1 ou 2, e a numeração fica em `number`. As listas do corpo (p. 9 e p. 19) estão como `list_item`.
- **Sete quadros "Key Commission actions"**, ao fim de 1.1, 1.2, 1.3, 2, 3.3, 4.2 e 5 (36 itens; 668 palavras; `Box`). Entram porque são as ações operativas do plano, com prazos, e não cópias literais do corpo.
- **Quadro de casos dos European Digital Innovation Hubs** (p. 16–17): 4 títulos (`level` 3) e 4 parágrafos (376 palavras; `Box`).
- A frase "the AI Continent will focus on measures to enlarge the EU’s pool of AI specialists…" aparece duas vezes no início da seção 4, no próprio original. Foi mantida nas duas posições.

## 3. O que foi excluído e por quê

- **Capa (p. 1):** logotipo, "EUROPEAN COMMISSION", local e data, referência "COM(2025) 165 final", designação do ato e marcas "EN". A data e o emissor foram para os metadados.
- **Título repetido** no topo da p. 2, que já está em `document.title`.
- **54 notas de rodapé** (texto e marcadores no corpo), por determinação do pesquisador. Algumas têm conteúdo substantivo: n. 14 (iniciativa DARE, EUR 240 milhões), n. 24 (estratégia de IA para os setores culturais e criativos), n. 44 (dados do Cedefop) e n. 54 (calendário de aplicação do AI Act).
- **1 tabela (p. 6):** setores-chave × países das AI Factories.
- **3 figuras**, com os textos internos: pentágono dos cinco domínios (p. 4), mapa das AI Factories (p. 7) e pirâmide Gigafactories/Factories/EDIH (p. 15).
- **Rótulo repetido dos quadros** ("Key Commission / EuroHPC Actions:", "Key Commission / EuroHPC actions:", "Key Commission actions:"; 7 ocorrências): não virou unidade e ficou só no `path` dos itens.
- **Numeração de página.**

O documento não tem sumário, lista de siglas, referências nem anexos (sobre o Annex I, ver a seção 5).

## 4. Normalizações aplicadas

- **Junção das linhas** internas de cada parágrafo e **redução de espaços**, em todas as unidades.
- **Remoção dos 54 marcadores de nota**, recompondo o espaço que a camada de texto havia colado. Por exemplo, `Paris4in February` virou `Paris in February`, e `15 Member States6and two` virou `15 Member States and two`.
- **Restauração do hífen original em 3 compostos partidos na quebra de linha**, que a camada de texto havia apagado: `world-class` (p. 17–18), `hands-on` (p. 21) e `public-sector` (p. 22). Nas demais hifenizações de diagramação, a camada de texto já trazia as palavras unidas.

## 5. Pontos que podem precisar de revisão

- **Arquivo-fonte fora da pasta.** O PDF só foi anexado à conversa, por isso `source_sha256 = null`. Recomenda-se gravá-lo nesta pasta para que a extração possa ser reproduzida.
- **Quadros "Key Commission actions" (668 palavras).** Eles retomam, com prazos, ações já descritas no corpo (AI Factories, Apply AI Strategy, Data Union Strategy etc.), o que reforça a frequência desses termos. Para analisar o corpo sem essa retomada, basta filtrar as unidades `Box` com "Key Commission" no `path`, sem nova extração.
- **Tabela da p. 6.** É o único lugar em que o plano mostra a especialização setorial de cada AI Factory por país, e o parágrafo anterior termina em "as follows:". Ficou excluída conforme a regra; só entra por comando do pesquisador.
- **Annex I ausente.** O texto (p. 6) remete ao "Annex I", com o resumo das 13 AI Factories, mas o arquivo termina na p. 25 sem anexo.
- **Grafias do original mantidas sem correção:** `ofscientists` (p. 2), `fragmenation` (p. 8), `markets,–public` (p. 10, com travessão solto), `furthersupport`, `BlueCard`, `‘MSCA Choose Europe’scheme` e `insitution` (p. 20), e `positionEurope` (p. 25). Alguns desses casos podem ser espaços perdidos na camada de texto, e não erros do original. Se a contagem desses termos importar, convém conferi-los no PDF.
