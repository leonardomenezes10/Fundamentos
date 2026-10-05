# Relatório de extração — Apply AI Strategy

**Arquivo-fonte:** Apply AI Strategy.pdf (20 páginas; anexado à conversa, não gravado na pasta) · **JSON:** `Apply_AI_2025.json` (nome dado pelo pesquisador) · **Data:** 2026-10-05

## 1. Resumo

Extração inicial da Comunicação da Comissão Europeia COM(2025) 723 final (Bruxelas, 8.10.2025). Foram extraídas 137 unidades (20 títulos internos, 78 parágrafos e 39 itens de lista), com 7.608 palavras, das páginas 2 a 20. Todas as unidades são `Body`: o documento não tem apresentação, sumário executivo separado, quadros nem anexos no arquivo.

## 2. O que foi incluído

- **Título** "Apply AI Strategy" em `document.title`. O documento não tem subtítulo (`subtitle = null`): a linha "COMMUNICATION FROM THE COMMISSION TO THE EUROPEAN PARLIAMENT AND THE COUNCIL" é a designação do ato e dos destinatários, e não um complemento do título.
- **Seções 1 a 5** (p. 2–20), com as subseções 2.1–2.11 e 3.1–3.4. Os títulos têm `level` 1 ou 2, e a numeração original ("1.", "2.1.", "2.10.") fica em `number`.
- **Introdução** (p. 2–3; 498 palavras), incluindo a lista das três partes da Estratégia. Ela é a abertura numerada da própria Comunicação, e não um sumário executivo à parte.
- **Listas de ações** (39 itens, marcador "•"), em que a Comissão anuncia o que fará em cada setor e em cada desafio transversal.
- **Frases que abrem as listas** ("To support the AI first policy in the healthcare sector, the Commission will:" e variantes; 16 frases, 227 palavras), registradas como parágrafos. Ficaram porque são frases do texto, que os itens completam (os itens começam com verbo em minúscula: "establish…", "launch…"), e não rótulos de layout. Ver a seção 5.
- **Segundo parágrafo do item "Frontier AI Initiative"** (p. 17, "As part of this initiative…"), registrado como parágrafo próprio logo após o item, sem fundir os dois.
- **Parágrafos finais da seção 4** sobre a dimensão internacional (p. 20). Eles não têm subtítulo e ficam no `path` da seção 4.
- As remissões "(Annex 1)" (p. 3) e "(Annex 2)" (p. 13) foram mantidas, porque fazem parte da frase.

## 3. O que foi excluído e por quê

- **Capa (p. 1):** logotipo, "EUROPEAN COMMISSION", local e data, referência "COM(2025) 723 final", designação do ato e marcas "EN". A data e o emissor foram para os metadados.
- **94 notas de rodapé** (texto e marcadores no corpo), por determinação do pesquisador. Algumas têm conteúdo substantivo: n. 10 (programas que financiam o EUR 1 bilhão: Horizon Europe, Digital Europe, EU4Health e Creative Europe), n. 26 (Implementation Roadmap for AI in CFSP/CSDP), n. 49 (parágrafo inteiro sobre IA no turismo), n. 51 (direitos autorais e Code of Practice), n. 52 (anúncio de uma estratégia de IA para os setores culturais e criativos), n. 62 (chamada GenAI4EU), n. 63 (Erasmus+ e IA na educação), n. 79 (definições de *fine-tuning* e *distillation*), n. 89 (metodologia com a OECD para medir investimentos em IA) e n. 91 (Global Dialogue on AI Governance e International Independent Scientific Panel on AI).
- **1 figura (p. 19):** diagrama AI Board / Apply AI Alliance / AI Observatory, com os textos internos.
- **Numeração de página.**

O arquivo não tem tabelas, sumário, lista de siglas nem referências.

## 4. Normalizações aplicadas

- **Junção das linhas** internas de cada parágrafo, em todas as unidades. **Redução de espaços duplos** do original, em 3 casos: "Strategy.  This" (p. 3), "will  improve" (p. 13) e "EU.  Particular" (p. 20).
- **Remoção dos 94 marcadores de nota.** Em 4 casos foi preciso recompor o espaço que a camada de texto havia colado: `consultation5and` virou `consultation and`, `discussions6over` virou `discussions over`, `evidence9and` virou `evidence and` e `SMEs2- the` virou `SMEs - the`. Em 1 caso foi retirado o espaço solto antes do ponto: `Alliance 32.` virou `Alliance.`.
- **Restauração do hífen original em 5 compostos partidos na quebra de linha**, que a camada de texto havia apagado: `post-deployment` (p. 4), `environment-AI` (p. 10), `user-engagement` (p. 11), `high-quality` (p. 12) e `innovation-friendly` (p. 18).

## 5. Pontos que podem precisar de revisão

- **Arquivo-fonte fora da pasta.** O PDF só foi anexado à conversa, por isso `source_sha256 = null`. Recomenda-se gravá-lo nesta pasta para que a extração possa ser reproduzida.
- **Frases que abrem as listas de ações (16 frases, 227 palavras).** A fórmula "To support the AI first policy in the … sector, the Commission will:" se repete no próprio plano. Essas frases concentram 7 das 12 ocorrências de "AI first" e 16 das 46 de "Commission". Foram mantidas porque são texto do emissor. Para analisar sem elas, basta filtrar os parágrafos curtos que terminam em "will:", sem nova extração.
- **Anexos ausentes.** O texto remete ao "Annex 1" (os 17 diálogos setoriais, p. 3) e ao "Annex 2" (as políticas internas de IA da Comissão, p. 13), mas o arquivo termina na p. 20, com a Conclusão.
- **Variações e grafias do original, mantidas sem correção:** "Resource of AI Science in Europe" (p. 3) e "Resource for AI Science in Europe" (p. 17) para a mesma sigla RAISE; "European Connected and Autonomous Alliance" (p. 8) ao lado de "European Connected and Autonomous Vehicle Alliance"; "objectives.." (p. 6); "deployment European AI-enabled" (p. 7, sem "of"); item terminado em vírgula, "digital environments," (p. 8); "a Agri-food" (p. 11); "candidate counties" (p. 20). Se a contagem desses termos importar, convém conferi-los.
