# Relatório de extração — America’s AI Action Plan

**Arquivo-fonte:** `Americas-AI-Action-Plan (1).pdf` (28 páginas; anexado à conversa, não gravado na pasta) · **JSON:** `EUA_2025_extracao.json` · **Data:** 2026-10-04

## 1. Resumo

Extração do texto essencial do plano dos Estados Unidos (*Winning the Race — America’s AI Action Plan*, The White House, julho de 2025), cobrindo as p. 4–26 do arquivo (p. 1–23 da numeração impressa). O JSON reúne **183 unidades**: 34 títulos internos, 47 parágrafos e 102 itens de lista, num total de **8.204 palavras** e 56.281 caracteres. Todas as unidades têm `category = "Body"`. Distribuição por parte: Introduction, 11 unidades e 637 palavras; Pilar I, 92 e 4.011; Pilar II, 49 e 2.198; Pilar III, 31 e 1.358.

A conciliação foi verificada por script: a camada de texto do PDF foi transcrita à parte, recebeu as normalizações da seção 4 deste relatório e teve os elementos excluídos retirados. O resultado é **idêntico, caractere a caractere**, à concatenação das 183 unidades. A página de início de cada unidade também foi conferida.

## 2. O que foi incluído

- **Metadados:** título `America’s AI Action Plan` e subtítulo `Winning the Race` (capa). O título aparece em caixa alta na capa, mas foi registrado na grafia que o próprio plano usa no texto (p. 4). Data `July 2025` e emissor `The White House`, ambos da capa. `period = null`, porque o documento não fixa vigência.
- **Introduction** (p. 4–5): apresenta os três pilares e os três princípios transversais. Faz parte do plano: consta do sumário, na p. 1 impressa.
- **Pilar I** (p. 6–16, 15 seções), **Pilar II** (p. 17–22, 8 seções) e **Pilar III** (p. 23–26, 7 seções): títulos dos pilares, títulos das 30 seções, parágrafos introdutórios e todos os itens das listas de ações.
- **Hierarquia:** a Introduction e os pilares são nível 1; as seções são nível 2. Os itens de lista levam `number = "•"`, como no original.

## 3. O que foi excluído e por quê

| Elemento | Local | Motivo |
|---|---|---|
| Capa | p. 1 | Moldura editorial. Título, subtítulo, data e emissor foram para os metadados |
| Epígrafe: citação de Donald J. Trump, com atribuição | p. 2 | Epígrafe (86 palavras), e não texto do plano |
| Sumário | p. 3 | Repete os títulos do corpo |
| Bloco de assinaturas da Introduction (Kratsios, Sacks, Rubio e cargos) | p. 5 | Créditos (31 palavras). Os cargos repetiriam termos como *AI*, *Science and Technology* e *National Security* |
| 30 notas de rodapé e os 20 grupos de marcadores no corpo (ex.: `Plan.1`, `Future.”7, 8`, `Accelerator.21, 22, 23, 24`) | p. 4–22 | Exclusão determinada pelo pesquisador. As URLs do documento estão todas nas notas e saíram com elas |
| Rótulo *Recommended Policy Actions* | 30 ocorrências, uma por seção | Rótulo estrutural repetido. Fica só no `path` dos itens de lista |
| Item repetido em *Invest in Biosecurity*: “Build, maintain, and update as necessary national security-related AI evaluations…” | p. 26 | Repete, palavra por palavra, o último item da seção anterior (p. 25), que foi mantido (23 palavras) |
| Cabeçalho corrido “AMERICA’S AI ACTION PLAN” e numeração de página | p. 2–28 | Artefato de diagramação |
| “This page intentionally left blank.” e contracapa | p. 27–28 | Artefato de diagramação e moldura editorial |

O documento não tem tabelas nem figuras no corpo. As únicas imagens são o selo, na capa, e o desenho da Casa Branca, na contracapa.

## 4. Normalizações aplicadas

- **Quebras de linha e de página:** removidas dentro das unidades, inclusive em 10 unidades que atravessam a página (ex.: p. 4→5, “And the / breakthroughs”). Em dois casos a quebra vinha logo depois de um travessão, e a junção foi feita sem espaço, como em todo o documento: “infrastructure—factories” (p. 17) e “stack—hardware” (p. 23).
- **Hífen original restaurado (10 casos):** a camada de texto do PDF apagou o hífen de fim de linha em palavras compostas que a página renderizada mostra hifenizadas: *Open-source* (p. 7), *large-scale* (p. 7), *self-driving* (p. 10), *use-cases* (p. 12), *deepfake-related* (p. 16), *industry-driven* (p. 20), *best-practices* (p. 22), *like-minded* (p. 23), *sub-systems* (p. 24) e *multi-tiered* (p. 26). O documento não usa hifenização automática: todas as quebras com hífen caem em palavras compostas, e seis delas (*open-source*, *large-scale*, *use-cases*, *industry-driven*, *best-practices* e *sub-systems*) aparecem hifenizadas também em outro ponto do texto.
- **Espaço entre palavras restaurado (7 casos):** artefato do texto justificado na camada de texto. Os casos foram *duringhis* → *during his* (p. 4), *Federalfunding* → *Federal funding* (p. 6), *DOC,to* → *DOC, to* (p. 8), *Administrationmust* → *Administration must* (p. 16), *Order14306* → *Order 14306* (p. 22), *Influencein* → *Influence in* (p. 23, título que o sumário grafa com espaço) e *DOC,the* → *DOC, the* (p. 23).
- **Nada foi corrigido no original.** Ficaram como estão “the U.S to develop” (p. 25), “identify surface scalable” (p. 10), “a researchers’ prior funded efforts” (p. 11), “the Department of Interior” (p. 12), “best practices” (p. 13) ao lado de “best-practices” (p. 22) e “whole-genome” ao lado de “whole genome” (p. 12).

## 5. Pontos que podem precisar de revisão

1. **Item repetido (p. 25 e p. 26):** ficou só na p. 25, onde corresponde ao tema da seção (avaliação de riscos à segurança nacional). Com isso, a seção *Invest in Biosecurity* passa a ter 2 ações em vez das 3 publicadas. Se o pesquisador quiser reproduzir as listas exatamente como o documento as publica, basta reincluir o item (+23 palavras).
2. **Epígrafe (p. 2):** excluída, embora traga termos centrais para a análise (*artificial intelligence*, *national security imperative*, *global technological dominance*). Incluí-la acrescentaria 86 palavras.
3. **Introduction assinada (p. 4–5):** classificada como `Body`, porque o documento a apresenta como sua introdução e ela expõe os pilares e os princípios. Por ser assinada por três autoridades, tem também caráter de apresentação. Se o pesquisador quiser tratá-la à parte, as 11 unidades (637 palavras) têm `path = ["Introduction"]`.
4. **Arquivo-fonte fora da pasta:** o PDF veio só como anexo, por isso `source_sha256 = null`, e o nome registrado traz o sufixo de download “(1)”. Recomenda-se gravar o PDF em `Planos Nacionais de IA/`, para que a extração possa ser reproduzida, e então atualizar `source_file` e `source_sha256`.
