# Registro de Análise de Vocabulário — new_generation_ai_development_plan.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 6), associado ao documento `new_generation_ai_development_plan.json` (State Council Notice on the Issuance of the New Generation Artificial Intelligence Development Plan, China, 2017). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês (tradução publicada pela New America/DigiChina; o documento original é em chinês, mas a análise recai exclusivamente sobre o campo `texto_completo`, conforme protocolo da Skill02).
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"artificial intelligence"` (case-insensitive) → `"AI"` | Sigla e forma por extenso designam exatamente o mesmo referente (o conceito de IA). Ocorre apenas 3 vezes no texto corrido (2x no título/cabeçalho do documento, 1x na frase de definição "artificial intelligence (AI)" no primeiro parágrafo) — a partir daí o documento usa exclusivamente a sigla "AI". A ocorrência de "artificial data-oriented" (Seção IV, plataformas de dados) foi verificada e **não** corresponde a esse padrão (não contém "intelligence" na sequência), logo não foi afetada pela substituição. |

## 2. Tokenização

Sequências de letras (`[A-Za-z]+`); qualquer caractere não alfabético (espaço, hífen, apóstrofo, ponto, parênteses, barra) tratado como separador — mesma regra única e uniforme adotada em `registro_vocabulario_americas_ai_action_plan.md` (Estados Unidos), para manter consistência metodológica entre os documentos do projeto. Como consequência, compostos com hífen são fragmentados em suas palavras componentes (ver Seção 7, limitações, para o impacto específico neste documento).

## 3. Palavras removidas (funcionais/resíduos) — lista completa

Mesma lista de palavras funcionais do inglês aplicada ao documento dos Estados Unidos (artigos, preposições, conjunções, pronomes, verbos auxiliares/modais e conectores discursivos genéricos):

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

Adicionalmente: tokens de um único caractere (resíduo de tokenização de possessivos, ex.: "China's" → fragmento solto "s").

## 4. Agrupamentos de variantes (normalização) — termo representativo e membros

**Substantivos singular/plural** (30 grupos):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| technology | technology, technologies |
| systems | system, systems |
| applications | application, applications |
| theory | theory, theories |
| platforms | platform, platforms |
| enterprises | enterprise, enterprises |
| breakthroughs | breakthrough, breakthroughs |
| products | product, products |
| robots | robot, robots |
| capabilities | capability, capabilities |
| bases | base, bases (verificado: sentido consistente de "polo/centro institucional" — ex. "innovation base(s)", "talent base", "training base(s)" — nunca no sentido militar) |
| resources | resource, resources |
| mechanisms | mechanism, mechanisms |
| tasks | task, tasks |
| projects | project, projects |
| demonstrations | demonstration, demonstrations |
| areas | area, areas |
| methods | method, methods |
| models | model, models |
| standards | standard, standards |
| fields | field, fields |
| policies | policy, policies |
| regulations | regulation, regulations |
| laws | law, laws |
| talent | talent, talents |
| levels | level, levels |
| results | result, results |
| sectors | sector, sectors |
| environments | environment, environments |
| services | service, services |

**Conjugações/flexões verbais** (18 famílias):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| strengthen | strengthen, strengthens, strengthening, strengthened |
| promote | promote, promotes, promoting, promoted |
| establish | establish, establishes, establishing, established |
| develop | develop, develops, developing, developed |
| construct | construct, constructs, constructing, constructed |
| build | build, builds, built |
| accelerate | accelerate, accelerates, accelerating, accelerated |
| encourage | encourage, encourages, encouraging, encouraged |
| improve | improve, improves, improving, improved |
| achieve | achieve, achieves, achieving, achieved |
| enhance | enhance, enhances, enhancing (**"enhanced" excluído deste grupo** — ver Seção 5) |
| form | form, forms, forming, formed |
| launch | launch, launches, launching, launched |
| focus | focus, focuses, focusing, focused |
| integrate | integrate, integrates, integrating, integrated |
| coordinate | coordinate, coordinates, coordinating, coordinated |
| lead | lead, leads, leading, led |
| create | create, creates, creating, created |

**Siglas / formas por extenso:** AI ⟷ artificial intelligence (já aplicado no pré-processamento, Seção 1).

## 5. Pares deliberadamente NÃO agrupados (grafia/lema semelhante, referente distinto)

| Termos | Motivo de manter separados |
|---|---|
| development / develop | Substantivo vs. verbo — variação derivacional, não flexional (mesma lógica do par development/develop já registrado para os EUA). |
| intelligent / intelligence | Adjetivo vs. substantivo — derivacional. "intelligent" (122 ocorrências) é usado como modificador de dezenas de domínios ("intelligent manufacturing", "intelligent society", "intelligent economy" etc.); "intelligence" (58) é o substantivo (ex. "swarm intelligence", "hybrid intelligence", além do núcleo do próprio conceito de AI). |
| intelligentization | Substantivo próprio do documento (tradução de 智能化), com 13 ocorrências; mantido fora de qualquer fusão com intelligent/intelligence por ser uma forma lexical distinta, não uma flexão de nenhuma das duas. |
| smart / intelligent | Duas palavras inglesas genuinamente distintas, aparentemente usadas pelos tradutores como equivalentes alternados de um mesmo campo semântico em chinês (ex. "smart economy"/"intelligent economy", "smart society"/"intelligent society"). Como a Skill exige que a fusão ocorra apenas entre formas que designam exatamente o mesmo referente **e** compartilham a mesma forma lexical, e não entre sinônimos de tradução, os dois termos foram mantidos separados — ver limitação correspondente na Seção 7. |
| enhance / enhancing / **enhanced** | "enhanced" (16 ocorrências) funciona neste documento, de forma consistente, como parte do termo técnico fixo do próprio documento **"hybrid (and) enhanced intelligence"** — uma categoria nomeada na taxonomia de teorias de IA do plano (Seção III.1) — e não como flexão livre do verbo genérico "to enhance". Fundir "enhanced" a "enhance"/"enhancing" (18 ocorrências, sentido genérico de "melhorar/reforçar") juntaria dois referentes distintos sob um único rótulo, violação expressa da salvaguarda metodológica da Skill 02_Análise_Vocab_A. |
| research / researching | "research" (104) é usado predominantemente como substantivo (ex. "AI research", "scientific research", "research institutions"); "researching" (12) ocorre majoritariamente como abertura de item de lista técnica (ex. "Researching short text computing...", nos blocos de tarefas-foco da Seção III). Mesma lógica do par research/researchers já registrado para os EUA — substantivo vs. função gramatical distinta. |
| support / supporting / supports | "support" (68) é usado de forma mista, com peso substancial como substantivo (ex. "Support Platforms", "policy support", "long-term support") e como verbo; "supporting" (6) e "supports" (1) são inequivocamente verbais. Fundi-los sob um único rótulo obscureceria essa mistura substantivo/verbo sem justificativa linguística clara — mantidos separados, mesma cautela aplicada a "research/researching". |
| driving / driven / drive | Identificados ao menos três referentes distintos sob o mesmo lema: (a) direção autônoma de veículos ("unmanned driving", "automatic driving", sentido literal de dirigir); (b) compostos adjetivais fragmentados pela regra de hífen (Seção 2), como "data-driven" e "knowledge-driven" ("baseado em/orientado por"); (c) a locução "driving force" ("força motriz"). Diante de referentes genuinamente distintos sob a mesma grafia, os três tokens foram mantidos completamente separados, em vez de arriscar uma fusão incorreta. |
| building | Uso misto identificado: majoritariamente gerúndio do verbo "to build" (ex. "building an intelligent society", "building service system architecture"), mas com ao menos duas ocorrências claramente nominais, referindo-se a edificações físicas (ex. "building systems", "building facilities" — sistemas/instalações prediais). Por essa ambiguidade genuína e por não ser possível desambiguar automaticamente as 9 ocorrências, "building" foi mantido fora do agrupamento verbal de "build" (que reúne apenas build/builds/built, todas inequivocamente verbais). |
| process / processing | "process" (4, sempre substantivo — "process management", "the process of constructing") e "processing" (12, predominantemente como núcleo de termos técnicos compostos — "natural language processing", "information processing", "knowledge processing", "graphic processing") foram mantidos separados: embora relacionados, "processing" funciona neste documento como elemento fixo de terminologia técnica de IA, com peso analítico próprio, distinto do uso genérico de "process" como "procedimento/etapa". |
| share / sharing | "share" (1 ocorrência: "share investment", sentido financeiro de participação/quota) e "sharing" (17 ocorrências, sentido de "compartilhar/uso compartilhado" — ex. "open-source sharing", "resource sharing") designam referentes diferentes; fundi-los seria um erro de mesmo tipo do par state(s)/United States já identificado nos EUA (coincidência lexical parcial, referente distinto). |
| decision / making | O bigrama fixo **"decision-making"** ocorre 23 vezes no texto e, por força da regra uniforme de tokenização por hífen (Seção 2), é fragmentado em "decision" (24 ocorrências no total, das quais 23 vêm do composto) e "making" (25 ocorrências no total, das quais 23 vêm do composto). Optou-se por **não** tratar "decision-making" como unidade composta especial e **não** fundir "making" ao verbo genérico "make" (12 ocorrências, sentido causativo distinto — ex. "making China the world's primary AI innovation center"), para manter a mesma regra uniforme de tokenização adotada no documento dos EUA, sem exceções ad hoc. O efeito de fragmentação resultante é registrado como limitação explícita (Seção 7). |

## 6. Critério de corte aplicado

**Top 25 termos por frequência absoluta**, em ordem decrescente, após as etapas 1–4 acima. Frequência absoluta (não relativa) é apropriada porque a análise é interna a um único documento — a normalização relativa entre documentos de tamanhos distintos é exigida apenas na pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B), que não se aplica aqui.

**Ajuste de empate na fronteira do corte:** a 25ª posição (termo "major", frequência 43) empata exatamente com o termo seguinte ("focus", frequência 43). Para evitar um corte arbitrário entre dois termos de frequência idêntica, o critério foi estendido para incluir todos os termos empatados no valor de corte — resultando em **26 termos** no gráfico final, todos com frequência ≥ 43.

## 7. Limitações metodológicas identificadas e registradas

- **Fragmentação por hífen mais acentuada neste documento do que no dos EUA.** A regra uniforme de tokenização (hífen = separador, Seção 2) fragmenta um número comparativamente alto de compostos técnicos característicos da prosa de planejamento chinês traduzida, entre eles: "decision-making" → decision + making (23 ocorrências fragmentadas, ver Seção 5); "data-driven"/"knowledge-driven" → driven (ver Seção 5); "high-end"/"high-level" → contribuem para inflar o token solto "high" (53 ocorrências, 20º lugar no corte); "brain-inspired" → contribui para "brain" (23); "open-source" → contribui para "open" (30). Esse efeito é qualitativamente o mesmo já observado e registrado no documento dos EUA (caso "open-source"/"open-weight"), mas de maior magnitude relativa aqui.
- **"smart" e "intelligent" tratados como termos totalmente independentes** (Seção 5), apesar de indícios de que os tradutores os usam de forma intercambiável para o mesmo campo semântico em chinês. Isso pode **subestimar** a proeminência conjunta desse campo semântico no gráfico (cada termo aparece isoladamente, em vez de somados), mas fundi-los exigiria um julgamento de equivalência conceitual entre sinônimos de tradução — não autorizado pela Skill 02_Análise_Vocab_A, que exige identidade de referente e de forma lexical, não apenas proximidade de sentido.
- **Contagem lexical, não semântica**, como em qualquer aplicação desta metodologia: não foi feita desambiguação de sentido dentro de um mesmo token além dos casos explicitamente verificados e registrados na Seção 5.
- **Texto de partida é uma tradução**, não o original em chinês. Toda a análise de vocabulário descreve as escolhas lexicais dos tradutores da New America/DigiChina, não os termos chineses originais diretamente — limitação estrutural inerente ao uso de `texto_completo` conforme protocolo da Skill02.

## 8. Histórico de atualizações

- **2026-08-05:** criação do registro. Metodologia completa (pré-processamento, tokenização, remoção, normalização, corte com ajuste de empate) aplicada para o gráfico de barras horizontais dos 26 termos mais frequentes, produzido no notebook `new_generation.ipynb`.