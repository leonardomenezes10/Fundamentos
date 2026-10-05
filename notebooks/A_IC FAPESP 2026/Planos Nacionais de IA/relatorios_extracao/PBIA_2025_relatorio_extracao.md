# Relatório de extração — AI for the Good of All: Brazilian Artificial Intelligence Plan

**Arquivo-fonte:** `ai-for-the-good-of-all-2025.pdf` (70 páginas), anexado à conversa · **JSON:** `PBIA_2025_extracao.json` · **Data:** 2026-10-04

> Relatório apenas informativo. Não é insumo nem instrução para as etapas seguintes.

## 1. Resumo

Foram extraídas **585 unidades** (153 títulos internos, 200 parágrafos e 232 itens de lista), com **16.594 palavras**, das páginas 11 a 62 do arquivo. Por categoria: `Foreword` (12 unidades, 566 palavras), `Body` (217 unidades, 10.720 palavras) e `Annex` (356 unidades, 5.308 palavras). O PDF foi fornecido só como anexo e não está gravado na pasta, por isso `source_sha256` é `null`. Para que a extração possa ser reproduzida, convém gravá-lo na pasta. A sigla `PBIA_2025` segue a data impressa no documento (*Brasília – DF, 2025*).

## 2. O que foi incluído

- **Título e subtítulo** (nos metadados): *AI for the Good of All* / *Brazilian Artificial Intelligence Plan*.
- **Presentation** (p. 11–12), como `Foreword`: é a mensagem da Ministra, que expõe a visão, o investimento e os objetivos do plano.
- **Introduction** (p. 13–15), **capítulos 1 a 4** (p. 17–39) e **Final Considerations** (p. 40), como `Body`.
- **Anexo 1**, com as 27 ações de impacto imediato (p. 41–47), e **Anexo 2**, com as 54 ações estruturantes (p. 49–62), como `Annex`. Os anexos entram porque o próprio plano diz que as suas ações estão detalhadas neles (seção 3.3).
- **Hierarquia (`level`):** 1 = partes e capítulos; 2 = seções x.y, pilares I)–V) e grupos dos anexos; 3 = subseções 3.4.x e eixos ou áreas dos anexos; 4 = cada ação dos anexos; 5 = programas A)–D) do capítulo 3; 6 = "Responsibilities:".

## 3. O que foi excluído e por quê

- **Moldura editorial:** capa, contracapa e páginas em branco (p. 1–2, 10, 16, 26, 48, 69–70); folha de rosto (p. 3); créditos, ficha catalográfica e ISBN (p. 4); composição do CCT, grupo de trabalho, equipes e instituições participantes (p. 5–8); sumário (p. 9); assinatura da Apresentação (p. 12).
- **Aparato de consulta:** lista de siglas (p. 63–65) e referências (p. 66–68).
- **Notas de rodapé, por determinação do pesquisador:** 8 notas, com o texto e o marcador. Algumas têm conteúdo substantivo: a nota 1 diz que os anexos serão atualizados; a 5 lista as seis missões da NIB; a 6 descreve as medidas do MDIC para *data centers*; a 8 traz o decreto do CIT Digital.
- **Tabela, por determinação do pesquisador:** *Table 1 – PBIA Investments* (p. 28), com a linha de fonte.
- **Figura:** *Figure 1*, a linha do tempo da IA (p. 18), com o texto interno, a legenda e a fonte. A remissão "(Figure 1)" continua no corpo.
- **Artefatos de página:** cabeçalhos com o título do plano e do capítulo, e números de página.
- **19 citações bibliográficas autor-data no corpo**, como "(OECD, 2024)", "(Cetic.br, 2023b)" e "(ABES, 2024; Cetic.br, 2023c)". Elas apontam para as referências excluídas e equivalem aos marcadores de nota. Saiu só o parêntese, e o resto da frase ficou intacto. Ficou "(ICT Electronic Government, 2023)" (p. 22), porque nomeia a pesquisa citada na frase.
- **Rótulos estruturais repetidos**, que deixaram de ser unidades e ficaram **só no `path`**:
  - "Where are we?", "Where do we want to get to(?)" e "What will we do(?)": repetidos nos 5 eixos (15 ocorrências).
  - "Challenge(s):" e "Expected impact(s):": abrem os dois itens » de cada uma das 81 ações dos anexos (162 ocorrências). Mantidos no texto, acrescentariam cerca de 81 ocorrências de *challenge*, 81 de *expected* e 81 de *impact* que vêm do formulário do anexo, e não do discurso do plano. O `text` do item começa logo depois do rótulo.

## 4. Normalizações aplicadas

- Quebras de linha internas removidas em todo o texto, e 7 espaços duplos reduzidos a um (ex.: "AI holds  transformative" → "AI holds transformative").
- 1 hifenização de diagramação desfeita: "Process-ing" → "Processing" (Action 2).
- 5 hífens **originais** de palavras compostas mantidos onde caíam na quebra de linha (a camada de texto do PDF os havia perdido): *general-purpose* (p. 17), *micro-level* (p. 22), *well-being* (p. 30), *public-private* (p. 39) e *state-owned* (p. 58).
- 1 glifo corrompido: "J" → "→", nos 3 subitens da p. 31 (campo `number`).

## 5. Pontos que podem precisar de revisão

1. **Rótulos *Challenge* / *Expected impacts* fora do texto.** É a decisão que mais afeta as contagens. Para revertê-la, basta recolocar no início do `text` o último elemento do `path` desses itens.
2. **Table 1 excluída, embora tenha conteúdo central.** O texto da seção 3.2 traz os percentuais por eixo, mas não os valores em BRL de cada eixo (o total de R$ 23,03 bilhões está no texto).
3. **19 citações autor-data retiradas** por decisão do agente, por analogia com as notas de rodapé.
4. **Títulos com rótulo numerado ficam inteiros**, como manda a skill (§4.3): "Impact Action N:" (27) e "Action N:" (54). Isso soma 81 ocorrências de *action* e 27 de *impact*.
5. **Repetições do próprio plano foram mantidas**, porque são texto do emissor e não erro de leitura:
   - 11 títulos do capítulo 3 reaparecem idênticos no Anexo 2 (1 eixo e 10 programas).
   - "Health" e "Agriculture and livestock" aparecem duas vezes no Anexo 1.
   - Há textos de impacto esperado idênticos entre ações: Impact Actions 1 e 3; Actions 1, 2 e 3; Actions 5 e 6.
6. **Escolhas estruturais:**
   - Os pilares I)–V) do capítulo 2 são títulos internos (frases completas que abrem cada pilar).
   - *Final Considerations* ficou no nível 1. Não está no sumário, mas conclui o plano inteiro.
   - Erros do original foram mantidos sem correção: "Table 2 details" (a tabela é a Table 1), "(3)" repetido, "see section 4.4." e "several factors Among".
7. **Metadados:**
   - `period` = "2024 to 2028" é o período de investimentos declarado na seção 3.2; o documento não define outra vigência.
   - `issuer` = MCTI e CGEE, conforme a referência bibliográfica do próprio documento. O plano se apresenta como iniciativa do CCT, coordenada pelo MCTI.
