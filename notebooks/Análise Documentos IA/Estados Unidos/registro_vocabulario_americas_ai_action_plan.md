# Registro de Análise de Vocabulário — americas_ai_action_plan.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 6), associado ao documento `americas_ai_action_plan.json` (América's AI Action Plan, Estados Unidos). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês.
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"U.S."` → `"United States"`, e o bigrama `"United States"` tratado como unidade lexical única (`united_states`) | Sigla e forma por extenso designam exatamente o mesmo referente (o país). |
| `"Artificial Intelligence"` → `"AI"` | Sigla e forma por extenso designam exatamente o mesmo referente (o conceito de IA). |
| Remoção do subtítulo fixo `"Recommended Policy Actions"` (30 ocorrências) | Rótulo estrutural repetido mecanicamente antes de cada lista de ações recomendadas, sem nenhuma ocorrência com sentido distinto — não é vocabulário empregado organicamente no texto corrido, mesma natureza dos cabeçalhos de página já descartados na Skill01. |

## 2. Tokenização

Sequências de letras (`[A-Za-z]+`); qualquer caractere não alfabético (espaço, hífen, apóstrofo, ponto, parênteses, barra) tratado como separador — regra única, sem exceções, aplicada a todos os hífens do texto (ex.: "open-source" → "open" + "source"; "AI-related" → "AI" + "related").

## 3. Palavras removidas (funcionais/resíduos) — lista completa

Artigos, preposições, conjunções, pronomes, verbos auxiliares/modais e conectores discursivos genéricos do inglês:

```
a, an, the, and, or, but, nor, so, yet, if, because, while, although, that, which, who, whom, whose,
when, where, how, than, whether, as, this, these, those, it, its, they, their, them, theirs, he, she,
his, her, him, himself, herself, itself, themselves, we, our, ours, us, you, your, yours, i, my, mine,
is, are, was, were, be, been, being, am, has, have, had, having, do, does, did, doing, will, would,
shall, should, can, could, may, might, must, to, of, in, on, at, by, for, with, from, into, through,
across, throughout, under, over, without, within, among, between, via, per, about, upon, toward,
towards, not, no, nor, also, more, most, many, much, very, only, further, therefore, thus, however,
moreover, there, here, such, other, others, any, all, both, each, every, some, including, include,
includes, included, etc, eg, ie
```

Adicionalmente: tokens de um único caractere (resíduos de tokenização de abreviações pontuadas como "e.g." e de possessivos como "nation's" → fragmento solto "s").

**Não removido, por decisão deliberada:** verbos de ação substantivos para a análise (ex.: *ensure*, *establish*, *develop*, *build*, *expand*, *promote*, *support*, *lead/led*) foram mantidos, por carregarem sinal analítico legítimo sobre a orientação de ação do documento — a única exclusão de natureza "estrutural" foi o subtítulo fixo "Recommended Policy Actions" (ver seção 1), não os verbos em si.

## 4. Agrupamentos de variantes (normalização) — termo representativo e membros

**Substantivos singular/plural** (35 grupos):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| systems | system, systems |
| models | model, models |
| agencies | agency, agencies |
| technology | technology, technologies |
| programs | program, programs |
| workers | worker, workers |
| controls | control, controls |
| standards | standard, standards |
| capabilities | capability, capabilities |
| tools | tool, tools |
| actions | action, actions (após remoção do subtítulo estrutural, ver seção 1) |
| risks | risk, risks |
| developers | developer, developers |
| initiatives | initiative, initiatives |
| stakeholders | stakeholder, stakeholders |
| frameworks | framework, frameworks |
| resources | resource, resources |
| occupations | occupation, occupations |
| assessments | assessment, assessments |
| evaluations | evaluation, evaluations |
| regulations | regulation, regulations |
| values | value, values |
| threats | threat, threats |
| vulnerabilities | vulnerability, vulnerabilities |
| centers | center, centers |
| innovation | innovation, innovations |
| needs | need, needs |
| skills | skill, skills |
| countries | country, countries |
| efforts | effort, efforts |
| employers | employer, employers |
| industry | industry, industries |
| partners | partner, partners |
| sector | sector, sectors |
| services | service, services |
| sources | source, sources |
| states (subnacionais dos EUA — distinto de "United States") | state, states |

**Conjugações verbais** (12 famílias):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| lead / led | lead, leads, leading, led |
| develop | develop, develops, developing, developed |
| create | create, creates, creating, created |
| build | build, builds, building, built |
| establish | establish, establishes, establishing, established |
| ensure | ensure, ensures, ensuring, ensured |
| promote | promote, promotes, promoting, promoted |
| expand | expand, expands, expanding, expanded |
| support | support, supports, supporting, supported |
| make | make, makes, making, made |
| require | require, requires, requiring, required |
| use | use, uses, used, using |

**Siglas / formas por extenso:** AI ⟷ Artificial Intelligence; United States ⟷ U.S. (ambos já aplicados no pré-processamento, seção 1).

## 5. Pares deliberadamente NÃO agrupados (grafia semelhante, referente distinto)

| Termos | Motivo de manter separados |
|---|---|
| America / American / Americans | Classes gramaticais e referentes distintos: topônimo, adjetivo e substantivo plural (pessoas). |
| research / researchers | "research" é a atividade (substantivo não contável); "researchers" designa os agentes (pessoas) — mesma lógica do par provide/providers. |
| development / develop | Substantivo vs. verbo (variação derivacional, não flexional — a Skill exige agrupar apenas flexões de um mesmo lema, não formas derivadas entre classes gramaticais). |
| security / secure | Substantivo vs. adjetivo/verbo — derivacional, não flexional. |
| state(s) / United States | "state(s)" no documento refere-se predominantemente a estados subnacionais dos EUA (ex.: "a state's AI regulatory climate"), referente distinto de "United States" o país. |
| leadership / lead-led-leading-leads | "leadership" é substantivo abstrato derivado; mantido fora do agrupamento verbal por ser outra classe gramatical. |
| technical / technological | Sinônimos próximos, mas grafias e possivelmente nuances distintas; não constituem a mesma forma lexical. |
| provide / providers | Verbo vs. substantivo-agente (pessoas/entidades). |
| economic / economy | Adjetivo vs. substantivo — derivacional. |
| advance / advanced | Verbo vs. adjetivo — usos com sentidos distintos ("to advance the science of AI" vs. "advanced AI compute"). |
| intelligence (sentido de "Intelligence Community"/inteligência de segurança) | Mantido fora da fusão com "AI": apenas o bigrama exato "Artificial Intelligence" foi fundido a "AI"; ocorrências de "intelligence" fora desse bigrama preservam seu sentido de inteligência/serviços de inteligência (ex.: "Intelligence Community", "raw intelligence data"). |

## 6. Critério de corte aplicado

Nas visualizações já produzidas: **Top 25 termos por frequência absoluta**, em ordem decrescente, após as etapas 1–4 acima. Frequência absoluta (não relativa) é apropriada porque a análise é interna a um único documento — a normalização relativa entre documentos de tamanhos distintos é exigida apenas na pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B), que não se aplica aqui.

## 7. Histórico de atualizações

- **2026-08-05:** criação do registro. Metodologia completa (pré-processamento, tokenização, remoção, normalização, corte) aplicada para o gráfico de barras horizontais dos 25 termos mais frequentes, produzido no notebook `winning_race.ipynb`.