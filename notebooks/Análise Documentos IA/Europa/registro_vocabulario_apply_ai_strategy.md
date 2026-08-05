# Registro de Análise de Vocabulário — apply_ai_strategy.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 8), associado ao documento `apply_ai_strategy.json` (Apply AI Strategy, União Europeia). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês (variante britânica do inglês institucional da UE).
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05 — revisão metodológica completa determinada pelo usuário (correção da fragmentação por hífen, tratamento de bigramas essenciais, desambiguação contextual de termos polissêmicos e expansão do corte para Top 50).

## 0. Correção metodológica aplicada nesta revisão

A versão anterior tratava **todo hífen não coberto pelos cinco compostos institucionais já protegidos como separador universal** (regra explícita: "'cross-border' → 'cross' + 'border'; 'AI-powered' → 'AI' + 'powered'; 'open-source' → 'open' + 'source'"). Essa regra foi substituída por uma **auditoria individual de cada uma das 76 formas hifenizadas** identificadas no texto (Seção 2). Foi também descoberta uma polissemia genuína, ainda que de baixa frequência: **"power"**, quando usado solto, mistura sentido computacional ("computing power"), abstrato/preditivo ("predictive power") e energético/verbal ("power robots and machines"). Adicionalmente, foi corrigida a limitação já apontada e não resolvida na versão anterior — **"actions"/"alliance" misturavam vocabulário genérico com componentes de nomes próprios** ("AI Continent Action Plan", "Security Action for Europe", "Automotive Action Plan", "Apply AI Alliance", "European Connected and Autonomous Alliance") — usando o sinal de maiúscula (confirmado por concordância: toda ocorrência de "Action"/"Alliance" capitalizados no meio da frase pertence a um nome próprio; toda ocorrência minúscula é vocabulário genérico). Foram também expandidas a normalização morfológica e o corte de Top 25 para **Top 50**.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

Mantido integralmente da versão anterior, com dois acréscimos:

| Operação | Justificativa |
|---|---|
| `"Artificial Intelligence"` → `"AI"` (2); `"Artificial General Intelligence"` (AGI) **excluída** desta fusão | AGI é conceito distinto por definição do próprio texto (herdado). |
| `"European Union"` → `"EU"` (1); `"Member States"` → composto (13, ver Seção 4); `"digital twin(s)"` → composto (6); `"AI Act"` → composto (13) | Herdado, ver histórico. |
| Isolamento do substantivo "building" (1 ocorrência não gerúndio) | Herdado — ver Seção 4 do registro anterior a esta revisão. |
| **[Novo]** `"computing power"` (1 ocorrência) protegida, rótulo `power (computacional)` | Desambiguação contextual — capacidade computacional, referente distinto de energia e de capacidade preditiva/abstrata. |
| **[Novo]** `"predictive power"` (1 ocorrência) protegida, rótulo `power (capacidade preditiva/abstrata)` | Desambiguação contextual — força preditiva de simulações/modelos, um terceiro referente distinto. |
| **[Novo]** `"Action"` capitalizado (7 ocorrências) protegido, rótulo `Action (nome de plano/programa)` | Todas as 7 ocorrências capitalizadas pertencem a nomes próprios de planos/programas ("AI Continent Action Plan" ×5, "Security Action for Europe" ×1, "Automotive Action Plan" ×1); as 5 ocorrências minúsculas de "action" e as 11 de "actions" permanecem como vocabulário genérico (Seção 4). |
| **[Novo]** `"Alliance"` capitalizado (8 ocorrências) protegido, rótulo `Alliance (nome próprio de entidade)` | Todas as 8 ocorrências capitalizadas pertencem a nomes próprios de entidades ("Apply AI Alliance", "the existing AI Alliance", "European Connected and Autonomous (Vehicle) Alliance"); as 2 ocorrências minúsculas de "alliances" permanecem como vocabulário genérico (Seção 4). |

## 2. Tokenização e auditoria de compostos com hífen

**Regra de tokenização:** sequências de letras (e `_` para os cinco compostos institucionais protegidos), preservando hífens internos como parte do token (`[A-Za-z]+(?:-[A-Za-z]+)*`) — substitui a antiga regra de "hífen = separador universal para tudo que não estivesse protegido".

**Auditoria das 76 formas hifenizadas identificadas em `texto_completo`.** Todas foram mantidas unidas — nenhuma qualificou para separação. Organizadas tematicamente:

| Categoria | Formas (frequência) |
|---|---|
| Descritores "AI-X" | ai-based (10), ai-powered (8), ai-enabled (4), ai-ready (2), ai-driven (1), ai-enhanced (1), ai-generated (1), ai-related (1), environment-ai (1) |
| Ecossistema aberto/técnico geral | general-purpose (6), open-source (2), use-cases (1), end-user (1), fine-tune (1), non-discrimination (1) |
| Escala/qualidade/desempenho | real-world (6), high-quality (5), cutting-edge (4), large-scale (2), high-impact (1), high-tech (1), high-technology (1), high-risk (1), high-resolution (1), full-scale (1), wide-scale (1), world-class (1), lower-cost (1), cost-effective (1) |
| Transversalidade "cross-X" | cross-cutting (3), cross-border (3) |
| Processo decisório | decision-making (3), problem-solving (2), step-by-step (1), what-if (1) |
| Termos/nomes europeus específicos | agri-food (2), european-made (2), pan-european (1), eu-owned (1), eu-wide (1) |
| Geração tecnológica | next-generation (2) |
| "-specific"/"-related" | sector-specific (1), industry-specific (1), gender-specific (1), healthcare-related (1), defence-relevant (1), digital-intense (1) |
| Diversos técnicos | e-commerce (1), multi-disciplinary (1), post-deployment (1), human-robot (1), co-finances (1), in-orbit (1), on-orbit (1), space-based (1), fast-changing (1), self-healing (1), dual-use (1), self-driving (1), point-to-point (1), demand-side (1), data-sharing (1), cloud-edge-iot (1), early-warning (1), ground-breaking (1), earth-system (1), user-engagement (1), micro-studios (1), micro-credentials (1), sub-configuration (1), non-state (1), innovation-friendly (1), like-minded (1), top-down (1), co-evolution (1), mid-caps (1) |

## 3. Duas operações distintas: remoção e normalização

**(a) Remoção:** mesma lista de palavras funcionais do inglês já usada neste projeto.

**(b) Normalização morfológica — cobertura ampliada para Top 50.** Mantidos os 68 grupos de substantivos e as 34 famílias verbais já existentes; acrescentados nesta revisão:

*Novos pares singular/plural (9):* source(s), programme(s), impact(s), operation(s), change(s), communication(s), advance(s), training(s), user(s).

*Novas famílias verbais (2):* remain (remain/remains/remaining/remained), focus-verbo (focus/focuses/focusing/focused — mantido como família verbal distinta do substantivo "focus", que não ocorre isoladamente como núcleo nominal relevante neste documento).

## 4. Desambiguação contextual de termos polissêmicos/homônimos (Skill 02_Análise_Vocab_A, item 5)

| Termo | Sentidos identificados (por concordância) | Decisão |
|---|---|---|
| power (4 ocorrências soltas antes do desdobramento, excluindo o falso-positivo "em[[power]]" = "empower", palavra distinta) | "computing power capacities" (computacional, 1); "predictive power" de simulações (capacidade preditiva/abstrata, 1); "power robots and machines used for field work" (verbo, sentido energético — energizar/acionar maquinário, 1) | **Desdobrado em três rótulos**: `power (computacional)` (1), `power (capacidade preditiva/abstrata)` (1), `power (energia)` (1) |
| generation | Única ocorrência solta ("personalise content generation") tem sentido de geração de conteúdo por IA; as 2 ocorrências do composto "next-generation" (mantido unido, Seção 2) têm sentido de geração tecnológica. **Nenhuma ocorrência no sentido de geração de energia elétrica.** | Verificado e **não desdobrado** — sentidos já compatíveis entre si (tecnológico), sem conflito |
| state (1) / states (13, todas "Member States") | "state" solto ocorre 1 vez ("by state and non-state actors" — "non-state" já é composto hifenizado protegido); todas as 13 ocorrências de "states" são parte de "Member States" | Bigrama "Member States" protegido (herdado); resíduo "state" mantido em grupo próprio, sem ocorrências genéricas de "states" remanescentes |
| action (5) / actions (11) / Action (7, nome de plano) | "action"/"actions" minúsculos = vocabulário genérico de política pública; "Action" maiúsculo = componente de nome próprio de plano ("AI Continent Action Plan" etc.) | **Desdobrado**: `action`/`actions` (genérico, mantidos no grupo "actions" normal) e `Action (nome de plano/programa)` (7) |
| alliance (0 genérico) / alliances (2) / Alliance (8, nome próprio) | "alliances" minúsculo = vocabulário genérico ("universities alliances", "partnerships and alliances"); "Alliance" maiúsculo = nome próprio de entidade (Apply AI Alliance, European Connected and Autonomous Alliance) | **Desdobrado**: `alliances` (genérico) e `Alliance (nome próprio de entidade)` (8) |
| European / EU / Europe; development/develop; security/secure; strategy/strategic; economy/economic; industry/industrial; sovereignty/sovereign; governance/government(s); innovation(s)/innovative; AI/AGI; intelligence (fora do bigrama) | Pares derivacionais, de classe gramatical distinta, ou conceitos distintos por definição do próprio texto | Mantidos **separados** (herdados desta versão, reconfirmados) |

## 5. Bigramas essenciais tratados como unidade

| Bigrama | Ocorrências | Justificativa |
|---|---|---|
| European Union / EU | 52 (1 + 51 soltos; caiu de 54 nesta revisão porque "eu-owned" e "eu-wide", agora compostos hifenizados próprios, deixaram de contribuir "eu" ao bigrama) | Herdado, contagem recalculada |
| Member States | 13 | Herdado |
| digital twin(s) | 6 | Herdado |
| AI Act | 13 | Herdado |
| computing power | 1 | Desambiguação de "power" (Seção 4) |
| predictive power | 1 | Desambiguação de "power" (Seção 4) |
| AI Continent Action Plan / Security Action for Europe / Automotive Action Plan | 7 | Nomes próprios de planos/programas (Seção 1/4) |
| Apply AI Alliance / (existing) AI Alliance / European Connected and Autonomous (Vehicle) Alliance | 8 | Nomes próprios de entidades (Seção 1/4) |

## 6. Critério de corte

**Top 50** termos por frequência absoluta (critério padrão da Skill 02_Análise_Vocab_A, item 6), com o **Top 25** mantido como recorte adicional. Frequência absoluta é apropriada por se tratar de análise de um único documento.

## 7. Limitações metodológicas remanescentes

- **Cobertura da normalização morfológica e da desambiguação contextual concentrada nos candidatos plausíveis ao Top 50** — não há varredura exaustiva de toda a cauda longa de 1.493 termos distintos do vocabulário final.
- **Empates na fronteira do corte** (herdado): a ordem entre termos empatados é definida apenas pela ordem de primeira ocorrência no texto (comportamento determinístico do `Counter.most_common()`), sem significado semântico adicional — válido também para o novo corte de Top 50.
- **"European"/"EU"/"Europe" seguem não fundidos**, por representarem classes gramaticais e referentes distintos (herdado).

## 9. Correção de consistência entre documentos (auditoria da Análise Conjunta, 2026-08-05)

Antes da análise comparada de similaridade na pasta "Análise Conjunta", a Skill 02_Análise_Vocab_B (item 3) exige verificar se o mesmo bigrama recebe o mesmo tratamento em todos os documentos comparados. A auditoria identificou que **"public sector" ocorre 12 vezes** em `texto_completo` — nenhuma delas protegida como bigrama. É o caso de maior magnitude relativa encontrado em toda a auditoria: 12 ocorrências em um documento de 4.654 tokens de conteúdo (proporcionalmente mais denso que o "Private Sector" da EUA ou o "Public Sector" do PBIA) ficavam inteiramente fragmentadas em "public" (token solto, sem qualquer normalização) + "sector" (absorvido pelo bucket genérico `sectors`, junto com qualquer outro uso de "sector" no documento). Como "public sector" é bigrama institucional protegido tanto no PBIA (19 ocorrências) quanto em `ai_continent_action_plan.json` (18 ocorrências, o documento europeu irmão deste), a ausência de proteção aqui era a inconsistência de maior impacto potencial sobre a comparação entre os dois documentos europeus.

**Correção aplicada:** adicionado o padrão `\bpublic sector\b` → `PUBLICSECTORTOKEN` ao `preprocess()` de `ai_apply_strategy.ipynb`, com o mesmo rótulo de exibição já usado em `ai_continent_action_plan.ipynb` ("public sector", minúsculo). O notebook foi reexecutado; o termo passa a contar 12 ocorrências sob rótulo próprio — abaixo do corte de Top 50 deste documento (que tem um piso de frequência mais alto que os demais, dado o tamanho do texto), mas corretamente identificável e comparável.

**Nota metodológica:** "private sector" não ocorre neste documento (0 ocorrências, confirmado por busca literal) — não há, portanto, necessidade de proteção equivalente para esse termo aqui, apesar de protegido em outros documentos do projeto.

## 10. Histórico de atualizações

- **2026-08-05 (criação):** metodologia inicial completa (pré-processamento com 5 compostos institucionais, tokenização com hífen como separador residual, remoção, normalização com 68+34 grupos, corte Top 25 com observação de empates).
- **2026-08-05 (revisão metodológica):** correção da fragmentação por hífen (auditoria de 76 formas, todas mantidas unidas — Seção 2), desambiguação contextual de "power" em três sentidos e de "action"/"alliance" (nome próprio vs. genérico, usando o sinal de maiúscula — Seção 4), expansão da normalização morfológica (9 novos pares, 2 novas famílias verbais) e do corte para Top 50. Alterações determinadas pelo usuário para toda a pasta "Análise Documentos IA" (Brasil, China, Estados Unidos, Europa) e replicadas nas Skills 02_Análise_Vocab_A/B.
- **2026-08-05 (correção de consistência entre documentos):** adicionada proteção do bigrama "public sector" (Seção 9), motivada pela auditoria de consistência exigida antes da análise comparada da pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B, item 3). 12 ocorrências antes invisíveis, diluídas no bucket genérico "sectors".
