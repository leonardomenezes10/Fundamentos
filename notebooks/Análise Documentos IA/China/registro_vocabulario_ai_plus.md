# Registro de Análise de Vocabulário — ai_plus.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 8), associado ao documento `ai_plus.json` (Opinions of the State Council on Deepening the Implementation of the "Artificial Intelligence+" Initiative, China). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês (tradução oficial do CSET do documento original em chinês — o idioma do texto não corresponde ao idioma nativo do país de origem, conforme alerta a própria Skill 02_Análise_Vocab_A).
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05 — revisão metodológica completa determinada pelo usuário (correção da fragmentação por hífen, tratamento de bigramas essenciais, desambiguação contextual de termos polissêmicos e expansão do corte para Top 50).

## 0. Correção metodológica aplicada nesta revisão

A versão anterior deste registro tokenizava tratando **todo hífen como separador universal**, com apenas duas exceções escolhidas manualmente ("AI+" e "open-source"). Essa regra cega fragmentava compostos tecnicamente relevantes — ex.: "decision-making" → "decision"+"making"; "high-quality"/"high-level"/"high-risk" → inflavam artificialmente o token genérico "high" — e, criticamente, **inflava a própria contagem de "AI"**: seis famílias de compostos ("AI-driven", "AI-native", "AI-powered", "AI-based", "AI-enabled", "AI-related", somando 15 ocorrências) eram fragmentadas de modo que o "AI" solto de cada composto se somava ao "AI" genérico do texto, elevando seu total de 66 para 81 ocorrências — uma mistura indevida entre o "AI" como sujeito da frase e o "AI" como prefixo de um adjetivo composto distinto. Por determinação do usuário, essa regra foi substituída por uma **análise individual e auditável de cada forma hifenizada** (Seção 2), sem regra cega em nenhuma das duas direções. Foram adicionalmente implementadas: (i) desambiguação contextual de termos polissêmicos (Seção 4); (ii) proteção do bigrama institucional "State Council"; e (iii) expansão da normalização morfológica e do corte de Top 25 para **Top 50** (Seções 3 e 6).

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"Artificial Intelligence+"` / `"Artificial intelligence+"` (2 ocorrências) e `"AI+"` (9 ocorrências) unificados no rótulo `AI+` (11 ocorrências no total) | Sigla e forma por extenso designam exatamente o mesmo referente: o nome próprio da iniciativa/política. Mantido **separado** do termo genérico `AI` (66 ocorrências) porque os dois designam referentes distintos — a iniciativa nomeada vs. a tecnologia como campo (Seção 4). |
| `"State Council"` (4 ocorrências) protegido como bigrama único | Nome de instituição (o órgão administrativo central chinês, 国务院) — referente institucional próprio. Sem essa proteção, "state" apareceria solto no vocabulário, apesar de o documento nunca usar essa palavra em nenhum outro sentido (confirmado por concordância — Seção 4). |
| `"factors of production"` / `"relations of production"` / `"paradigms of production"` (6 ocorrências) protegidas como bigrama/trigrama único, rótulo `production (fatores/relações teóricas)` | Registro teórico-econômico de raiz marxista (生产力/生产关系 — "productive forces"/"relations of production"), distinto do sentido operacional de "production" (Seção 4). Fusão sob um único "production" indevidamente somaria dois referentes incompatíveis, exatamente o erro de polissemia não desambiguada identificado na versão anterior deste registro. |

## 2. Tokenização e auditoria de compostos com hífen

**Regra de tokenização adotada:** sequências de letras, preservando hífens internos como parte do token (`[A-Za-z]+(?:-[A-Za-z]+)*`) — um composto hifenizado é, por padrão, um único candidato a token, sujeito à auditoria abaixo. Isso substitui a antiga regra de "hífen = separador universal".

**Auditoria individual das 59 formas hifenizadas identificadas em `texto_completo`** (Skill 02_Análise_Vocab_A, item 4): nenhuma regra cega foi aplicada — cada forma foi avaliada quanto a manter-se unida (quando denota um conceito com identidade própria, ou quando a separação colidiria com sentidos distintos de uma das partes) ou separar-se (quando ambas as partes preservam, soltas, o mesmo sentido genérico já presente no texto). **Resultado: as 59 formas foram mantidas unidas** — nenhuma qualificou para separação, porque todas nomeiam um conceito, mecanismo de governança, categoria de política ou colocação fixa mais específico do que a soma de suas partes.

| Forma (freq.) | Categoria | Por que foi mantida unida |
|---|---|---|
| open-source (9) | Modelo de governança tecnológica | Eixo de comparação internacional relevante (Skill 02_Análise_Vocab_A, item 3) — o modelo chinês de código aberto é um mecanismo de governança distinto de outros modelos nacionais |
| human-computer (5) | Termo técnico | "human-computer symbiosis" — conceito próprio, não a soma de "human" + "computer" |
| high-quality (5), high-level (2), high-risk (1) | Categorias de política | Três colocações fixas com pesos temáticos distintos (qualidade, hierarquia/elite, risco); fundi-las sob "high" apagaria essa distinção |
| ai-driven (5), ai-native (5), ai-powered (1), ai-based (1), ai-enabled (1), intelligence-driven (1) | Família "impulsionado por IA" | Descritores técnicos fixos; soltar "driven"/"native" colidiria com sentidos não relacionados (Seção 4) e inflaria indevidamente o "AI" genérico (Seção 0) |
| decision-making (3) | Conceito de ciência política | Processo decisório como categoria própria; evita inflar "making" com um sentido não verbal |
| cross-sector (2), cross-modal (1), cross-industry (1), cross-disciplinary (1) | Prefixo "cross-" + domínio | Cada um nomeia um tipo específico de transversalidade |
| forward-looking (2), long-term (2), in-depth (1), real-time (1), on-site (1) | Colocações fixas | Unidades fixas do inglês de política pública; as partes soltas não preservam o sentido do composto |
| large-scale (2), ultra-large-scale (1) | Escala de sistemas/modelos | Mantidos como dois rótulos distintos — não sinônimos; "ultra-large-scale" denota um grau qualitativamente maior, categoria própria no debate sobre modelos de IA |
| scenario-based (2), platform-based (1), cloud-based (1), collaboration-based (1), contribution-based (1) | Sufixo "-based" | Cada um nomeia um modelo/abordagem específico; "based" solto (verbo "to base") tem sentido gramatical distinto |
| intelligentization-based (2) | Termo técnico chinês | Composto sobre o neologismo "intelligentization" (智能化) — ver Seção 4 sobre por que não se funde com "intelligent"/"smart" |
| supply-demand (2), risk-sharing (1) | Pareamento econômico | "supply-demand matching", "risk-sharing mechanisms" — conceitos econômico-financeiros próprios |
| province-level (1) | Nível de governo | Marcador de escala administrativa (central vs. provincial) |
| co-creation (1), self-directed (1), self-discipline (1) | Prefixo "co-"/"self-" | Conceitos de agência/colaboração distintos das raízes soltas |
| people-centered (1) | Filosofia de governança | Framing valorativo comparável a "human-centric" (usado, por ex., pela União Europeia) — eixo comparativo relevante |
| sector-specific (1), application-oriented (1), innovation-oriented (1) | Sufixo "-specific"/"-oriented" | Modificadores fixos de escopo/orientação |
| chinese-style (1) | Framing ideológico | "Chinese-style modernization" — categoria discursiva própria do documento |
| sixth-generation (1) | Geração tecnológica (6G) | Sentido de "geração" tecnológica (Seção 4) — não se confunde com sentido demográfico/energético (ausente neste documento) |
| e-commerce (1) | Substantivo composto padrão | Palavra composta consolidada no inglês |
| low-altitude (1) | Setor econômico específico | "low-altitude economy" — termo de política setorial chinês específico |
| brain-computer (1) | Termo técnico | "brain-computer interface" — tecnologia específica |
| well-being (1) | Substantivo composto padrão | Palavra composta consolidada no inglês |
| resource-rich (1), cost-effective (1) | Adjetivos compostos | Modificadores fixos |
| whole-process (1) | Conceito de governança regulatória | "whole-process oversight" — escopo regulatório integral |
| air-space-ground-sea (1) | Domínio multi-espacial | Composto de quatro elementos nomeando um único conceito de integração multidomínio; fragmentá-lo destruiria o conceito |
| multi-element (1), multi-path (1) | Prefixo "multi-" | Modificadores fixos de pluralidade estrutural |
| win-win (1) | Idioma diplomático-econômico | "win-win cooperation" — expressão fixa característica do discurso de política externa chinês |
| east-west (1) | Nome de projeto/eixo geográfico | "East-West Compute Transfer" — nome de hub nacional de infraestrutura, referente próprio |
| trial-and-error (1) | Idioma metodológico | Expressão fixa, não a soma de "trial" + "and" + "error" |
| industry-education (1) | Política educacional chinesa | "industry-education integration" — termo de política real e específico |
| human-provided (1) | Contraste com automação | Distingue serviços humanos de serviços automatizados/por IA — distinção central ao documento |
| black-box (1) | Termo de governança de IA | "black-box models" — categoria de interpretabilidade consolidada |
| state-owned (1) | Categoria econômica | "state-owned capital" — categoria de propriedade econômica (Seção 4) |

## 3. Duas operações distintas: remoção e normalização

**(a) Remoção (exclusão):** artigos, preposições, conjunções, pronomes, verbos auxiliares/modais e conectores discursivos genéricos do inglês (lista integral abaixo), tokens de um único caractere, numerais romanos estruturais dos cabeçalhos (`ii`/`iii`/`iv`).

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

Adicionalmente removidos: tokens de um único caractere (resíduos de `&`, compostos letra-dígito, possessivos e numerais entre aspas); numerais romanos estruturais dos cabeçalhos de seção (`i`/`ii`/`iii`/`iv`).

**Não removido, por decisão deliberada:** os verbos diretivos que estruturam cada item de ação do documento (ex.: *promote*, *strengthen*, *accelerate*, *build*, *explore*, *encourage*, *establish*, *optimize*) foram mantidos, por carregarem sinal analítico legítimo sobre a "gramática de ação" do documento.

**(b) Normalização/agrupamento morfológico — cobertura ampliada para o corte de Top 50 (Skill 02_Análise_Vocab_A, item 6).** Em relação à versão anterior (que cobria apenas os pares já presentes no Top 25), esta revisão levantou exaustivamente os pares singular/plural e famílias verbais entre os ~150 tokens mais frequentes do documento.

*Substantivos singular/plural (43 grupos):* application, models, services, systems, capabilities, industry, products, resources, technology, talent, risks, levels, agents, initiatives, sectors, structures, processes, policies, ecosystems, evaluations, platforms, approach — **(já existentes)** — mais, **novos nesta revisão:** governments, commissions, forces, transformations, advantages, scenarios, achievements, breakthroughs, sciences, architectures, chains, operations, jobs, environments, students, roles, humans, rights, incentives, networks, investments, laws.

*Conjugações verbais (25 famílias):* promote, strengthen, accelerate, support, build, develop, create, establish, improve, enhance, explore, encourage, deepen, optimize, implement — **(já existentes)** — mais, **novas nesta revisão:** learn, empower, exploit, focus, foster, fund, grow, help, launch, work.

*Siglas / expressões compostas:* `AI+` ⟷ `Artificial Intelligence+`; `open-source` (unidade composta); `State Council` (bigrama institucional).

## 4. Desambiguação contextual de termos polissêmicos/homônimos (Skill 02_Análise_Vocab_A, item 5)

Cada termo abaixo foi verificado por concordância (contexto de todas as suas ocorrências no texto) antes de entrar na contagem final:

| Termo | Sentidos identificados | Decisão |
|---|---|---|
| AI (66) / AI+ (11) | "AI" = tecnologia/campo genérico, em todas as ocorrências soltas; "AI+" = nome próprio da iniciativa política, sempre entre aspas ou como prefixo dos seis subtítulos da Parte II | Mantidos **separados** |
| generation | Toda ocorrência solta de "generation" tem sentido de "nova geração" tecnológica (ex.: "new generation smart terminal devices", 5x); "sixth-generation" (mobile communications/6G) confirma o mesmo sentido. **Nenhuma ocorrência no sentido de geração de energia/eletricidade foi encontrada** | Verificado e **não desdobrado** — sentido único confirmado por concordância |
| state | As 5 ocorrências são "State Council" (nome de instituição, 4x) ou parte do composto "state-owned" (1x). **Nenhuma ocorrência no sentido de "estado subnacional"** (o par polissêmico do documento dos EUA não se aplica aqui) | "State Council" protegido como bigrama; "state-owned" mantido como composto; não há "state" genérico solto neste texto |
| power | Única ocorrência: "computing power ('compute')" — sentido de capacidade computacional | Sentido único confirmado, sem necessidade de desdobramento |
| production (11 no total antes do desdobramento) | 6 ocorrências no registro teórico-econômico marxista ("factors/relations/paradigms of production", 生产力/生产关系); 5 ocorrências no sentido operacional ("design, pilot testing, production...", "agricultural production", "cultural production") | **Desdobrado** em `production (fatores/relações teóricas)` (6) e `production` (5) — mesmo tipo de erro que a fusão indevida de compostos, agora corrigido também para este termo |
| open (4) / opening (2) / openings (1) | "open" = adjetivo ("open ecosystem/cooperation", abertura/acessibilidade); "opening" = verbo/gerúndio idiomático "opening up" (expandir/liberalizar novos setores); "openings" = substantivo, "job openings" (vagas de emprego) — três referentes distintos | Mantidos os três **completamente separados** |
| major (3) / majors (1) | "major" = adjetivo ("major growth pole" — significativo); "majors" = substantivo ("academic majors" — áreas de formação) | Mantidos **separados** |
| process(es) (6) / processing (4) | "process"/"processes" = substantivo, procedimento; "processing" = ação técnica sobre dados ("data processing") | Mantidos **separados**, mesma lógica de "development"/"develop" |
| share (1) / shared (1) / sharing (4) | "share" = verbo ("share in the benefits" — participar/beneficiar-se); "shared" = adjetivo ("shared datasets" — de uso comum); "sharing" = substantivo/gerúndio ("openness and sharing" — prática de compartilhamento aberto) | Mantidos **separados** |
| lead (1) / leading (2) | "lead" = verbo idiomático ("take the lead" — estar à frente); "leading" = adjetivo ("leading talents" — talentos de elite) | Mantidos **separados** |
| play (1) / playing (1) | "play" = idioma ("give full play to" — dar pleno efeito a); "playing" = verbo ("playing its role" — exercendo seu papel) | Mantidos **separados**, por cautela metodológica |
| lives (1) / living (1) | "lives" = substantivo ("fulfilling lives" — qualidade de vida pessoal); "living" = substantivo ("production and living" — subsistência/vida cotidiana) | Mantidos **separados** |
| intelligent (32) / intelligentization (5) / intelligentized (6) / smart (15) | Quatro itens lexicais distintos do mesmo campo semântico — adjetivo, substantivo (neologismo chinês), particípio/adjetivo e sinônimo não-cognato | Mantidos **separados** — princípio geral de não fusão de quase-sinônimos (Skill 02_Análise_Vocab_A, item 5) |
| driven (composto) / drive, drives, driving (verbo) | "driven" ocorre exclusivamente dentro de compostos hifenizados, nunca como verbo finito | Mantidos **separados** |
| development (37) / develop (verbo) | Substantivo vs. verbo — variação derivacional, não flexional | Mantidos **separados** |
| capacity / capability, capabilities | Quase-sinônimos em português, lemas distintos em inglês | Mantidos **separados** |
| compute (9) / computing (3) | "compute" = substantivo de massa autônomo; "computing" = modificador atributivo | Mantidos **separados** (dúvida real, critério conservador) |
| security (9) / safety (3) | Palavras distintas do inglês | Mantidos **separados** |

## 5. Bigramas essenciais tratados como unidade

| Bigrama | Grafia no texto | Ocorrências | Justificativa |
|---|---|---|---|
| Artificial Intelligence+ / AI+ | Espaço (forma extensa) e sem espaço (sigla) | 11 (2+9) | Nome próprio da iniciativa (Seção 1) |
| open-source | Hífen | 9 | Modelo de governança tecnológica, eixo comparativo do projeto (Seção 2) |
| State Council | Espaço | 4 | Nome de instituição (Seção 1) |
| factors/relations/paradigms of production | Espaço | 6 | Registro teórico-econômico marxista, distinto do sentido operacional de "production" (Seção 4) |

## 6. Critério de corte

**Top 50** termos por frequência absoluta (critério padrão da Skill 02_Análise_Vocab_A, item 6), com o **Top 25** mantido como recorte adicional dentro do mesmo Top 50. Frequência absoluta (não relativa) é apropriada por se tratar de análise interna a um único documento — a normalização relativa entre documentos de tamanhos distintos é exigida apenas na pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B), que não se aplica aqui.

## 7. Correção de consistência entre documentos (auditoria da Análise Conjunta, 2026-08-05)

Antes da análise comparada de similaridade na pasta "Análise Conjunta", a Skill 02_Análise_Vocab_B (item 3) exige verificar se o mesmo bigrama recebe o mesmo tratamento em todos os documentos comparados. A auditoria identificou que "Research and Development"/"R&D" ocorre 4 vezes em `texto_completo` (usualmente como "R&D", nas seções sobre financiamento e infraestrutura de pesquisa), sem estar protegido como bigrama — permanecendo fragmentado em "research" (token genérico, absorvido pela normalização morfológica de `technology`-adjacentes) e a sigla solta "r"/"d" (já descartada como resíduo de formatação). Como "Research & Development (R&D)" é bigrama protegido no PBIA (27 ocorrências) e passou a ser protegido também em `new_generation.json` e `americas_ai_action_plan.json` (ver correção equivalente nos respectivos registros), a ausência de proteção aqui quebraria a comparabilidade do termo entre os documentos do projeto.

**Correção aplicada:** adicionado o padrão `\bResearch and Development\b|\bR&D\b` → `RESEARCHDEVTOKEN` ao `preprocess()` de `ai_plus.ipynb`, com o mesmo rótulo representativo do PBIA ("Research & Development (R&D)"). O notebook foi reexecutado; o termo agora conta 4 ocorrências sob rótulo próprio (abaixo do corte de Top 50 deste documento, mas corretamente identificável e comparável).

## 8. Histórico de atualizações

- **2026-08-05 (criação):** metodologia inicial aplicada (pré-processamento, tokenização com hífen como separador, remoção, normalização, corte Top 25), gráfico de barras horizontais no notebook `ai_plus.ipynb`.
- **2026-08-05 (revisão metodológica):** correção da fragmentação por hífen (auditoria individual de 59 formas, todas mantidas unidas — Seção 2), desambiguação contextual de termos polissêmicos (Seção 4), proteção do bigrama "State Council" (Seção 1), expansão da normalização morfológica e do corte para Top 50 (Seções 3 e 6). Alterações determinadas pelo usuário para toda a pasta "Análise Documentos IA" (Brasil, China, Estados Unidos, Europa) e replicadas nas Skills 02_Análise_Vocab_A/B.
- **2026-08-05 (correção de consistência entre documentos):** adicionada proteção do bigrama "Research & Development (R&D)" (Seção 7), motivada pela auditoria de consistência exigida antes da análise comparada da pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B, item 3).
