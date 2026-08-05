# Registro de Análise de Vocabulário — ai_continent_action_plan.json

Registro persistente exigido pela **Skill 02_Análise_Vocab_A** (item 8), associado ao documento `ai_continent_action_plan.json` (AI Continent Action Plan, União Europeia). Deve ser lido antes de qualquer nova visualização de vocabulário sobre este mesmo documento e atualizado de forma cumulativa a cada novo pedido do usuário.

- **Idioma identificado em `texto_completo`:** inglês.
- **Campos do JSON utilizados:** `titulo`, `pais_ou_bloco`, `texto_completo` (exclusivamente, conforme protocolo da Skill02).
- **Última atualização:** 2026-08-05 — revisão metodológica completa determinada pelo usuário (correção da fragmentação por hífen, tratamento de bigramas essenciais, desambiguação contextual de termos polissêmicos e expansão do corte para Top 50).

## 0. Correção metodológica aplicada nesta revisão

A versão anterior tratava **todo hífen do texto corrido como separador universal** (regra explícita: "'open-source' → 'open' + 'source'; 'fine-tuning' → 'fine' + 'tuning'"), mesmo já protegendo 17 expressões compostas institucionais sem hífen (ex.: "Member States", "AI Factory"). Essa regra foi substituída por uma **auditoria individual de cada uma das 74 formas hifenizadas** identificadas no texto (Seção 2). Foi também descoberta uma polissemia genuína de "power" (computacional/energético/econômico-abstrato) e corrigida uma inconsistência de grafia: "public-sector"/"private-sector" (forma adjetival hifenizada) designam o mesmo referente que "public sector"/"private sector" (forma nominal com espaço, já protegida na versão anterior), mas não estavam sendo unificados a ela. Foram também expandidas a normalização morfológica e o corte de Top 25 para **Top 50**.

## 1. Pré-processamento aplicado ao texto corrido (antes da tokenização)

Mantidos integralmente da versão anterior: remoção do rótulo estrutural "Key Commission (/ EuroHPC) actions:" (7 ocorrências) e as 17 expressões compostas institucionais (EU, Cloud and AI Development Act, EuroHPC Joint Undertaking, AI Skills Academy, Apply AI Strategy, Data Union Strategy, Digital Innovation Hubs, AI in Science, AI Gigafactories, AI Factories, AI Act, AI Office, Member States, Single Market, Data Labs, public sector, private sector). Acrescentado nesta revisão:

| Operação | Justificativa |
|---|---|
| `"public-sector"` (3 ocorrências) → normalizado para `"public sector"` antes do bigrama institucional | Mesmo referente da forma nominal já protegida (Seção 1 da versão anterior) — forma adjetival hifenizada, não um composto conceitualmente distinto. |
| `"private-sector"` (1 ocorrência) → normalizado para `"private sector"` antes do bigrama institucional | Idem. |
| `"computing power"` / `"computational power"` (9 ocorrências) protegidas, rótulo `power (computacional)` | Desambiguação contextual — capacidade computacional, o sentido mais frequente de "power" neste documento. |
| `"power capacity"` e `"power"` (verbo, "power their facilities") (2 ocorrências) protegidas, rótulo `power (energia)` | Desambiguação contextual — sentido energético/elétrico. |
| `"purchasing power"` (1 ocorrência) protegida, rótulo `power (econômico/abstrato)` | Desambiguação contextual — capacidade de compra, um terceiro referente distinto. |

## 2. Tokenização e auditoria de compostos com hífen

**Regra de tokenização:** sequências de letras (e `_` para os rótulos institucionais), preservando hífens internos como parte do token (`[A-Za-z_]+(?:-[A-Za-z]+)*`) — substitui a antiga regra de "hífen = separador universal".

**Auditoria das 74 formas hifenizadas identificadas em `texto_completo`.** Duas foram resolvidas como variantes ortográficas do mesmo referente institucional já protegido (Seção 1: "public-sector"/"private-sector"). As **72 formas restantes foram mantidas unidas** — nenhuma qualificou para separação. Organizadas tematicamente:

| Categoria | Formas (frequência) |
|---|---|
| Categorias "high-X" | high-quality (12), high-performance (2), high-risk (2), high-resolution (1) |
| Escopo EU/não-EU | non-eu (8), eu-based (2), eu-funded (1), intra-eu (1) |
| Escala | large-scale (7), giga-factories (1, uso genérico, distinto do bigrama institucional "AI Gigafactories") |
| Excelência/desempenho | cutting-edge (5), world-class (2), first-ever (1) |
| Porte/prazo "mid-X" | mid-caps (4), mid-term (1) |
| Descritores "AI-X" | ai-optimised (3), ai-based (3), ai-driven (2), ai-related (2), ai-focused (2), ai-savvy (1) |
| Termos empresariais | scale-up (3), spin-off (2), one-stop (1) |
| Técnicas de IA | fine-tuning (3), pre-trained (1), risk-based (1), decision-making (1) |
| "-specific" | sector-specific (3), industry-specific (2) |
| Nível/hierarquia | top-level (3) |
| Parceria público-privada | public-private (2) |
| Humano-IA | human-centric (2), human-robot (1) |
| Ecossistema aberto | open-source (1), general-purpose (1), know-how (1) |
| Sustentabilidade/eficiência | resource-efficient (1), energy-related (1), energy-consumption (1) |
| Colocações fixas | forward-looking (1), real-world (2), real-time (1), well-organised (1), well-functioning (1), well-being (1), ready-to-use (1), tailor-made (1), hands-on (1), long-term (1), broad-based (1), like-minded (1) |
| Nomes próprios (sítios/consórcios) | melusina-ai (1) — AI Factory em Luxemburgo; alt-edic (1) — Alliance for Language Technologies |
| Dados/demanda | data-pooling (1), demand-side (1) |
| Idioma/setor | agri-food (1), cyber-defence (1), non-technical (1) |
| Escala corporal/técnica | micro-sized (1) |
| "co-X" | co-pilot (1), co-creation (1), co-funds (1), co-legislators (1), co-regulatory (1) |
| Geração/inovação | next-generation (1), cross-pollinations (1), cross-sectoral (1) |
| Idioma fixo | beyond-the-state-of-the-art (1), use-case (1) |
| Autoavaliação | self-assessment (1) |

## 3. Duas operações distintas: remoção e normalização

**(a) Remoção:** mesma lista de palavras funcionais do inglês já usada neste projeto, mais `up`/`well` (partículas fraseológicas específicas deste documento, herdadas) e tokens de um único caractere.

**(b) Normalização morfológica — cobertura ampliada para Top 50.** Mantidos os 31 grupos de substantivos e as 26 famílias verbais já existentes; acrescentados nesta revisão:

*Novos pares singular/plural (21):* application(s), business(es), domain(s), science(s), infrastructure(s), administration(s), provision(s), call(s), market(s), way(s), communication(s), dialogue(s), example(s), process(es), partner(s), degree(s), scheme(s), candidate(s), field(s), centre(s), effort(s).

*Nova família verbal (1):* focus-verbo (focus/focuses/focusing/focused).

## 4. Desambiguação contextual de termos polissêmicos/homônimos (Skill 02_Análise_Vocab_A, item 5)

| Termo | Sentidos identificados (por concordância) | Decisão |
|---|---|---|
| power (12 ocorrências soltas antes do desdobramento) | 9 no sentido computacional ("computing power", "computational power"); 2 no sentido energético ("power capacity", "power their facilities"); 1 no sentido econômico/abstrato ("purchasing power") | **Desdobrado em três rótulos**: `power (computacional)` (9), `power (energia)` (2), `power (econômico/abstrato)` (1) |
| generation | Todas as 5 ocorrências soltas (excluindo o composto hifenizado "next-generation", mantido unido) têm sentido de geração tecnológica/etária ("the next generation of frontier AI models", "the current generation of AI models") | Verificado e **não desdobrado** — sentido único confirmado por concordância |
| state (residual, 2) / states (0 genérico, todas "Member States") / State aid (2) | "Member States" protegido como bigrama (25); "State aid" designa instituto jurídico distinto (regras de auxílio estatal da UE); a única ocorrência de "state" fora desses dois padrões está dentro do composto hifenizado "beyond-the-state-of-the-art" (Seção 2), já mantido unido | Mantidos **separados** (herdado, reconfirmado) |
| AI / AGI (Artificial General Intelligence); development/develop; security/secure; advance/advances/advancing/advanced; European/Europe; innovation/innovative; strategy/strategic; sector/sectorial | Conceitos distintos por definição do texto, pares derivacionais, ou ambiguidade de classe gramatical alta demais para fusão segura | Mantidos **separados** (herdados, reconfirmados) |

## 5. Bigramas essenciais tratados como unidade

Mantidos os 17 já existentes (Seção 1). Acrescentados nesta revisão:

| Bigrama | Ocorrências | Justificativa |
|---|---|---|
| computing power / computational power | 9 | Desambiguação de "power" (Seção 4) |
| power capacity / power (verbo) their | 2 | Desambiguação de "power" (Seção 4) |
| purchasing power | 1 | Desambiguação de "power" (Seção 4) |
| public-sector → public sector | 3 | Normalização de grafia adjetival/nominal (Seção 1) |
| private-sector → private sector | 1 | Normalização de grafia adjetival/nominal (Seção 1) |

## 6. Critério de corte

**Top 50** termos por frequência absoluta (critério padrão da Skill 02_Análise_Vocab_A, item 6), com o **Top 25** mantido como recorte adicional. Frequência absoluta é apropriada por se tratar de análise de um único documento.

## 7. Limitações metodológicas remanescentes

- **Cobertura da normalização morfológica e da desambiguação contextual concentrada nos candidatos plausíveis ao Top 50** — não há varredura exaustiva de toda a cauda longa de 1.583 termos distintos do vocabulário final.
- **"State aid" segue sem proteção de bigrama explícita no código** (apenas documentado como par não-fundido) — sua baixíssima frequência (2 ocorrências) não afeta o corte de Top 50, mas uma reprodução futura desta análise deveria formalizar essa proteção caso a frequência aumente em revisões futuras do documento.
- **"European"/"Europe" seguem não fundidos**, por representarem classes gramaticais e referentes distintos (herdado).

## 8. Histórico de atualizações

- **2026-08-05 (criação):** metodologia inicial completa (remoção de rótulo estrutural, unificação de 17 expressões compostas institucionais, tokenização com hífen como separador, normalização de 31+26 grupos, corte Top 25).
- **2026-08-05 (revisão metodológica):** correção da fragmentação por hífen (auditoria de 74 formas, 72 mantidas unidas, 2 normalizadas para o bigrama nominal já existente — Seção 2), desambiguação contextual de "power" em três sentidos (Seção 4), expansão da normalização morfológica (21 novos pares, 1 nova família verbal) e do corte para Top 50. Alterações determinadas pelo usuário para toda a pasta "Análise Documentos IA" (Brasil, China, Estados Unidos, Europa) e replicadas nas Skills 02_Análise_Vocab_A/B.
