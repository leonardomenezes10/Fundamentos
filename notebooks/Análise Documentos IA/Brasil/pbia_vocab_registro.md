# Registro de Análise de Vocabulário — PBIA (Brasil)

Registro persistente exigido pela **Skill 02_Análise_Vocab_A**, associado ao documento `pbia.json` (campo `texto_completo`). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Documento de origem:** `pbia.json` (`titulo`: "AI for the Good of All – Brazilian Artificial Intelligence Plan"; `pais_ou_bloco`: "Brasil")
- **Idioma identificado em `texto_completo`:** inglês (o PDF de origem — publicação oficial do MCTI/CGEE — está publicado nessa língua; os critérios de stopwords e normalização abaixo são, portanto, do inglês, não do português).
- **Última atualização deste registro:** 2026-08-05

## 1. Termos removidos (exclusão) e justificativa

### 1.1. Palavras funcionais do inglês (stopwords)
Removidas por não carregarem conteúdo temático próprio (critério linguístico, não narrativo), agrupadas por classe gramatical:

- **Artigos:** a, an, the
- **Preposições:** of, in, to, for, with, on, by, as, at, from, into, about, through, during, before, after, above, below, between, under, over, without, within, among, throughout, towards, toward, upon, across, per, via, despite, unlike, regarding, off, out, up, down, besides
- **Conjunções:** and, or, but, nor, so, yet, if, because, while, although, though, whether, since, unless, until, than
- **Pronomes/determinantes:** it, its, this, that, these, those, we, our, ours, they, their, theirs, which, who, whom, whose, i, you, he, she, him, her, us, them, his, hers, itself, themselves, ourselves, yourself, yourselves, himself, herself, one, ones, such, other, others, any, some, each, all, both, either, neither, no, none, own, same
- **Verbos auxiliares/modais:** is, are, was, were, be, been, being, am, has, have, had, do, does, did, will, would, shall, should, can, could, may, might, must, ought
- **Conectores/quantificadores genéricos:** more, most, much, many, few, several, various, not, also, only, just, still, even, well, thus, therefore, however, moreover, furthermore, given, whereas

### 1.2. Resíduos não semânticos de formatação (marcadores de lista)
O documento utiliza marcadores alfabéticos (A), B), C), D)) para os subitens de cada eixo ("What will we do?") e numerais romanos (I), II), III), IV), V)) para os cinco pilares do Capítulo 2. Ao tokenizar o texto, esses marcadores geram tokens isolados sem valor semântico próprio (ex.: "d" de "D) AI Research and Development Program"; "iii" de "III) Founded on..."). Removidos: **b, c, d, ii, iii, iv, v** (as letras "a" e "i" já estão cobertas pela lista de stopwords, como artigo e pronome, respectivamente).

Também foram removidos, pela mesma razão, **tokens isolados de um único caractere** remanescentes de siglas quebradas por símbolos não alfabéticos que a expressão regular de tokenização não captura — em especial "r" e "d", resíduos da grafia "R$" (valores em reais, ex.: "R$ 23 billion") e de marcadores de lista.

### 1.3. Termo genérico de baixo valor analítico no contexto desta demanda
- **"expected"** — 84 ocorrências no total, das quais **81 (96,4%)** correspondem estritamente ao rótulo fixo de campo "Expected impact(s):", repetido mecanicamente em cada uma das 81 entradas dos Anexos 1 e 2 (27 Impact Actions + 54 Actions). As 3 ocorrências restantes, em prosa corrida, não justificam a permanência do termo como vocabulário substantivo do plano — sua altíssima frequência decorre da estrutura de listagem do documento, não de ênfase conceitual. Removido por critério metodológico (evitar artefato de contagem gerado pelo template), nunca por favorecer ou contrariar alguma leitura do conteúdo.

**Termos avaliados e mantidos, apesar de também aparecerem como rótulo de campo nos Anexos 1-2** (transparência quanto à decisão inversa, para não haver seleção arbitrária): **"challenge(s)"** (133 ocorrências totais; 82 são o rótulo "Challenge(s):", mas 51 ocorrem organicamente em prosa corrida — ex.: "the Country's challenges", "windows of opportunity... to face this challenge"); **"impact(s)"** (148 totais; 81 são o rótulo "Expected impact(s):", mas 67 ocorrem organicamente — ex.: "transformative potential", "economic impact", "impacts on society"); e **"action(s)"** (152 totais; 81 são os rótulos "Impact Action N:"/"Action N:", mas 71 ocorrem organicamente, sendo inclusive categoria estruturante do próprio Plano — "immediate impact actions", "structuring actions"). Esses três termos foram **mantidos** no vocabulário porque designam categorias conceituais reais e centrais do PBIA, não apenas rótulos de template — ao contrário de "expected", que não carrega conteúdo temático autônomo. Essa inflação parcial por template é registrada aqui para leitura crítica do gráfico.

## 2. Normalização/agrupamento de variantes (sem exclusão de conteúdo)

### 2.1. Siglas e formas por extenso (mesmo referente)
Tratadas como uma única unidade analítica antes da tokenização em palavras isoladas (para não fragmentar a expressão composta), somando as ocorrências da sigla e da forma por extenso:

| Termo representativo | Formas agrupadas | Ocorrências |
|---|---|---|
| Artificial Intelligence (AI) | "Artificial Intelligence" + "AI" (sigla isolada) | 627 |
| Research & Development (R&D) | "Research and Development" + "R&D" | 27 |
| Unified Health System (SUS) | "Unified Health System" + "SUS" | 18 |
| National Data Infrastructure (IND) | "National Data Infrastructure" + "IND" | 8 |
| Large Language Models (LLM) | "Large Language Model(s)" + "LLM(s)" | 7 |
| Sustainable Development Goals (SDGs) | "Sustainable Development Goal(s)" + "SDG(s)" | 7 |

### 2.2. Expressões técnicas compostas (tratadas como unidade única, não fragmentadas)
Bigramas técnicos do domínio de políticas de IA, extraídos como unidade antes da contagem por palavra isolada — sem forma abreviada equivalente no texto:

Data Center(s) (16); Public Service(s) (27); Public Sector (19); Private Sector (8); Value Chain (10); Federal Government (9); Public Administration (7); Clean Energy (7); Data Infrastructure — uso genérico, distinto do IND (4); Machine Learning (6); Digital Government (3); Energy Matrix (2).

*Critério de não fusão:* "National Data Infrastructure (IND)" e "Data Infrastructure" (genérico) foram mantidos como **rótulos distintos**, apesar da sobreposição textual, porque designam referentes diferentes — o primeiro é o programa/estrutura nomeada no Eixo 3 (IND), o segundo é o conceito genérico de infraestrutura de dados mencionado no Capítulo 1 e na Introdução.

### 2.3. Variação morfológica (singular/plural, mesmo lema)
Unificados sob um rótulo representativo comum (contagens somadas): action(s), challenge(s), impact(s), solution(s), resource(s), investment(s), model(s), benefit(s), professional(s), network(s), initiative(s), institution(s), researcher(s), capacity/capacities, company/companies, citizen(s), agency/agencies, axis/axes, center(s), innovation(s), qualification(s), system(s), technology/technologies, sector(s), process(es), service(s), government(s), policy/policies, right(s), risk(s), servant(s).

Também unificado: **"Brazil's" → "Brazil"** (mesma forma de caixa/variação gramatical — possessivo do mesmo substantivo próprio).

### 2.4. Casos avaliados e **não** agrupados (referentes distintos, apesar da semelhança gráfica)
- **"country" (singular) vs. "countries" (plural):** no PBIA, "the Country" (singular, maiúscula estilística) é usado sistematicamente como sinônimo do próprio Brasil (ex.: "the Country's challenges", "the Country has also made great progress"), enquanto "countries" (plural) refere-se a outras nações/países em geral (ex.: "developing countries", "leading countries"). Referentes diferentes — fusão evitada deliberadamente.
- **"intelligence" (2 ocorrências residuais fora de "Artificial Intelligence"):** uma delas cita o título da obra de Turing, "Computing Machinery and Intelligence" (nome próprio de um artigo, não o conceito de IA); a outra refere-se a "the main intelligence platform" (uso no sentido de plataforma de inteligência/monitoramento, não de inteligência artificial). Mantidas fora do agrupamento "Artificial Intelligence (AI)" por design do próprio método de extração por bigrama adjacente, que só funde os termos quando aparecem imediatamente adjacentes um ao outro.
- **"value" vs. "values":** todas as 10 ocorrências de "value" (singular) fazem parte da expressão composta "value chain" (já tratada em 2.2); "values" (plural) refere-se a um conceito distinto (valores éticos/democráticos — ex.: "human values", "democratic values"). Não fundidos.

## 3. Critério de corte

**Top 25 termos por frequência absoluta** (contagem de ocorrências em `texto_completo`, após as remoções da seção 1 e as normalizações da seção 2). Critério fixo, aplicado de forma consistente a toda a análise deste documento.

## 4. Histórico de atualizações

- **2026-08-05:** criação do registro; primeira análise de vocabulário do PBIA (gráfico de barras horizontais, Top 25 termos), executada dentro de `pbia.ipynb`.
