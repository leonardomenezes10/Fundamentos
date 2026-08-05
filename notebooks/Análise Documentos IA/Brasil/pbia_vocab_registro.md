# Registro de Análise de Vocabulário — PBIA (Brasil)

Registro persistente exigido pela **Skill 02_Análise_Vocab_A**, associado ao documento `pbia.json` (campo `texto_completo`). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Documento de origem:** `pbia.json` (`titulo`: "AI for the Good of All – Brazilian Artificial Intelligence Plan"; `pais_ou_bloco`: "Brasil")
- **Idioma identificado em `texto_completo`:** inglês (o PDF de origem — publicação oficial do MCTI/CGEE — está publicado nessa língua; os critérios de stopwords e normalização abaixo são, portanto, do inglês, não do português).
- **Última atualização deste registro:** 2026-08-05 — revisão metodológica determinada pelo usuário (auditoria de hífen, novos bigramas de desambiguação contextual, expansão da normalização morfológica e do corte para Top 50).

## 0. Correção metodológica aplicada nesta revisão

Diferentemente dos demais documentos deste projeto, a tokenização do PBIA **já preservava hífens como parte do token** desde a criação deste registro (`[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ'\-]*`) — não havia, portanto, o erro de "hífen como separador universal" corrigido nos demais documentos. Ainda assim, por determinação do usuário, esta revisão: (i) **auditou individualmente as 58 formas hifenizadas** do texto (Seção 1.4, nova); (ii) **descobriu e corrigiu duas polissemias genuínas não tratadas** — "power" (computacional vs. jurídico-institucional, "Federal Public Power") e "state"/"states" (subnacional genérico vs. "the State" como ente político abstrato vs. "United States" nome de país) — e uma polissemia menor em "generation" (título de eixo do Plano vs. geração de conteúdo por IA vs. sentido genérico); (iii) **expandiu a normalização morfológica**, incluindo pela primeira vez famílias de conjugações verbais (o registro original só normalizava substantivos); e (iv) **expandiu o corte de Top 25 para Top 50**.

### 1.4. Auditoria de compostos com hífen (58 formas identificadas)

Todas as 58 formas hifenizadas do texto foram avaliadas individualmente (Skill 02_Análise_Vocab_A, item 4) e **mantidas unidas** — nenhuma qualificou para separação em suas palavras componentes. Organizadas tematicamente:

| Categoria | Formas (frequência) |
|---|---|
| Bem-estar/qualidade | well-being (15), well-defined (3), well-cared (1) |
| Desempenho/escala | high-performance (14), large-scale (8), high-speed (3), ultra-high-performance (1) |
| Processo decisório | decision-making (7) |
| Excelência tecnológica | cutting-edge (6), ai-based (6) |
| Socioeconômico/propriedade | socio-economic (4), state-owned (4) |
| Porte/prazo | medium-sized (3), long-term (2), micro-level (1) |
| Humano-centrado | human-centered (3), human-produced (1), human-machine (1), people-oriented (1) |
| Eficiência/sustentabilidade | energy-efficient (3), low-environmental (1), low-carbon (1), self-sustenance (1) |
| Descritores "AI-X" | ai-focused (1), ai-related (1), ai-trained (1) |
| Público-privado/infraestrutura | public-private (2), pro-infra (2), inct-ai (1), besm-inpe (1), besm-oa (1), inct-mc (1), inct-ia (1) |
| Micro/empreendedorismo | micro-entrepreneurs (2), micro-entrepreneur (1) |
| Termos técnicos diversos | de-contingency (1), non-discriminatory (1), general-purpose (1), re-evaluation (1), non-existent (1), market-leading (1), data-driven (1), high-risk (1), technical-professional (1), high-cost (1), low-income (1), non-residents (1), uv-c (1), high-accuracy (1), in-person (1), multi-institutional (1), high-capacity (1), technical-scientific (1), ocean-atmosphere (1), co-operation (1) |
| Geração tecnológica | next-generation (1) — sentido tecnológico, distinto dos usos de "generation"/"Generation" tratados na Seção 2.4 |

## 1.5. Novos bigramas de desambiguação contextual

| Bigrama | Ocorrências | Justificativa |
|---|---|---|
| `"United States"` | 3 | Nome de país, referente distinto de "state(s)" subnacional (ver Seção 2.4) |
| `"the State"` (case-sensitive, "State" maiúsculo) | 2 | Sentido de ente político abstrato — "o Estado" (ex.: "collaboration between the State, academia..."), referente distinto do sentido subnacional genérico |
| `"computational power"` | 6 | Sentido computacional de "power" |
| `"Federal Public Power"` (case-sensitive) | 1 | Termo jurídico-institucional (tradução de "Poder Público Federal"), terceiro referente de "power", distinto de energia/computação |
| `"Generation of national"` (case-sensitive) | 2 | Título de eixo/categoria estruturante do Plano ("Generation of national capacities and qualifications", "Generation of national capabilities"), não vocabulário genérico solto |
| `"content generation"` | 1 | Sentido de geração de conteúdo por IA, distinto do sentido genérico de "geração/criação" |

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

**Cobertura ampliada nesta revisão (Top 50), substantivos (39 novos pares):** application(s), area(s), advantage(s), framework(s), database(s), decision(s), ecosystem(s), enterprise(s), environment(s), example(s), fund(s), goal(s), human(s), interest(s), job(s), leader(s), level(s), market(s), mission(s), nation(s), objective(s), partnership(s), plan(s), platform(s), population(s), problem(s), project(s), scenario(s), school(s), science(s), standard(s), student(s), supercomputer(s), tool(s), transformation(s), treatment(s), volume(s), context(s), characteristic(s), bias(es), business(es), cost(s), change(s), result(s), state(s) (subnacional/genérico, ver Seção 2.4).

**Novidade metodológica desta revisão — famílias verbais (22, antes inexistentes neste registro):** promote, increase, improve, support (verbo), ensure, strengthen, foster, establish, expand, create (verbo), develop (verbo), implement (verbo), include, identify, require, guarantee, monitor, integrate, propose, protect, provide (verbo), reduce, launch, offer. Cada uma mantida separada do substantivo derivacional correspondente quando existente (ex.: "develop"/"development"; "create"/"creation"; "implement"/"implementation"; "provide"/"providers" — este último já documentado na Seção 2.4), seguindo o mesmo critério de não fusão substantivo/verbo já aplicado em todos os demais documentos do projeto.

### 2.4. Casos avaliados e **não** agrupados (referentes distintos, apesar da semelhança gráfica)
- **"country" (singular) vs. "countries" (plural):** no PBIA, "the Country" (singular, maiúscula estilística) é usado sistematicamente como sinônimo do próprio Brasil (ex.: "the Country's challenges", "the Country has also made great progress"), enquanto "countries" (plural) refere-se a outras nações/países em geral (ex.: "developing countries", "leading countries"). Referentes diferentes — fusão evitada deliberadamente.
- **"intelligence" (2 ocorrências residuais fora de "Artificial Intelligence"):** uma delas cita o título da obra de Turing, "Computing Machinery and Intelligence" (nome próprio de um artigo, não o conceito de IA); a outra refere-se a "the main intelligence platform" (uso no sentido de plataforma de inteligência/monitoramento, não de inteligência artificial). Mantidas fora do agrupamento "Artificial Intelligence (AI)" por design do próprio método de extração por bigrama adjacente, que só funde os termos quando aparecem imediatamente adjacentes um ao outro.
- **"value" vs. "values":** todas as 10 ocorrências de "value" (singular) fazem parte da expressão composta "value chain" (já tratada em 2.2); "values" (plural) refere-se a um conceito distinto (valores éticos/democráticos — ex.: "human values", "democratic values"). Não fundidos.
- **"country" vs. "countries":** decisão herdada (ver acima) — reconfirmada nesta revisão.

### 2.5. Desambiguação contextual de termos polissêmicos/homônimos (nova, Skill 02_Análise_Vocab_A, item 5)

| Termo | Sentidos identificados (por concordância) | Decisão |
|---|---|---|
| power (7 ocorrências soltas antes do desdobramento) | 6 no sentido computacional ("computational power"); 1 no sentido jurídico-institucional ("Federal Public Power", tradução de "Poder Público Federal") | **Desdobrado** em `power (computacional)` (6) e `Poder Público Federal (termo jurídico-institucional)` (1) — ver Seção 1.5 |
| state (7) / states (4) | 5 ocorrências no sentido subnacional/genérico (estados federativos, ex.: "federal and state agencies"); 2 ocorrências de "the State" como ente político abstrato ("o Estado"); 3 ocorrências de "United States" (nome de país); 1 ocorrência de "states" genérico ("Federative Units (States)") | **Desdobrado** em `state(s) (subnacional/genérico)` (6), `the State (ente político/entidade abstrata)` (2) e `United States` (3) — ver Seção 1.5. Mesma lógica do par "state(s)"/"United States" já documentado no registro dos EUA deste projeto. |
| generation (5 ocorrências soltas, excluindo o composto hifenizado "next-generation") | 2 ocorrências como título de eixo do Plano ("Generation of national capacities and qualifications", "Generation of national capabilities"); 1 ocorrência no sentido de geração de conteúdo por IA ("content generation capabilities"); 2 ocorrências no sentido genérico de criação ("generation of new employment opportunities") | **Desdobrado** em `Generation of national capacities/capabilities (título de eixo do Plano)` (2) e `generation (geração de conteúdo por IA)` (1); a ocorrência genérica remanescente permanece como token solto "generation" — ver Seção 1.5 |

## 3. Critério de corte

**Top 50** termos por frequência absoluta (critério padrão da Skill 02_Análise_Vocab_A, item 6, adotado nesta revisão), com o **Top 25** mantido como recorte adicional dentro do mesmo Top 50. Frequência absoluta (não relativa) é apropriada por se tratar de análise de um único documento.

## 5. Correção de consistência entre documentos (auditoria da Análise Conjunta, 2026-08-05)

Antes de iniciar a análise comparada de similaridade na pasta "Análise Conjunta", a Skill 02_Análise_Vocab_B (item 3) exige verificar se o mesmo composto/bigrama recebe o mesmo tratamento em todos os documentos comparados. Essa auditoria (registrada de forma centralizada em `Análise Conjunta/`) identificou que o PBIA já protegia corretamente a maioria dos bigramas institucionais compartilhados entre documentos (Public Sector, Private Sector, Federal Government, Machine Learning, Value Chain, Data Center(s), Data Infrastructure, Research & Development), mas **não protegia "AI Act"** como bigrama — as 2 ocorrências do termo (referência à regulação europeia de IA, usada como termo de comparação internacional no corpo do PBIA e no glossário de siglas) permaneciam soltas como "AI" (absorvido pelo bigrama `Artificial Intelligence (AI)`) + "act" (token genérico). Como "AI Act" é protegido como bigrama institucional nos dois documentos europeus (27 e 13 ocorrências, respectivamente), a ausência de proteção equivalente no PBIA quebraria a comparabilidade desse termo entre documentos.

**Correção aplicada:** adicionado o padrão `\bAI Act\b` ao `COMPOUND_TERMS` de `pbia.ipynb`, posicionado **antes** do padrão genérico `Artificial Intelligence|AI` na lista (ordem da mais específica para a mais genérica, conforme já orienta o comentário do próprio bloco de código), para que "AI Act" seja resolvido primeiro e não seja consumido pelo bigrama "AI" solto. O notebook foi reexecutado; "AI Act" agora conta 2 ocorrências sob rótulo próprio (abaixo do corte de Top 50, mas corretamente identificável e comparável entre documentos).

## 6. Histórico de atualizações

- **2026-08-05 (criação):** primeira análise de vocabulário do PBIA (gráfico de barras horizontais, Top 25 termos), executada dentro de `pbia.ipynb`.
- **2026-08-05 (revisão metodológica):** auditoria das 58 formas hifenizadas (já preservadas desde a criação, mas agora formalmente auditadas — Seção 1.4), novos bigramas de desambiguação contextual para "power"/"state(s)"/"generation" (Seções 1.5, 2.5), expansão da normalização morfológica com 39 novos pares nominais e, pela primeira vez, 22 famílias verbais (Seção 2.3), e expansão do corte para Top 50 (Seção 3). Alterações determinadas pelo usuário para toda a pasta "Análise Documentos IA" (Brasil, China, Estados Unidos, Europa) e replicadas nas Skills 02_Análise_Vocab_A/B.
- **2026-08-05 (correção de consistência entre documentos):** adicionada proteção do bigrama "AI Act" (Seção 5), motivada pela auditoria de consistência exigida antes da análise comparada da pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B, item 3).
