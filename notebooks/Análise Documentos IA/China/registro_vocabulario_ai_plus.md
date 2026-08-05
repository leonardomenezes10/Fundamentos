# Registro de Análise de Vocabulário — ai_plus.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 6), associado ao documento `ai_plus.json` (Opinions of the State Council on Deepening the Implementation of the "Artificial Intelligence+" Initiative, China). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês (tradução oficial do CSET do documento original em chinês — o idioma do texto não corresponde ao idioma nativo do país de origem, conforme alerta a própria Skill 02_Análise_Vocab_A).
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"Artificial Intelligence+"` / `"Artificial intelligence+"` (2 ocorrências, grafia por extenso) e `"AI+"` (9 ocorrências, forma abreviada) unificados no rótulo `AI+` (11 ocorrências no total) | Sigla e forma por extenso designam exatamente o mesmo referente: o nome próprio da iniciativa/política. Mantido **separado** do termo genérico `AI` (ver seção 5) porque os dois designam referentes distintos — a iniciativa nomeada vs. a tecnologia como campo. |
| `"open-source"` (9 ocorrências, sempre grafada com hífen) tratada como unidade lexical única | Expressão técnica composta que designa um único conceito (modelos/ferramentas/dados abertos), central a uma das seis seções autônomas do documento ("(11) Promote a thriving open-source ecosystem") e explicitamente citada no resumo da própria tradução CSET como um dos temas do documento. Fragmentá-la em "open"+"source" dissolveria esse sentido em dois termos genéricos, conforme a Skill 02_Análise_Vocab_A determina para expressões compostas com significado próprio. |

## 2. Tokenização

Sequências de letras (`[A-Za-z]+`); qualquer caractere não alfabético (espaço, hífen, apóstrofo, ponto, parênteses, barra, `&`, dígitos) tratado como separador. Compostos com hífen **além** dos dois casos protegidos na seção 1 (ex.: "AI-driven", "AI-native", "human-computer", "high-quality", "decision-making", "scenario-based") foram fragmentados em suas palavras componentes — regra única, sem exceções adicionais além das já justificadas acima, para não introduzir uma lista extensa e pouco auditável de "quais outros hifens preservar" (ver limitações no notebook).

## 3. Palavras removidas (funcionais/resíduos) — lista completa

Artigos, preposições (incluindo partículas fraseológicas), conjunções, pronomes, verbos auxiliares/modais e conectores discursivos genéricos do inglês:

```
a, an, the, and, or, but, nor, so, yet, if, because, while, although, that, which, who, whom, whose,
when, where, how, than, whether, as, this, these, those, it, its, they, their, them, theirs, he, she,
his, her, him, himself, herself, itself, themselves, we, our, ours, us, you, your, yours, i, my, mine,
is, are, was, were, be, been, being, am, has, have, had, having, do, does, did, doing, will, would,
shall, should, can, could, may, might, must, to, of, in, on, at, by, for, with, from, into, through,
across, throughout, under, over, without, within, among, between, via, per, about, upon, toward,
towards, up, out, not, no, nor, also, more, most, many, much, very, only, further, therefore, thus,
however, moreover, there, here, such, other, others, any, all, both, each, every, some, including,
include, includes, included, etc, eg, ie
```

`up` e `out` foram acrescentados a esta lista em relação ao registro análogo de outros documentos do projeto, por serem partículas preposicionais/fraseológicas sem carga semântica própria neste texto (ex.: "speed up", "carry out").

Adicionalmente removidos:
- **Tokens de um único caractere** — resíduos de tokenização de abreviações com `&` (ex.: "R&D" → fragmentos soltos `r`/`d`; "S&T" → `s`/`t`), de compostos letra-dígito (ex.: "6G" → fragmento solto `g`), de possessivos (ex.: "China's", "AI's", "humanity's", "Party's" → fragmento solto `s`) e de numerais isolados entre aspas (ex.: `"from 1 to N"` → fragmento solto `n`).
- **Numerais romanos estruturais dos quatro cabeçalhos de seção** do documento — "I." (Overall Requirements), "II." (Accelerating Implementation of Key Initiatives), "III." (Strengthening Basic Support Capabilities), "IV." (Organizing Implementation) → tokens `i`/`ii`/`iii`/`iv` — marcadores editoriais de organização do texto, mesma natureza dos cabeçalhos/numeração de página já descartados na Skill01, não vocabulário empregado organicamente.

**Não removido, por decisão deliberada:** os verbos diretivos que estruturam cada item de ação do documento (ex.: *promote*, *strengthen*, *accelerate*, *build*, *explore*, *encourage*, *establish*, *optimize*) foram mantidos, por carregarem sinal analítico legítimo sobre a "gramática de ação" do documento.

## 4. Agrupamentos de variantes (normalização) — termo representativo e membros

**Substantivos singular/plural** (22 grupos, apenas pares em que ambas as formas ocorrem no texto):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| application | application, applications |
| models | model, models |
| services | service, services |
| systems | system, systems |
| capabilities | capability, capabilities |
| industry | industry, industries |
| products | product, products |
| resources | resource, resources |
| technology | technology, technologies |
| talent | talent, talents |
| risks | risk, risks |
| levels | level, levels |
| agents | agent, agents |
| initiatives | initiative, initiatives |
| sectors | sector, sectors |
| structures | structure, structures |
| processes | process, processes |
| policies | policy, policies |
| ecosystems | ecosystem, ecosystems |
| evaluations | evaluation, evaluations |
| platforms | platform, platforms |
| approach | approach, approaches |

**Conjugações verbais** (15 famílias, apenas onde mais de uma flexão ocorre no texto):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| promote | promote, promotes, promoting, promoted |
| strengthen | strengthen, strengthens, strengthening, strengthened |
| accelerate | accelerate, accelerates, accelerating, accelerated |
| support | support, supports, supporting, supported |
| build | build, builds, building, built |
| develop | develop, develops, developing, developed |
| create | create, creates, creating, created |
| establish | establish, establishes, establishing, established |
| improve | improve, improves, improving, improved |
| enhance | enhance, enhances, enhancing, enhanced |
| explore | explore, explores, exploring, explored |
| encourage | encourage, encourages, encouraging, encouraged |
| deepen | deepen, deepens, deepening, deepened |
| optimize | optimize, optimizes, optimizing, optimized |
| implement | implement, implements, implementing, implemented |

**Siglas / formas por extenso / expressões compostas:** `AI+` ⟷ `Artificial Intelligence+` / `Artificial intelligence+` (protegido no pré-processamento, seção 1); `open-source` tratada como unidade composta (protegido no pré-processamento, seção 1).

## 5. Pares deliberadamente NÃO agrupados (grafia ou sentido semelhante, referente ou classe gramatical distintos)

| Termos | Motivo de manter separados |
|---|---|
| AI (81) / AI+ (11) | `AI+` é o nome próprio da iniciativa/política (usado, entre outros lugares, como prefixo fixo dos seis subtítulos "(1)–(6)" da Parte II); `AI` genérico designa a tecnologia como campo. Referentes distintos apesar da sobreposição lexical — mesma lógica do par "United States"/"state(s)" já tratado como não-fundível na análise análoga dos EUA neste projeto. |
| intelligent (32) / intelligentization (7) / intelligentized (6) / smart (15) | Quatro itens lexicais distintos do mesmo campo semântico: adjetivo, substantivo, particípio/adjetivo e sinônimo não-cognato, respectivamente. Nenhum par compartilha o mesmo lema — fundi-los apagaria uma distinção terminológica central ao vocabulário característico do documento. |
| driven (6) / drive, drives, driving (3, agrupados) | "driven" ocorre exclusivamente como adjetivo composto ("AI-driven", "data-driven", "intelligence-driven"), nunca como verbo finito ou progressivo — particípio adjetival vs. verbo, uso derivacional/funcional distinto. |
| integrated (5) / integrate, integrates, integrating (2, agrupados) | Mesma lógica de "driven": todas as 5 ocorrências de "integrated" são adjetivais ("an integrated system", "integrated national spatial planning"), não verbo finito. |
| development (37) / develop (verbo, 8 agrupado) | Substantivo vs. verbo — variação derivacional, não flexional (mesmo par documentado como não-fundível na análise dos EUA). |
| innovation (13) / innovative (2) / innovate (4) | Substantivo, adjetivo e verbo — três classes gramaticais distintas derivadas da mesma raiz, não flexões de um único lema. |
| implementation (6) / implement (verbo, 4 agrupado) | Substantivo vs. verbo — derivacional, não flexional. |
| integration (6) / integrate, integrated | Substantivo vs. verbo/adjetivo — derivacional. |
| capacity (2) / capability, capabilities (15, agrupados) | Quase-sinônimos em português ("capacidade"/"capacidade"), mas lemas distintos em inglês — risco clássico de fusão por "falso amigo" semântico, evitado. |
| form, forms (5) / format, formats (4) | Grafia parecida, lemas totalmente distintos ("forma" vs. "formato/modelo de negócio"). |
| compute (9) / computing (3) | Caso de dúvida real: o próprio texto aproxima os dois termos ("international cooperation in computing power ('compute')"), mas "computing" ocorre sempre como modificador atributivo ("computing cluster", "computing resource") enquanto "compute" ocorre como substantivo de massa autônomo ("intelligent compute", "compute network"). Resolvido em favor da **não fusão**, por dúvida real quanto à identidade estrita do referente — critério conservador exigido pela Skill. |
| security (9) / safety (3) | Palavras distintas do inglês, ainda que o documento por vezes as empregue emparelhadas ("safety and security governance") — não são flexões nem grafias de um mesmo lema. |

## 6. Critério de corte aplicado

Nas visualizações já produzidas: **Top 25 termos por frequência absoluta**, em ordem decrescente, após as etapas 1–4 acima. Frequência absoluta (não relativa) é apropriada porque a análise é interna a um único documento — a normalização relativa entre documentos de tamanhos distintos é exigida apenas na pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B), que não se aplica aqui. Este documento é sensivelmente mais curto (3.025 tokens tratáveis) que outros já analisados no projeto, o que reforça que suas contagens absolutas não devem ser comparadas diretamente às de outros países fora da pasta "Análise Conjunta".

## 7. Histórico de atualizações

- **2026-08-05:** criação do registro. Metodologia completa (pré-processamento, tokenização, remoção, normalização, corte) aplicada para o gráfico de barras horizontais dos 25 termos mais frequentes, produzido no notebook `ai_plus.ipynb`.