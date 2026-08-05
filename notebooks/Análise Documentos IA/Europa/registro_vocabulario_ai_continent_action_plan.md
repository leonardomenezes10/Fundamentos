# Registro de Análise de Vocabulário — ai_continent_action_plan.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 6), associado ao documento `ai_continent_action_plan.json` (AI Continent Action Plan, União Europeia). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês.
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

### 1.1 Remoção de rótulo estrutural

| Operação | Justificativa |
|---|---|
| Remoção do cabeçalho fixo `"Key Commission actions:"` / `"Key Commission / EuroHPC actions:"` / `"Key Commission / EuroHPC Actions:"` (7 ocorrências) | Rótulo estrutural repetido mecanicamente antes de cada lista de ações da Comissão/EuroHPC, sem nenhuma ocorrência com sentido distinto — não é vocabulário empregado organicamente no texto corrido, mesma natureza dos cabeçalhos de página já descartados na Skill01 e do tratamento dado a "Recommended Policy Actions" no registro dos EUA. |

### 1.2 Unificação de expressões compostas que designam um único referente institucional (17 grupos)

O documento é estruturado em torno de nomes de programas, atos legislativos e órgãos compostos por mais de uma palavra. Fragmentá-los em palavras isoladas inflaria artificialmente o termo genérico "AI" (já dominante) e dissolveria o sinal analítico de cada iniciativa específica — exatamente o risco que a Skill 02_Análise_Vocab_A adverte ao tratar de expressões técnicas compostas (item 3, "Atenção a expressões compostas"). Cada expressão abaixo designa um referente único e estável ao longo de todo o documento:

| Expressão composta (todas as variantes de maiúsculas/singular-plural) | Rótulo representativo | Ocorrências |
|---|---|---|
| "European Union" | EU | 1 |
| "Cloud and AI Development Act" | Cloud and AI Development Act | 6 |
| "EuroHPC Joint Undertaking" | EuroHPC Joint Undertaking | 4 |
| "AI Skills Academy" | AI Skills Academy | 6 |
| "Apply AI Strategy" | Apply AI Strategy | 14 |
| "Data Union Strategy" | Data Union Strategy | 7 |
| "European Digital Innovation Hub(s)" / "Digital Innovation Hub(s)" | Digital Innovation Hubs | 17 |
| "AI in Science" | AI in Science | 6 |
| "AI Gigafactory" / "AI Gigafactories" | AI Gigafactories | 14 |
| "AI Factory" / "AI Factories" | AI Factories | 40 |
| "AI Act" | AI Act | 27 |
| "AI Office" | AI Office | 6 |
| "Member States" | Member States | 25 |
| "Single Market" | Single Market | 9 |
| "Data Lab" / "Data Labs" | Data Labs | 8 |
| "public sector" | public sector | 15 |
| "private sector" | private sector | 2 |

Ordem de aplicação: das expressões mais longas/específicas para as mais curtas (ex.: "Cloud and AI Development Act" antes de "AI Act"), para que nenhuma expressão longa seja parcialmente capturada por um padrão mais curto. Verificado que nenhuma colisão ocorre (ex.: "Cloud and AI Development Act" não contém a sequência contígua "AI Act").

**Caso de atenção resolvido — "Artificial General Intelligence" (AGI):** a expressão "Artificial Intelligence" (2 ocorrências, forma por extenso de "AI") **não** foi fundida ao termo "AI" nesta rodada de análise porque, ao inspecionar as duas ocorrências, uma delas integra a sequência "Artificial General Intelligence (AGI)" — um conceito distinto (rumo à IA de propósito geral), não sinônimo simples de "AI". Como a sigla "AGI" já se tokeniza isoladamente e designa um referente diferente do de "AI", nenhuma fusão foi aplicada a "Artificial (General) Intelligence" para evitar equiparar indevidamente dois conceitos do documento. Isso é tratado como decisão deliberada de não-fusão (ver seção 5).

## 2. Tokenização

Sequências de letras, tratando o sublinhado (`_`) usado internamente nos rótulos de expressões compostas acima como parte do token (`[A-Za-z_]+`); qualquer outro caractere não alfabético (espaço, hífen, apóstrofo, ponto, parênteses, barra) tratado como separador — regra única, sem exceções, aplicada a todos os hífens do texto corrido (ex.: "open-source" → "open" + "source"; "fine-tuning" → "fine" + "tuning").

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

Adicionalmente, específicas deste documento:
- `up`: partícula de verbo frasal ("scaled up", "step up", "set up") sem conteúdo lexical próprio — mesma função estrutural das preposições já listadas acima.
- `well`: fragmento residual do conector discursivo "as well as", papel equivalente a "moreover"/"however", já removidos na lista-base.
- Tokens de um único caractere (resíduo de tokenização de possessivos como "EU's" → fragmento solto "s").

**Não removido, por decisão deliberada:** verbos de ação substantivos para a análise (ex.: *ensure*, *establish*, *develop*, *build*, *support*, *launch*, *facilitate*) foram mantidos, por carregarem sinal analítico legítimo sobre a orientação de ação do documento.

## 4. Agrupamentos de variantes (normalização) — termo representativo e membros

**Substantivos singular/plural** (30 grupos, aplicados sobre o texto já tratado pela seção 1):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| models | model, models |
| services | service, services |
| solutions | solution, solutions |
| sectors | sector, sectors (após extração de "public sector"/"private sector", seção 1.2) |
| initiatives | initiative, initiatives |
| resources | resource, resources |
| stakeholders | stakeholder, stakeholders |
| facilities | facility, facilities |
| partnerships | partnership, partnerships |
| programmes | programme, programmes |
| skills | skill, skills (após extração de "AI Skills Academy", seção 1.2) |
| actions | action, actions (após remoção do rótulo estrutural, seção 1.1) |
| needs | need, needs |
| companies | company, companies |
| startups | startup, startups |
| scaleups | scaleup, scaleups |
| technologies | technology, technologies |
| values | value, values |
| tools | tool, tools |
| networks | network, networks |
| supercomputers | supercomputer, supercomputers |
| talent | talent, talents |
| projects | project, projects |
| funds | fund, funds |
| investments | investment, investments |
| gaps | gap, gaps |
| spaces | space, spaces |
| risks | risk, risks |
| areas | area, areas |
| chips | chip, chips |
| strategy | strategy, strategies |
| development | development, developments |
| capacity | capacity, capacities |

**Conjugações verbais** (26 famílias):

| Rótulo representativo | Variantes agrupadas |
|---|---|
| support | support, supports, supporting, supported |
| launch | launch, launching, launched |
| ensure | ensure, ensures |
| use | use, uses, using, used |
| develop | develop, developing, developed |
| provide | provide, provides, providing, provided |
| facilitate | facilitate, facilitates, facilitating, facilitated |
| train | train, training, trained |
| adopt | adopt, adopted |
| build | build, building |
| create | create, creates, creating |
| strengthen | strengthen, strengthening, strengthened |
| increase | increase, increases, increasing, increased |
| foster | foster, fosters, fostering |
| attract | attract, attracting |
| work | work, works, working |
| set | set, sets |
| link | link, links, linking, linked |
| offer | offer, offers, offering, offered |
| require | require, requires |
| address | address, addresses |
| identify | identify, identifying |
| continue | continue, continues |
| aim | aim, aims, aimed |
| enhance | enhance, enhances |
| promote | promote, promoting |

**Siglas / formas por extenso:** EU ⟷ European Union (aplicado no pré-processamento, seção 1.2).

## 5. Pares deliberadamente NÃO agrupados (grafia semelhante, referente ou classe gramatical distintos)

| Termos | Motivo de manter separados |
|---|---|
| AI / AGI (Artificial General Intelligence) | Conceitos distintos: "AI" é o termo genérico do documento; "AGI" designa especificamente a Inteligência Artificial Geral, um patamar de capacidade explicitamente diferenciado no texto (seção 1.2). Ver caso de atenção na seção 1.2 acima. |
| development / develop | Substantivo vs. verbo — variação derivacional, não flexional (mesma lógica aplicada no registro dos EUA para o par development/develop). |
| security / secure | Substantivo vs. adjetivo/verbo — derivacional, não flexional. |
| advance / advances / advancing / advanced | Mantidos totalmente separados: "advanced" funciona predominantemente como **adjetivo** neste documento (ex.: "advanced AI processors", "advanced AI models", "advanced semiconductors" — 10 das 13 ocorrências de "advanced"), não como particípio passado do verbo "to advance"; e "advances" é majoritariamente **substantivo plural** ("advances in training techniques", "recent advances") e não a forma verbal de terceira pessoa. Ambiguidade de classe gramatical alta demais para fusão segura sem desambiguação manual de cada ocorrência. |
| European / Europe | Adjetivo vs. topônimo (substantivo próprio) — mesma lógica do par America/American já documentado no registro dos EUA. |
| innovation / innovative | Substantivo vs. adjetivo — derivacional. |
| strategy / strategic | Substantivo vs. adjetivo — derivacional (a "Skills Academy" e as diversas "Strategy" nomeadas usam "strategy" substantivo; "strategic sectors"/"strategic autonomy" usam o adjetivo "strategic", referente gramatical distinto). |
| sector / sectorial | Substantivo vs. adjetivo ("sectorial approach", ocorrência única) — derivacional. |
| Member States / State aid | "State aid" (regras de auxílio estatal, 2 ocorrências) designa um instituto jurídico específico da UE, referente distinto de "Member States" (os Estados-membros como atores institucionais); ambos contêm a raiz "state" mas não foram fundidos entre si nem com "Member States". Frequência residual (≤2) não altera o corte de 25 termos aplicado nas visualizações já produzidas. |

## 6. Critério de corte aplicado

Nas visualizações já produzidas: **Top 25 termos por frequência absoluta**, em ordem decrescente, após as etapas 1–4 acima. Frequência absoluta (não relativa) é apropriada porque a análise é interna a um único documento — a normalização relativa entre documentos de tamanhos distintos é exigida apenas na pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B), que não se aplica aqui. O valor de corte (25) foi escolhido, adicionalmente, por consistência com a análise já realizada para o documento dos Estados Unidos (`americas_ai_action_plan.json`), facilitando eventual leitura comparativa qualitativa entre notebooks de países distintos — sem que isso constitua, em si, uma comparação normalizada de frequências (o que exigiria a Skill 02_Análise_Vocab_B).

## 7. Histórico de atualizações

- **2026-08-05:** criação do registro. Metodologia completa (remoção de rótulo estrutural, unificação de 17 expressões compostas institucionais, tokenização, remoção de funcionais/resíduos, normalização de 30 grupos nominais e 26 famílias verbais, corte) aplicada para o gráfico de barras horizontais dos 25 termos mais frequentes, produzido no notebook `ai_continent_action_plan.ipynb`.