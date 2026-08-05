# Registro de Análise de Vocabulário — apply_ai_strategy.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 6), associado ao documento `apply_ai_strategy.json` (Apply AI Strategy, União Europeia). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês (variante britânica do inglês institucional da UE — ex.: *centres*, *organisation*, *specialised*).
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"Artificial Intelligence"` → `"AI"` (2 ocorrências) | Sigla e forma por extenso designam exatamente o mesmo referente (o conceito de IA). O trigrama `"Artificial General Intelligence"` (AGI, 1 ocorrência) foi deliberadamente **excluído** desta fusão: o próprio texto o define como um conceito distinto e mais específico ("AI capable of performing any cognitive task that humans can"), e fundi-lo a "AI" conflacionaria dois conceitos diferentes. |
| `"European Union"` → `"EU"` (1 ocorrência) | Sigla e forma por extenso designam exatamente o mesmo referente (o bloco); "EU" já é a forma amplamente dominante no restante do documento (53 ocorrências adicionais). |
| `"Member States"` → `member_states` (12 ocorrências) | Expressão composta institucional fixa referente aos Estados-membros da UE — estrutura análoga ao par "United States"/"U.S." já tratado no registro de vocabulário do documento dos Estados Unidos deste projeto. Não inclui a única ocorrência genérica de "States" fora do bigrama exato ("...as States and citizens face increasingly complex..."), mantida separada por não se referir especificamente aos Estados-membros da UE. |
| `"digital twin"` / `"digital twins"` → `digital_twins` (1 + 5 = 6 ocorrências) | Termo técnico composto, definido no próprio texto ("virtual replicas of real-world objects or processes"); fragmentá-lo em "digital" + "twin(s)" distorceria tanto a contagem do adjetivo genérico "digital" (15 ocorrências fora deste termo) quanto o significado do conceito técnico — mesma lógica do exemplo "aprendizado de máquina" citado pela própria Skill 02_Análise_Vocab_A. |
| `"AI Act"` → `ai_act` (13 ocorrências) | Nome de instrumento legal específico (Regulamento (UE) 2024/1689), distinto de outros atos nomeados no documento que também contêm a palavra "Act" (`"Cloud and AI Development Act"`, `"Industrial Accelerator Act"`, 1 ocorrência cada — mantidos como texto corrido comum, não fundidos a "AI Act" nem entre si). |
| Isolamento manual de 1 ocorrência do substantivo "building" (não gerúndio) | Em "*a building or even of a human body*", "building" é substantivo comum (um edifício), não o gerúndio do verbo "build". Identificado por leitura contextual e isolado antes da tokenização (substituído por `buildingnoun`) para ser corretamente agrupado ao substantivo plural "buildings" (2 ocorrências) — e não à família verbal de "build" (as demais 12 ocorrências de "building" no documento são gerúndio/particípio, como em "Building on the AI Continent Action Plan"). |

## 2. Tokenização

Sequências de letras e do caractere `_` (usado internamente apenas para os cinco termos compostos tratados acima); qualquer outro caractere não alfabético (espaço, hífen, apóstrofo, ponto, parênteses, barra) tratado como separador — regra única, sem exceções, aplicada a todos os hífens não cobertos pelo pré-processamento (ex.: "cross-border" → "cross" + "border"; "AI-powered" → "AI" + "powered"; "open-source" → "open" + "source").

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
includes, included, etc, eg, ie, e, g
```

Adicionalmente: tokens de um único caractere (resíduos de tokenização de abreviações pontuadas como "e.g." e de possessivos como "EU's" → fragmento solto "s").

**Não removido, por decisão deliberada:** os verbos de ação que estruturam as listas "the Commission will:" (ex.: *support*, *establish*, *develop*, *build*, *ensure*, *promote*, *foster*, *accelerate*, *launch*) foram mantidos, por carregarem sinal analítico legítimo sobre a orientação de ação do documento.

## 4. Agrupamentos de variantes (normalização) — termo representativo e membros

**Siglas / formas por extenso / compostos institucionais e técnicos** (tratados no pré-processamento, seção 1): AI ⟷ Artificial Intelligence; EU ⟷ European Union; Member States (composto); digital twins (composto); AI Act (composto).

**Substantivos singular/plural** (68 grupos):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| sectors | sector, sectors |
| models | model, models |
| solutions | solution, solutions |
| systems | system, systems |
| tools | tool, tools |
| services | service, services |
| needs | need, needs, needed |
| actions | action, actions |
| initiatives | initiative, initiatives |
| challenges | challenge, challenges |
| applications | application, applications |
| infrastructures | infrastructure, infrastructures |
| skills | skill, skills |
| frameworks | framework, frameworks |
| networks | network, networks |
| platforms | platform, platforms |
| organisations | organisation, organisations |
| administrations | administration, administrations |
| hubs | hub, hubs |
| practices | practice, practices |
| tasks | task, tasks |
| robots | robot, robots |
| vehicles | vehicle, vehicles |
| labs | lab, labs |
| benefits | benefit, benefits |
| assets | asset, assets |
| architectures | architecture, architectures |
| flagships | flagship, flagships |
| boards | board, boards |
| resources | resource, resources |
| threats | threat, threats |
| dialogues | dialogue, dialogues |
| developments | development, developments |
| ecosystems | ecosystem, ecosystems |
| capacities | capacity, capacities |
| technologies | technology, technologies |
| sciences | science, sciences |
| processes | process, processes |
| decisions | decision, decisions |
| areas | area, areas |
| ways | way, ways |
| businesses | business, businesses |
| humans | human, humans |
| alliances | alliance, alliances |
| purposes | purpose, purposes |
| steps | step, steps |
| funds | fund, funds |
| risks | risk, risks |
| interests | interest, interests |
| chains | chain, chains |
| startups | startup, startups |
| strengths | strength, strengths |
| professionals | professional, professionals |
| drivers | driver, drivers |
| factors | factor, factors |
| partners | partner, partners |
| partnerships | partnership, partnerships |
| governments | government, governments |
| forms | form, forms |
| results | result, results |
| elements | element, elements |
| gaps | gap, gaps |
| values | value, values |
| innovations | innovation, innovations |
| strategies | strategy, strategies |
| industries | industry, industries |
| buildings | building (apenas o substantivo comum isolado na seção 1), buildings |
| states (genérico, distinto de "Member States") | state, states (apenas a ocorrência residual fora do bigrama "Member States") |

**Conjugações verbais** (34 famílias):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| support | support, supports, supporting, supported |
| foster | foster, fosters, fostering, fostered |
| promote | promote, promotes, promoting, promoted |
| develop (verbo) | develop, develops, developing, developed |
| build | build, builds, building (gerúndio), built |
| ensure | ensure, ensures, ensuring, ensured |
| enable | enable, enables, enabling, enabled |
| accelerate | accelerate, accelerates, accelerating, accelerated |
| deploy | deploy, deploys, deploying, deployed |
| create | create, creates, creating, created |
| facilitate | facilitate, facilitates, facilitating, facilitated |
| provide | provide, provides, providing, provided |
| address | address, addresses, addressing, addressed |
| improve | improve, improves, improving, improved |
| launch | launch, launches, launching, launched |
| establish | establish, establishes, establishing, established |
| monitor | monitor, monitors, monitoring, monitored |
| help | help, helps, helping, helped |
| use | use, uses, using, used |
| increase | increase, increases, increasing, increased |
| boost | boost, boosts, boosting, boosted |
| drive | drive, drives, driving |
| deliver | deliver, delivers, delivering, delivered |
| leverage | leverage, leverages, leveraging, leveraged |
| secure (verbo/adjetivo) | secure, secures, securing, secured |
| strengthen | strengthen, strengthens, strengthening, strengthened |
| expand | expand, expands, expanding, expanded |
| integrate | integrate, integrates, integrating, integrated |
| encourage | encourage, encourages, encouraging, encouraged |
| protect | protect, protects, protecting, protected |
| reduce | reduce, reduces, reducing, reduced |
| adopt | adopt, adopts, adopting, adopted |
| implement | implement, implements, implementing, implemented |
| reinforce | reinforce, reinforces, reinforcing, reinforced |

## 5. Pares deliberadamente NÃO agrupados (grafia semelhante, referente ou classe gramatical distintos)

| Termos | Motivo de manter separados |
|---|---|
| European / EU / Europe | Classes gramaticais e referentes distintos: adjetivo, sigla institucional e topônimo — análogo direto do caso America/American/Americans já registrado no documento dos Estados Unidos. |
| development / develop | Substantivo vs. verbo — variação derivacional, não flexional (mesmo critério já aplicado no documento dos EUA). |
| security / secure | Substantivo vs. verbo/adjetivo — derivacional, não flexional (mesmo par do documento dos EUA). |
| strategy / strategic | Substantivo vs. adjetivo — derivacional. "strategy"/"strategies" foram fundidos entre si (mesmo lema, flexão de número), mas não a "strategic". |
| economy / economic | Substantivo vs. adjetivo — derivacional (mesmo par citado como exemplo no documento dos EUA). |
| industry / industrial | Substantivo vs. adjetivo — derivacional. "industry"/"industries" foram fundidos entre si, mas não a "industrial". |
| sovereignty / sovereign | Substantivo vs. adjetivo — derivacional. |
| governance / government(s) | Lemas distintos apesar da raiz compartilhada: "governance" designa o processo/sistema de governar; "government(s)" designa o corpo institucional. |
| innovation(s) / innovative | Substantivo vs. adjetivo — derivacional. "innovation"/"innovations" foram fundidos entre si, mas não a "innovative". |
| actions / act | "actions" (substantivo, já normalizado) mantido separado do resíduo "act" (3 ocorrências heterogêneas fora do composto "AI Act": dois outros instrumentos legais nomeados — "Cloud and AI Development Act", "Industrial Accelerator Act" — e um uso verbal, "will act as privileged access point"). |
| Artificial Intelligence/AI vs. Artificial General Intelligence (AGI) | Conceitos distintos por definição do próprio texto; ver seção 1. |
| intelligence (sentido fora de "Artificial Intelligence") | Mantido fora da fusão com "AI": após a fusão do bigrama exato "Artificial Intelligence", os usos remanescentes de "intelligence" preservam sentidos distintos — "medical countermeasures intelligence" (informação/inteligência de vigilância sanitária) e "European Skills Intelligence Observatory" (inteligência de dados do mercado de trabalho). |

## 6. Critério de corte aplicado

Nas visualizações já produzidas: **Top 25 termos por frequência absoluta**, em ordem decrescente, após as etapas 1–4 acima. Frequência absoluta (não relativa) é apropriada porque a análise é interna a um único documento — a normalização relativa entre documentos de tamanhos distintos é exigida apenas na pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B), que não se aplica aqui.

**Observação sobre empates na fronteira do corte:** há empates múltiplos nas posições finais do Top 25 — quatro termos empatados em 23 ocorrências (innovations, actions, potential, energy) e seis termos empatados em 21 ocorrências (technologies, europe, initiatives, systems, defence, security). A ordem entre termos empatados é definida apenas pela ordem de primeira ocorrência no texto (comportamento determinístico do `Counter.most_common()` do Python), sem significado semântico adicional.

## 7. Histórico de atualizações

- **2026-08-05:** criação do registro. Metodologia completa (pré-processamento, tokenização, remoção, normalização, corte) aplicada para o gráfico de barras horizontais dos 25 termos mais frequentes, produzido no notebook `ai_apply_strategy.ipynb`. Nesta mesma data, corrigido um defeito da extração da Skill01: o trecho de `texto_completo` referente ao diagrama de governança havia sido registrado com uma descrição interpretativa em português, em vez de transcrição literal — corrigido antes desta análise de vocabulário para preservar a integridade do corpus em inglês.