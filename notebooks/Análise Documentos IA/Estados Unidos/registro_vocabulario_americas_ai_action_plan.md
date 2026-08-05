# Registro de Análise de Vocabulário — americas_ai_action_plan.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 8), associado ao documento `americas_ai_action_plan.json` (America's AI Action Plan, Estados Unidos). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês.
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05 — revisão metodológica completa determinada pelo usuário (correção da fragmentação por hífen, tratamento de bigramas essenciais, desambiguação contextual de termos polissêmicos e expansão do corte para Top 50).

## 0. Correção metodológica aplicada nesta revisão

A versão anterior tratava **todo hífen como separador universal** (regra explícita: "'open-source' → 'open' + 'source'; 'AI-related' → 'AI' + 'related'"). Essa regra foi substituída por uma **auditoria individual de cada uma das 83 formas hifenizadas** identificadas no texto (Seção 2). Foi também descoberta e corrigida uma polissemia genuína e significativa: **"power" e "generation"**, quando usados soltos neste documento, misturavam sistematicamente o sentido geopolítico/computacional com o sentido energético (rede elétrica/geração de energia) — o mesmo tipo de ambiguidade citado como exemplo pelo usuário ao pedir esta revisão. Foram também expandidas a normalização morfológica e o corte de Top 25 para **Top 50**.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

| Operação | Justificativa |
|---|---|
| `"U.S."` → `"United States"`, bigrama `"United States"` protegido (50 ocorrências) | Sigla e forma por extenso designam o mesmo referente (o país); mantido separado de "state(s)" subnacional (Seção 4). |
| `"Artificial Intelligence"` → `"AI"` | Mesmo referente. |
| Remoção do subtítulo fixo `"Recommended Policy Actions"` (30 ocorrências) | Rótulo estrutural repetido mecanicamente, sem valor de vocabulário orgânico — mesma natureza dos cabeçalhos já descartados na Skill01. |
| `"power generation"` / `"energy generation"` (6 ocorrências) protegidas como bigrama único, rótulo `power/energy generation (infraestrutura elétrica)` | Desambiguação contextual (Seção 4): sentido de infraestrutura de geração elétrica, o mais frequente de "power"/"generation" neste documento. |
| `"computing power"` (1 ocorrência) protegida, rótulo `power (computacional)` | Desambiguação contextual — capacidade computacional, referente distinto de energia e de geopolítica. |
| `"balance of power"` e `"power of American innovation"` (2 ocorrências) protegidas, rótulo `power (geopolítico/abstrato)` | Desambiguação contextual — sentido geopolítico/abstrato de força e capacidade nacional, referente distinto de energia e de computação. |

## 2. Tokenização e auditoria de compostos com hífen

**Regra de tokenização:** sequências de letras, preservando hífens internos como parte do token (`[A-Za-z]+(?:-[A-Za-z]+)*`) — substitui a antiga regra de "hífen = separador universal".

**Auditoria das 83 formas hifenizadas identificadas em `texto_completo`.** Todas foram mantidas unidas — nenhuma qualificou para separação em suas palavras componentes. Organizadas tematicamente:

| Categoria | Formas (frequência) |
|---|---|
| Descritores "AI-X" | ai-related (5), ai-enabled (4), ai-driven (2), ai-specific (2), ai-ready (1), ai-based (1), ai-generated (1) |
| Ecossistema aberto | open-source (4), open-weight (4), non-proprietary (1) |
| Categorias "high-X" | high-paying (4), high-quality (3), high-security (2), high-stakes (1), high-priority (1) |
| Escala | large-scale (3), industrial-scale (1) |
| Excelência/desempenho | world-class (3), cutting-edge (2), best-practices (2), well-suited (1) |
| Temporal/geracional | long-term (2), near-term (1), next-generation (2) |
| Propósito/escopo | general-purpose (2), domain-specific (1), full-stack (1) |
| Termo técnico fixo | use-cases (2) |
| Descritores "-driven" (fora do campo IA) | industry-driven (2), performance-driven (1) |
| Segurança "by design"/crítica | secure-by-design (2), safety-critical (1) |
| "-related"/sub- | sub-systems (2), security-related (2), deepfake-related (1), center-related (1) |
| Setor privado | private-sector (1), private-sector-led (1) |
| Programas de força de trabalho | set-aside (1), top-down (1), try-first (1), worker-first (1), job-ready (1), on-ramps (1), hands-on (1), pre-apprenticeships (1) |
| Nível/porte | medium-sized (1), entry-level (1), firm-level (1) |
| Compostos DOD | dod-intelligence (1), dod-led (1) |
| Fiscal | tax-free (1) |
| Veículos autônomos | self-driving (1) |
| Nome de lei (próprio) | stevenson-wydler (1) — Stevenson-Wydler Technology Innovation Act |
| Intensidade | labor-intensive (1), energy-intensive (1) |
| Infraestrutura/financiamento | cloud-enabled (1), chips-funded (1) |
| Pesquisa | focused-research (1) |
| "non-X" | non-sensitive (1), non-consensual (1) |
| Biotecnologia | whole-genome (1) |
| Descritor geral | real-world (1) |
| Programa de intercâmbio | talent-exchange (1) |
| "pre-X" | pre-existing (1), pre-construction (1) |
| Operações | back-office (1) |
| Geopolítico | nation-state (1) |
| "co-X" | co-developed (1), co-operation (1, grafia britânica — nome oficial da OCDE, "Organisation for Economic Co-operation and Development") |
| Descritores diversos | jump-started (1), fly-away (1), free-riding (1), like-minded (1), standard-setting (1), near-monopolies (1), defense-industrial (1), multi-tiered (1) |
| Nome próprio (instituição) | export-import (1) — Export-Import Bank |
| Controle de exportação | end-use (1), in-country (1) |

## 3. Duas operações distintas: remoção e normalização

**(a) Remoção:** mesma lista de palavras funcionais do inglês já usada neste projeto, mais tokens de um único caractere (resíduo de abreviações pontuadas e possessivos).

**(b) Normalização morfológica — cobertura ampliada para Top 50.** Mantidos os 35 grupos de substantivos e as 12 famílias verbais já existentes; acrescentados nesta revisão:

*Novos pares singular/plural (34):* field(s), benefit(s), pillar(s), semiconductor(s), application(s), job(s), goal(s), law(s), business(es), rule(s), order(s), government(s), academic(s), market(s), investment(s), project(s), approach(es), chip(s), environment(s), process(es), workflow(s), deepfake(s), way(s), officer(s), nation(s), agenda(s), ally/allies/allied, challenge(s), council(s), protection(s), requirement(s), review(s), role(s), provider(s) (mantido separado do verbo "provide", herdado).

*Novas famílias verbais (18):* adopt, align, conduct, deliver, design, direct, fund, implement, increase, launch, maintain, measure, pilot, protect, streamline, supply, train, transform.

## 4. Desambiguação contextual de termos polissêmicos/homônimos (Skill 02_Análise_Vocab_A, item 5)

| Termo | Sentidos identificados (por concordância) | Decisão |
|---|---|---|
| power (21 ocorrências soltas antes do desdobramento) | 14 no sentido energético/infraestrutura elétrica solto ("power grid", "power lines", "power markets", "power sources", "power consumers", "supply of power"); 6 na locução "power/energy generation"; 1 em "computing power" (computacional); 2 em sentido geopolítico/abstrato ("balance of power", "power of American innovation") | **Desdobrado em quatro rótulos**: `power (energia/infraestrutura elétrica)` (14), `power/energy generation (infraestrutura elétrica)` (6), `power (computacional)` (1), `power (geopolítico/abstrato)` (2) |
| generation (9 ocorrências soltas, excluindo as 2 do composto "next-generation") | 7 no sentido energético (das quais 6 dentro da locução "power/energy generation", já desdobradas acima); 1 no sentido tecnológico ("the next generation of AI breakthroughs") — exatamente o par de sentidos apontado como exemplo pelo próprio usuário ao solicitar esta revisão | **Desdobrado**: `power/energy generation (infraestrutura elétrica)` (6, ver acima) e `generation (tecnológica)` (1) |
| state(s) (13) / United States (50) | "state(s)" refere-se a estados subnacionais dos EUA (ex.: "a state's AI regulatory climate"); "United States" é o país | Mantidos **separados** (herdado, reconfirmado) |
| America / American / Americans | Topônimo, adjetivo e substantivo plural (pessoas) — classes gramaticais e referentes distintos | Mantidos **separados** (herdado) |
| intelligence (fora do bigrama "Artificial Intelligence") | Sentido de "Intelligence Community"/inteligência de segurança, referente distinto de "AI" | Mantido **separado** de "AI" (herdado) |
| development / develop; security / secure; leadership / lead-led; technical / technological; provide / providers; economic / economy; advance / advanced; research / researchers | Pares derivacionais ou de classe gramatical distinta, não flexões de um mesmo lema | Mantidos **separados** (herdados, reconfirmados) |

## 5. Bigramas essenciais tratados como unidade

| Bigrama | Ocorrências | Justificativa |
|---|---|---|
| United States | 50 | Nome do país (Seção 1) |
| power/energy generation | 6 | Desambiguação de "power"/"generation" (Seção 4) |
| computing power | 1 | Desambiguação de "power" (Seção 4) |
| balance of power / power of American innovation | 2 | Desambiguação de "power" (Seção 4) |
| Recommended Policy Actions | 30 (removido) | Rótulo estrutural, não vocabulário orgânico (Seção 1) |

## 6. Critério de corte

**Top 50** termos por frequência absoluta (critério padrão da Skill 02_Análise_Vocab_A, item 6), com o **Top 25** mantido como recorte adicional. Frequência absoluta é apropriada por se tratar de análise de um único documento.

## 7. Limitações metodológicas remanescentes

- **Cobertura da normalização morfológica e da desambiguação contextual concentrada nos candidatos plausíveis ao Top 50** — não há varredura exaustiva de toda a cauda longa de 1.681 termos distintos do vocabulário final.
- **"America"/"American"/"Americans" seguem não fundidos** — decisão herdada, mantida por representarem classes gramaticais e referentes distintos.
- **"DOC" (Department of Commerce) e demais siglas institucionais** (NIST, CAISI, NSF, DOE, DOL, OMB, OSTP, IC) mantidas como tokens próprios, sem fusão entre si nem com termos genéricos — cada uma designa uma agência distinta.

## 9. Correção de consistência entre documentos (auditoria da Análise Conjunta, 2026-08-05)

Antes da análise comparada de similaridade na pasta "Análise Conjunta", a Skill 02_Análise_Vocab_B (item 3) exige verificar se o mesmo bigrama recebe o mesmo tratamento em todos os documentos comparados. A auditoria identificou **quatro bigramas conceituais** presentes neste documento com frequência relevante, mas sem proteção equivalente à já aplicada em outros documentos do projeto:

| Bigrama | Ocorrências em `texto_completo` | Protegido em (antes desta correção) | Situação anterior neste documento |
|---|---|---|---|
| Research & Development (R&D) | 6 (2 "Research and Development" + 4 "R&D") | PBIA (27) | Fragmentado em "research"/"development" soltos |
| Data Center(s) | 14 | PBIA (16) | Fragmentado em "data"/"center(s)" — "center(s)" já tinha merge morfológico genérico, mas sem isolar o composto "data center" como conceito próprio |
| Private Sector | 10 (8 "private sector" + 2 formas hifenizadas "private-sector"/"private-sector-led") | PBIA (8), ai_continent_action_plan.json (3, unidas) | **Achado mais significativo desta auditoria** — ver detalhamento abaixo |
| Federal Government | 10 | PBIA (9) | Fragmentado em "federal" (solto) + "government(s)" (bucket genérico, misturado com qualquer outro uso de "government") |

**Detalhamento do caso "Private Sector".** Este é o achado mais relevante da auditoria, pelo tipo de erro que revela: o documento europeu `ai_continent_action_plan.json` já normalizava a variante adjetival hifenizada ("private-sector") para o mesmo referente nominal ("private sector") antes de protegê-lo como bigrama institucional — correção que o próprio registro daquele documento já havia aplicado à sua própria inconsistência interna (hífen vs. espaço). Este documento (EUA), porém, não replicava esse tratamento: das 10 ocorrências totais do conceito "setor privado", apenas 2 (as hifenizadas, mantidas como tokens "private-sector"/"private-sector-led" isolados, sem consolidação) eram sequer identificáveis como tal; as 8 ocorrências na forma espaçada "private sector" se fragmentavam em "private" (token solto, sem qualquer normalização) + "sector" (absorvido no bucket genérico `sector(s)`, junto com qualquer outro uso de "sector" no documento — tecnológico, de chips, etc.). Ou seja: 8 das 10 ocorrências do conceito ficavam **estatisticamente invisíveis**, diluídas em outro rótulo — exatamente o tipo de inconsistência que a Skill 02_Análise_Vocab_B, item 3, exige detectar e corrigir antes de qualquer comparação entre documentos.

**Correção aplicada:**
- `\bResearch and Development\b|\bR&D\b` → bigrama `"Research & Development (R&D)"` (mesmo rótulo do PBIA).
- `\bData Centers?\b` → bigrama `"Data Center(s)"` (mesmo rótulo do PBIA).
- `\bprivate-sector\b` (quando **não** seguido de outro hífen, preservando "private-sector-led" como composto de três partes com identidade própria — não fundido) → normalizado para a forma nominal `"private sector"`, em seguida protegido como bigrama `"Private Sector"` (mesmo rótulo do PBIA; mesma lógica de normalização já usada em `ai_continent_action_plan.ipynb`).
- `\bFederal Government\b` → bigrama `"Federal Government"` (mesmo rótulo do PBIA).

O notebook foi reexecutado. Nenhum dos quatro termos altera o Top 50 deste documento (todos abaixo do corte de frequência), mas todos passam a ser corretamente identificáveis e comparáveis entre documentos — o que é o requisito relevante para a Análise Conjunta, não para o gráfico individual deste documento.

**Nota metodológica:** "public sector" não ocorre neste documento (0 ocorrências, confirmado por busca literal) — não há, portanto, necessidade de proteção equivalente para esse termo aqui, apesar de protegido em outros documentos do projeto.

## 10. Histórico de atualizações

- **2026-08-05 (criação):** metodologia inicial (pré-processamento, tokenização com hífen como separador, remoção, normalização, corte Top 25).
- **2026-08-05 (revisão metodológica):** correção da fragmentação por hífen (auditoria de 83 formas, todas mantidas unidas — Seção 2), desambiguação contextual de "power" e "generation" — dois termos que misturavam sentido geopolítico/computacional e energético (Seção 4) —, proteção do bigrama "United States", expansão da normalização morfológica (34 novos pares, 18 novas famílias verbais) e do corte para Top 50. Alterações determinadas pelo usuário para toda a pasta "Análise Documentos IA" (Brasil, China, Estados Unidos, Europa) e replicadas nas Skills 02_Análise_Vocab_A/B.
- **2026-08-05 (correção de consistência entre documentos):** adicionada proteção de quatro bigramas conceituais — Research & Development (R&D), Data Center(s), Private Sector, Federal Government (Seção 9) — motivada pela auditoria de consistência exigida antes da análise comparada da pasta "Análise Conjunta" (Skill 02_Análise_Vocab_B, item 3). Caso mais significativo: "Private Sector", com 8 das 10 ocorrências antes invisíveis, diluídas no bucket genérico "sector(s)".
