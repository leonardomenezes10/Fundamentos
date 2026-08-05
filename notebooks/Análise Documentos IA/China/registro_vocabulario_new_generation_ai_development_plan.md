# Registro de Análise de Vocabulário — new_generation_ai_development_plan.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 8), associado ao documento `new_generation_ai_development_plan.json` (State Council Notice on the Issuance of the New Generation Artificial Intelligence Development Plan, China, 2017). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês (tradução publicada pela New America/DigiChina; o documento original é em chinês).
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05 — revisão metodológica completa determinada pelo usuário (correção da fragmentação por hífen, tratamento de bigramas essenciais, desambiguação contextual de termos polissêmicos e expansão do corte para Top 50).

## 0. Correção metodológica aplicada nesta revisão

A versão anterior tratava **todo hífen como separador universal**, sem nenhuma exceção. Isso fragmentava compostos altamente relevantes deste documento — a própria versão anterior já registrava, como limitação, que "decision-making" se fragmentava em 23 ocorrências de "decision"+"making", que "high-end"/"high-level" inflavam artificialmente o token solto "high" (que chegou a 53 ocorrências, 20º lugar no corte anterior), que "brain-inspired" inflava "brain" (23) e que "open-source" inflava "open" (30). Essa regra cega foi substituída por uma **auditoria individual de cada uma das 136 formas hifenizadas** identificadas no texto (Seção 2). Foram também implementadas: (i) desambiguação contextual de termos polissêmicos, incluindo dois casos genuínos de referentes distintos sob a mesma grafia — "power" (nacional/geopolítico vs. nuclear/energético) e "driving"/"drive"/"driven" (condução autônoma vs. força motriz/impulso figurado) —, além da confirmação de que "generation" e "state" têm sentido único neste documento; (ii) proteção do bigrama institucional "State Council"; e (iii) expansão da normalização morfológica e do corte de Top 25 para **Top 50**.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"artificial intelligence"` (case-insensitive) → `"AI"` | Sigla e forma por extenso designam exatamente o mesmo referente. Ocorre apenas 3x no texto corrido; a partir daí o documento usa exclusivamente "AI". |
| `"State Council"` (4 ocorrências) protegido como bigrama único | Nome de instituição — mesmo tratamento aplicado no documento `ai_plus.json` deste projeto. |
| `"nuclear power"` (1 ocorrência) protegido como bigrama único, rótulo `power (nuclear/energia)` | Desambiguação contextual (Seção 4) — sentido energético, distinto do uso geopolítico de "power" no restante do documento. |
| `"driving force"`, `"driving effect"`, `"driving role"`, `"driving networks"` (5 ocorrências), e as formas verbais soltas `"drive"` (2) e `"driven"` (1) protegidas sob o rótulo `driving/drive (força motriz)` | Desambiguação contextual (Seção 4) — sentido figurado de impulso/propulsão, distinto do sentido literal de condução autônoma de veículos que domina as demais 13 ocorrências de "driving". |
| `"co-ordination"` (1 ocorrência, grafia britânica) → `"coordination"` | Variante ortográfica do mesmo termo (mesmo referente, mesma língua) — normalização de grafia, não composto distinto. |
| `"rain-inspired"` (1 ocorrência) → `"brain-inspired"` | Artefato mecânico de extração/OCR do documento-fonte (falta a letra inicial "b"): todas as 19 ocorrências de "rain-inspired"/"brain-inspired" descrevem, de forma intercambiável e no mesmo parágrafo, o mesmo conceito técnico ("brain-inspired intelligence computing theory"). Tratado como variante de grafia do mesmo termo, não como segundo conceito — o arquivo-fonte (`texto_completo`) permanece inalterado; a normalização ocorre apenas nesta camada de análise de vocabulário. |

## 2. Tokenização e auditoria de compostos com hífen

**Regra de tokenização:** sequências de letras, preservando hífens internos como parte do token (`[A-Za-z]+(?:-[A-Za-z]+)*`) — substitui a antiga regra de "hífen = separador universal".

**Auditoria das 136 formas hifenizadas identificadas em `texto_completo`.** Das 136, 2 foram resolvidas como variantes de grafia/extração do mesmo termo já existente (Seção 1: "co-ordination"→"coordination", "rain-inspired"→"brain-inspired"). As **134 formas restantes foram mantidas unidas** — nenhuma qualificou para separação em suas palavras componentes, pelo mesmo critério do documento `ai_plus.json`: todas nomeiam um conceito técnico, uma categoria de política ou uma colocação fixa mais específica do que a soma das partes. Organizadas tematicamente para auditabilidade:

| Categoria | Formas (frequência) |
|---|---|
| Decisão/governança | decision-making (23) |
| Neurociência computacional | brain-inspired (18, +1 grafia "rain-inspired" — total 19), brain-machine (1) |
| Interação humano-máquina | human-machine (16), human-machine-object (3), human-computer (2), human-like (1), man-machine (2), human-in-the-loop (1) |
| Categorias de qualidade/hierarquia/desempenho ("high-X", mantidos distintos entre si) | high-end (17), high-performance (8), high-level (7), high-quality (3), high-tech (2), high-efficiency (2), high-dimensional (1), high-bitrate (1), high-energy (1), high-sensitivity (1), high-precision (1), high-throughput (1) |
| Transversalidade ("cross-X") | cross-medium (10), cross-media (6), cross-domain (3), cross-disciplinary (2), cross-sectoral (2), cross-integration (1), cross-language (1) |
| Pluralidade estrutural ("multi-"/"all-") | multi-domain (2), multi-disciplinary (2), multi-dimensional (2), multi-model (1), multi-source (1), multi-data (1), multi-style (1), multi-language (1), multi-intelligent (1), multi-field (1), multi-energy (1), multi-level (1), multi-sided (1), multi-billion-scale (1), all-element (2), all-factor (1), all-encompassing (1), multiple-channel (1) |
| Autonomia/agência ("self-"/"co-") | self-driving (2), self-adaptive (1), self-preservation (1), self-discipline (1), co-construction (1) |
| Descritores "-driven"/"-oriented"/"-based"/"-led"/"-centered"/"-deployed" | data-driven (5), knowledge-driven (3), innovation-driven (1), technology-led (1), industry-leading (1), problem-oriented (1), service-oriented (1), data-oriented (1), space-oriented (1), space-based (1), knowledge-based (1), learner-centered (1), people-centric (1), market-dominant (1), precision-deployed (1) |
| Escala/geração tecnológica | new-generation (4), next-generation (2), new-type (2), new-model (2), innovation-style (1), large-scale (8), mid-size (2), mid-sized (1), full-scale (1), small-sample (1), large-landscape (1) |
| Marcadores temporais/técnicos | long-term (6), real-time (6), short-distance (1), long-distance (1), three-year (1), already-deployed (1), follow-up (1), front-line (1), on-board (1) |
| Termos técnicos/econômicos consolidados | internet-based (1), quantum-accelerated (1), semi-supervised (1), built-in (1), open-source (7), open-style (1), start-up (2), first-mover (2), world-leading (4), far-sighted (2), far-sightedly (1), far-reaching (1), cutting-edge (1), mega-projects (2), general-purpose (1), special-purpose (1), intelligence-based (1), ai-based (1), ai-related (4), deep-sensing (1), real-world (1) |
| Militar/geográfico | military-civilian (5), military-civil (1), civil-military (1), anti-terrorism (1), beijing-tianjin-hebei (1, topônimo/megarregião) |
| Diversos, baixa frequência | chain-style (1), three-dimensional (2), two-way (2), two-tiered (1), low-cost (2), low-energy (1), low-power (1), low-latency (1), highly-dynamic (1), point-like (1), phase-type (1), word-concept (1), group-sharing (1), information-sharing (1), audio-visual (1), national-level (1), protection-related (1), re-employment (1), computing-fronted (1), made-to-order (3), tens-of-millions (1) |

## 3. Duas operações distintas: remoção e normalização

**(a) Remoção:** mesma lista de palavras funcionais do inglês já usada neste projeto (artigos, preposições, conjunções, pronomes, verbos auxiliares/modais, conectores discursivos genéricos), mais tokens de um único caractere (resíduo de possessivos, ex. "China's").

**(b) Normalização morfológica — cobertura ampliada para Top 50.** Em relação à versão anterior (30 grupos de substantivos, 18 famílias verbais), esta revisão manteve os grupos já existentes e acrescentou:

*Novos pares singular/plural (29):* network(s), demand(s), discipline(s), domain(s), plan(s), change(s), structure(s), risk(s), cluster(s), force(s), advantage(s), reform(s), livelihood(s), chain(s), team(s), center(s), framework(s), engine(s), sensor(s), counterpart(s), architecture(s), vehicle(s), market(s), terminal(s), trial(s), solution(s), organization(s), assistant(s), program(s), incentive(s).

*Famílias verbais:* mantidas as 18 já existentes (strengthen, promote, establish, develop, construct, build, accelerate, encourage, improve, achieve, enhance, form, launch, focus, integrate, coordinate, lead, create) — nenhuma família nova identificada com risco de POS/sentido divergente que justificasse inclusão.

## 4. Desambiguação contextual de termos polissêmicos/homônimos (Skill 02_Análise_Vocab_A, item 5)

| Termo | Sentidos identificados (verificados por concordância) | Decisão |
|---|---|---|
| power (6 no total antes do desdobramento) | 5 ocorrências no sentido geopolítico/nacional ("global power in science and technology", "comprehensive national power", "an economic power"); 1 ocorrência no sentido energético ("nuclear power security operations") | **Desdobrado** em `power (nacional/geopolítico)` (5) e `power (nuclear/energia)` (1, via bigrama "nuclear power" — Seção 1) |
| driving / drive / driven (21 no total antes do desdobramento, excluindo os hifenizados "self-driving") | 13 ocorrências no sentido literal de condução autônoma/veicular ("automatic driving", "autonomous driving", "human-machine joint driving technology"); 8 ocorrências no sentido figurado de força motriz/impulso ("driving force", "driving effect", "driving role", "driving networks", "Drive comprehensive elevation", "drive industries to migrate", "as driven by the scale of related industries") | **Desdobrado** em `driving (condução autônoma)` (13) e `driving/drive (força motriz)` (8) |
| generation | Todas as 27 ocorrências soltas de "generation" (fora dos compostos "new-generation"/"next-generation", já hifenizados e mantidos unidos) têm sentido de geração tecnológica/temporal (ex.: "a new generation of AI", "fifth generation mobile communication (5G)") | Verificado e **não desdobrado** — sentido único confirmado |
| state | As 4 ocorrências são todas "State Council" (nome de instituição) | Bigrama protegido (Seção 1); não há "state" genérico solto neste texto |
| smart (82) / intelligent (121) / intelligence (57) / intelligentization (13) | Herdado da versão anterior deste registro: quatro itens lexicais distintos — "smart"/"intelligent" são sinônimos de tradução usados de forma alternada pelos tradutores (não flexões do mesmo lema); "intelligence" é substantivo; "intelligentization" é neologismo próprio (智能化) | Mantidos **separados** — princípio geral de não fusão de quase-sinônimos (Skill 02_Análise_Vocab_A, item 5) |
| development / develop | Substantivo vs. verbo — derivacional | Mantidos **separados** (herdado) |
| research (104) / researching (12) | Substantivo vs. função gramatical distinta | Mantidos **separados** (herdado) |
| support (68) / supporting, supports | Uso misto substantivo/verbo | Mantidos **separados** (herdado) |
| enhance/enhancing (32) / enhanced (16) | "enhanced" é parte do termo técnico fixo "hybrid (and) enhanced intelligence" | Mantidos **separados** (herdado) |
| building | Uso misto gerúndio/substantivo (edificações físicas) | Mantido **fora** da família verbal "build" (herdado) |
| process (4) / processing (12) | "processing" funciona como núcleo de termos técnicos fixos ("natural language processing") | Mantidos **separados** (herdado) |
| share (1) / sharing (15) | Sentidos financeiro vs. de compartilhamento aberto | Mantidos **separados** (herdado) |
| bases (12) | Verificado: sentido consistente de "polo/centro institucional", nunca sentido militar | Mantido agrupado com "base" (herdado, confirmado nesta revisão) |

## 5. Bigramas essenciais tratados como unidade

| Bigrama | Ocorrências | Justificativa |
|---|---|---|
| State Council | 4 | Nome de instituição |
| nuclear power | 1 | Desambiguação de "power" (Seção 4) |
| driving force / driving effect / driving role / driving networks | 5 | Desambiguação de "driving" (Seção 4) |

## 6. Critério de corte

**Top 50** termos por frequência absoluta (critério padrão da Skill 02_Análise_Vocab_A, item 6), com o **Top 25** mantido como recorte adicional. Frequência absoluta é apropriada por se tratar de análise de um único documento.

## 7. Limitações metodológicas remanescentes

- **Texto de partida é uma tradução** (New America/DigiChina), não o original em chinês — limitação estrutural inerente ao protocolo da Skill02, não introduzida por esta revisão.
- **"smart"/"intelligent" seguem não fundidos**, apesar de indícios de uso intercambiável pelos tradutores — fundi-los exigiria julgamento de equivalência conceitual entre sinônimos de tradução, não autorizado pela Skill (que exige identidade de referente **e** de forma lexical).
- **Cobertura da normalização morfológica e da desambiguação contextual concentrada nos candidatos plausíveis ao Top 50** (frequência bruta aproximada ≥ 3-5) — não há lematização/desambiguação exaustiva de toda a cauda longa de 1.611 termos distintos do vocabulário final.
- **Duas substituições de grafia/extração aplicadas nesta camada de análise** ("co-ordination"→"coordination", "rain-inspired"→"brain-inspired") — decisões documentadas e reversíveis, mas dependentes de leitura manual da concordância, não de uma regra automática generalizável a outros documentos sem inspeção equivalente.

## 8. Histórico de atualizações

- **2026-08-05 (criação):** metodologia inicial (pré-processamento, tokenização com hífen como separador, remoção, normalização, corte Top 25 com ajuste de empate em 26 termos).
- **2026-08-05 (revisão metodológica):** correção da fragmentação por hífen (auditoria de 136 formas, 134 mantidas unidas — Seção 2), desambiguação contextual de "power" e "driving"/"drive"/"driven" (Seção 4), proteção do bigrama "State Council", normalização de duas variantes de grafia/extração, expansão da normalização morfológica (29 novos pares) e do corte para Top 50. Alterações determinadas pelo usuário para toda a pasta "Análise Documentos IA" (Brasil, China, Estados Unidos, Europa) e replicadas nas Skills 02_Análise_Vocab_A/B.
