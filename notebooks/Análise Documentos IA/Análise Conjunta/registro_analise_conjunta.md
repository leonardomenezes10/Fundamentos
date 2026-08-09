# Registro de Análise Conjunta — Comparação dos 6 Planos Nacionais de IA

Registro persistente exigido pela **Skill 02_Análise_Vocab_B** (item 8), associado à análise comparada de
similaridade de vocabulário executada em `analise_geral.ipynb`. Deve ser lido antes de qualquer nova
visualização comparada envolvendo os mesmos documentos, para manter consistência metodológica entre
gráficos diferentes construídos ao longo do tempo.

- **Última atualização:** 2026-08-05 — extensão com TF-IDF, dendrograma e mapa de similaridade 2D
  (escalonamento multidimensional clássico), ver Seção 9.
- 2026-08-05 — criação (primeira execução completa da Skill 02_Análise_Vocab_B).

## 1. Documentos incluídos e documento central

Os seis documentos abaixo, um de cada pasta de país/bloco (China e Europa com dois documentos cada):

| Documento | Arquivo | País/bloco | Ano |
|---|---|---|---|
| "AI+" Initiative | `China/ai_plus.json` | China | 2025 |
| New Generation AI Development Plan | `China/new_generation_ai_development_plan.json` | China | 2017 |
| America's AI Action Plan | `Estados Unidos/americas_ai_action_plan.json` | EUA | 2025 |
| Apply AI Strategy | `Europa/apply_ai_strategy.json` | União Europeia | 2025 |
| AI Continent Action Plan | `Europa/ai_continent_action_plan.json` | União Europeia | 2025 |
| PBIA | `Brasil/pbia.json` | Brasil | 2025 |

Nenhum documento foi tratado automaticamente como central. A sequência estruturada (item 6.1) posiciona o
PBIA por último, por ser o eixo declarado do projeto de pesquisa (Skill B, seção "Documento central da
comparação"), não por presunção não verificada — essa escolha foi confirmada como consistente com a demanda
desta execução.

## 2. Idioma de cada documento e método de equivalência

Todos os seis documentos estão, em `texto_completo`, integralmente em **inglês** — inclusive os dois
documentos chineses (traduções institucionais do CSET e da New America/DigiChina) e o PBIA (publicação
oficial do MCTI/CGEE já publicada em inglês). Como todos os documentos compartilham o mesmo idioma, a
comparação lexical direta é válida; **não foi necessária** nenhuma etapa de equivalência conceitual/tradução
entre idiomas (etapa 1 da Skill B).

## 3. Herança das etapas 1-3 (a-b) dos notebooks individuais

O pipeline de extração/remoção/normalização morfológica/tratamento de hífen e bigramas/desambiguação
contextual de cada um dos seis documentos foi **integralmente reaproveitado** dos respectivos notebooks
individuais, já auditados sob a Skill 02_Análise_Vocab_A:

- `China/ai_plus.ipynb` (ver `China/registro_vocabulario_ai_plus.md`)
- `China/new_generation.ipynb` (ver `China/registro_vocabulario_new_generation_ai_development_plan.md`)
- `Estados Unidos/winning_race.ipynb` (ver `Estados Unidos/registro_vocabulario_americas_ai_action_plan.md`)
- `Europa/ai_apply_strategy.ipynb` (ver `Europa/registro_vocabulario_apply_ai_strategy.md`)
- `Europa/ai_continent_action_plan.ipynb` (ver `Europa/registro_vocabulario_ai_continent_action_plan.md`)
- `Brasil/pbia.ipynb` (ver `Brasil/pbia_vocab_registro.md`)

Nenhuma decisão de remoção, normalização, tratamento de hífen/bigrama ou desambiguação já registrada nesses
seis arquivos foi alterada por esta análise conjunta. As únicas duas camadas adicionais, exclusivas desta
pasta, são descritas nas Seções 4 e 5, abaixo.

## 4. Exclusão de identificadores idiossincráticos de nacionalidade/instituição (etapa 3-c)

Termos avaliados caso a caso e **excluídos** da base de similaridade (mantidos, sem qualquer alteração, nas
visualizações de frequência por documento — base 5-b):

| Documento | Termos excluídos | Justificativa |
|---|---|---|
| ai_plus | china (5), chinese (2), State Council (4) | autoidentificação do país/instituição emissora |
| new_generation | China (31), chinese (2), State Council (4) | idem |
| americas | United States (50), america (25), american (35), americans (7), DOC (50), dod (20), nist (16), caisi (17), nsf (14), doe (15), dol (8), omb (8), ostp (7), ic (8) | autoidentificação do país e de suas agências governamentais |
| apply_ai | EU (52), european (55), europe (21) | autoidentificação do bloco emissor |
| ai_continent | EU (112), european (40), europe (34) | idem |
| pbia | brazil (121), brazilian (95), brasil (3), mcti (10), cgee (2), nib (10), pbia (32) | autoidentificação do país/instituições/nome do próprio plano |

**Casos avaliados e mantidos (não excluídos), com justificativa registrada para transparência da decisão
inversa:**
- `china`/`chinese` em `americas` (2/3 ocorrências) e em `ai_continent` (1 ocorrência) — referências a um
  terceiro país/concorrente estratégico, não autoidentificação; carregam conteúdo temático real
  (enquadramento de rivalidade/competição), mesma lógica do exemplo "ally/enemy" da Skill B.
- `america`/`eu`/`european` no PBIA (5/1/4 ocorrências) — referências comparativas a "Latin America" e à
  União Europeia como terceiros, confirmadas por concordância (ver `analise_geral.ipynb`, célula de
  verificação de contexto); não são autoidentificação do Brasil.
- `Member States` em `apply_ai` (12) e `ai_continent` (25) — categoria substantiva de governança (como a UE
  organiza poder entre suas nações constituintes), eixo de comparação legítimo, não mero rótulo de
  identidade — mantido.
- `Trump` em `americas` (14 ocorrências) — nome próprio de pessoa, fora do escopo estrito do item 3-c
  (nacionalidade/instituição, não indivíduos); mantido por conservadorismo metodológico, caso de fronteira
  registrado explicitamente.

## 5. Harmonização de rótulos entre documentos (achado crítico desta execução)

Antes do cálculo de similaridade, foi realizada uma auditoria sistemática de consistência de rótulo para
todo conceito compartilhado entre dois ou mais documentos — estendendo a auditoria já registrada na Seção 9
(ou equivalente) de cada `registro_vocabulario_*.md`, que havia corrigido bigramas **ausentes**, mas não
havia verificado se bigramas já presentes em múltiplos documentos usavam exatamente o mesmo rótulo entre si.

**Achado de alto impacto:** o PBIA rotulava o conceito de Inteligência Artificial como
`"Artificial Intelligence (AI)"`, enquanto os outros cinco documentos usavam apenas `"AI"`. Como esse é o
termo mais frequente de **todos** os seis documentos (3,3%–6,5% do vocabulário de cada um; 625 ocorrências
no PBIA, 5,8% do seu vocabulário), essa divergência de rótulo fazia com que o PBIA tivesse similaridade zero
com os demais documentos neste único termo — o maior componente individual do vetor de qualquer um dos seis
documentos. **Correção:** rótulo do PBIA unificado para `"AI"`.

**Achados de impacto menor (mesma natureza — divergência de caixa/grafia para o mesmo referente, sem
qualquer dúvida de julgamento envolvida):**
- `"public sector"` (`apply_ai`, `ai_continent`) vs. `"Public Sector"` (`pbia`) → unificado para `"Public Sector"`.
- `"private sector"` (`ai_continent`) vs. `"Private Sector"` (`americas`, `pbia`) → unificado para `"Private Sector"`.

**Correções não aplicadas nesta rodada (impacto negligenciável, ≤2 ocorrências/<0,03% do vocabulário do
respectivo documento — registradas como lacuna na Seção 7):** "Research & Development" não protegido em
`ai_continent_action_plan.json` (1 ocorrência bruta); "Machine Learning" não protegido em
`americas_ai_action_plan.json` (1 ocorrência); "Data Center" não protegido em
`new_generation_ai_development_plan.json` (1 ocorrência); "Public Service" e "Value Chain" não protegidos em
`apply_ai_strategy.json` (1 ocorrência cada).

**Importante:** esta harmonização de rótulos é exclusiva da base de similaridade (item 5-a) desta pasta —
não altera nenhum notebook, registro ou gráfico individual de país/bloco, cujos próprios Top 25/Top 50
permanecem corretos e inalterados para a leitura de cada documento isoladamente.

## 6. Método de normalização relativa e métrica de similaridade

- **Base vocabular:** vocabulário completo pós-etapa 3 (item 5-a da Skill B), após exclusão 3-c (Seção 4) e
  harmonização de rótulos (Seção 5) — **sem** corte de Top 50 em nenhuma etapa deste cálculo.
- **Normalização relativa (item 4):** frequência de cada termo dividida pelo total de tokens de conteúdo do
  próprio documento (após as etapas acima).
- **Métrica (item 6):** similaridade de cosseno entre vetores de frequência relativa, no espaço vetorial da
  união dos vocabulários completos dos seis documentos (5.119 termos distintos).
- **Sequência estruturada seguida (item 6.1):** (1) coerência interna China (`ai_plus` vs. `new_generation`);
  (2) coerência interna UE (`apply_ai` vs. `ai_continent`); (3) comparação entre blocos — China agregado, UE
  agregado e EUA; (4) posicionamento do PBIA em relação a cada documento e ao centroide dos outros cinco.
- **Critério de corte (item 5-b, usado apenas nas visualizações de frequência por documento, não na
  similaridade):** Top 50 termos por documento (herdado da Skill 02_Análise_Vocab_A), exibido em Top 15 no
  painel de pequenos múltiplos deste notebook por economia de espaço.

## 7. Resultados da matriz de similaridade (vocabulário completo)

| | AI+ (China) | New Gen. (China) | EUA | Apply AI (UE) | AI Continent (UE) | PBIA |
|---|---|---|---|---|---|---|
| **AI+ (China)** | 1,00 | 0,76 | 0,61 | 0,55 | 0,56 | 0,53 |
| **New Gen. (China)** | 0,76 | 1,00 | 0,71 | 0,65 | 0,64 | 0,62 |
| **EUA** | 0,61 | 0,71 | 1,00 | 0,78 | 0,75 | 0,72 |
| **Apply AI (UE)** | 0,55 | 0,65 | 0,78 | 1,00 | 0,86 | 0,74 |
| **AI Continent (UE)** | 0,56 | 0,64 | 0,75 | 0,86 | 1,00 | 0,71 |
| **PBIA** | 0,53 | 0,62 | 0,72 | 0,74 | 0,71 | 1,00 |

Bloco-agregado: China×UE = 0,68; China×EUA = 0,72; UE×EUA = 0,79. PBIA vs. centroide dos outros cinco = 0,77
(referência: similaridade média entre pares dentro desses cinco documentos = 0,69).

## 8. Lacunas metodológicas remanescentes

- Exclusão 3-c concentrada em candidatos de alta/média frequência mais uma busca direcionada por nomes de
  país/bloco, siglas de agências e nome do próprio plano — não uma auditoria termo a termo de toda a cauda
  longa de cada vocabulário (750-2.280 termos distintos por documento).
- As cinco correções de harmonização de impacto negligenciável listadas na Seção 5 não foram formalizadas
  nos notebooks individuais de origem.
- **[Resolvido em 2026-08-05, ver Seção 9]** ~~Sem `scipy` neste ambiente — não foi construído dendrograma
  formal de agrupamento hierárquico~~ — `scipy` foi utilizado na extensão desta mesma data para construir um
  dendrograma formal (`scipy.cluster.hierarchy`) e um mapa de similaridade 2D (`scipy.linalg.eigh`).
- **[Resolvido em 2026-08-05, ver Seção 9]** ~~Similaridade por frequência relativa pura (não ponderada por
  TF-IDF)~~ — uma segunda base ponderada por TF-IDF foi construída em paralelo à base original (que
  permanece válida e não foi substituída); as duas bases são comparadas explicitamente na Seção 9.
- Quatro dos seis documentos (dois chineses e, em menor medida, o PBIA) chegam ao corpus como tradução para
  o inglês — limitação estrutural inerente ao protocolo da Skill02/Skill B, não introduzida por esta análise.
- **(Nova, surgida na extensão da Seção 9)** N=6 documentos é uma amostra pequena para o cálculo de document
  frequency que alimenta o IDF (apenas 6 valores possíveis de df, resolução grosseira) e para a estabilidade
  estatística de uma projeção MDS (stress-1 de 0,376, "ajuste pobre" pelo critério de Kruskal — ver Seção 9).
- **(Nova)** Parte da distância lexical do PBIA em relação aos demais documentos reflete o gênero
  textual/formato do documento (plano extenso, com centenas de itens numerados em anexo — já registrado em
  `pbia_vocab_registro.md`, Seção 1.3), não apenas conteúdo temático; nem a similaridade de cosseno nem o
  TF-IDF separam esses dois efeitos.

## 9. Extensão: TF-IDF, dendrograma e mapa de similaridade 2D (MDS)

Registrada nesta seção porque estende a base de comparação (Seção 6) com uma segunda ponderação e três
visualizações adicionais — **sem** alterar ou substituir a matriz de similaridade por frequência relativa
pura já registrada na Seção 7, que permanece a base primária conforme o item 6 da Skill B.

- **TF-IDF.** Cada termo do vocabulário-união (Seção 6, 5.119 termos) ponderado por
  `idf(t) = ln((1+6)/(1+df(t))) + 1` (fórmula suavizada, equivalente a `TfidfVectorizer(smooth_idf=True)`,
  reimplementada manualmente por falta de `scikit-learn` no ambiente; `df(t)` = número de documentos, entre
  os 6, que contêm o termo). Reduz o peso do vocabulário genérico compartilhado por todo o corpus (ex.: "AI",
  presente em 6/6 documentos, idf=1,00) e aumenta o de termos discriminantes (presentes em 1 único documento,
  idf=2,25, ex.: "AI Factories"). Resultado: as 15 similaridades par-a-par caem em relação à base de
  frequência pura (efeito esperado, não erro), e a ordem de proximidade do PBIA muda de forma relevante —
  sob frequência pura o documento mais próximo do PBIA era America's AI Action Plan (0,7217), à frente do AI
  Continent Action Plan (0,7117); sob TF-IDF essa ordem se **inverte** (AI Continent 0,4602 > America's
  0,4547); o Apply AI Strategy permanece o mais próximo do PBIA nas duas bases (0,7381 / 0,5012).
- **Dendrograma.** Distância euclidiana exata derivada dos vetores TF-IDF normalizados para norma unitária
  (identidade algébrica ‖a−b‖² = 2(1−cos(a,b)), não uma aproximação). Três métodos de ligação testados
  (`average`/`complete`/`ward`); escolhido `average` por maior correlação cofenética (0,9097, vs. 0,8719 e
  0,8617) — medida de quão bem o dendrograma preserva as distâncias originais (1,0 = perfeito). Os dois
  documentos europeus se unem primeiro (menor altura), os dois chineses em segundo; o documento dos EUA se
  junta ao par europeu antes de qualquer documento chinês; o PBIA só se junta ao restante no nível mais alto
  (maior distância) — mesma hierarquia já lida na matriz numérica, agora em forma de árvore.
- **Mapa de similaridade 2D.** Escalonamento multidimensional clássico (MDS de Torgerson-Gower), implementado
  via `scipy.linalg.eigh` sobre a matriz de produtos internos duplamente centrada (duplo centramento das
  distâncias TF-IDF ao quadrado), por não haver `MDS` pronto no `scipy` (só no `scikit-learn`, indisponível).
  k=2 explica 58,3% da variância de distância total (k=1: 33,5%; k=3: 76,9%; k=4: 90,3%; k=5: 100,0%), com
  **stress-1 de Kruskal = 0,3758** — "ajuste pobre" pelo critério convencional (<0,05 excelente; <0,10 bom;
  <0,20 razoável; ≥0,20 pobre). Checagem par a par (distância real 6D vs. reconstruída no mapa 2D) confirma
  que a distorção não é uniforme: os dois pares intra-bloco (China×China, UE×UE) são comprimidos em 80% e
  92%, respectivamente, enquanto os pares que envolvem o PBIA (as maiores distâncias do corpus) são
  preservados com fidelidade de 92-95%. **Implicação de leitura:** o mapa é confiável para agrupamento amplo
  (quais documentos formam "famílias" distantes umas das outras), não para julgar visualmente o quão
  parecidos são dois documentos do mesmo bloco entre si — para isso, a matriz numérica (Seção 7) ou o
  dendrograma (correlação cofenética 0,91, objetivamente mais fiel que o mapa 2D) são as fontes corretas.
- **Mapa radial centrado no PBIA.** Complementa o mapa 2D com uma visualização sem a distorção da projeção
  simultânea de 15 pares: raio = dissimilaridade exata (1 − similaridade de cosseno TF-IDF) entre o PBIA e
  cada um dos outros cinco documentos, lida diretamente da matriz de similaridade, não de uma projeção.
  Ângulo é apenas agrupamento visual por bloco/país, sem significado métrico (declarado no título do
  gráfico). Ordem de proximidade ao PBIA: Apply AI Strategy (0,499) < AI Continent Action Plan (0,540) <
  America's AI Action Plan (0,545) < New Generation AI Development Plan (0,602) < "AI+" Initiative (0,668).
- **Lacunas específicas desta extensão:** ver os dois últimos itens da Seção 8, acima.

## 10. Histórico de atualizações

- **2026-08-05 (extensão):** adição de TF-IDF, dendrograma (`scipy.cluster.hierarchy`) e mapa de similaridade
  2D por escalonamento multidimensional clássico (`scipy.linalg.eigh`), mais um mapa radial centrado no PBIA,
  em `analise_geral.ipynb`. Resolve as duas lacunas de maior prioridade registradas na criação (ausência de
  `scipy`/dendrograma; similaridade apenas por frequência relativa pura). Não altera a matriz de similaridade
  original (Seção 7), que permanece a base primária. Ver Seção 9 para o detalhamento completo.
- **2026-08-05 (criação):** primeira execução completa da Skill 02_Análise_Vocab_B sobre os seis documentos,
  em `analise_geral.ipynb`. Inclui exclusão 3-c, harmonização crítica de rótulos (AI/Artificial Intelligence;
  Public/Private Sector), matriz de similaridade de cosseno sobre vocabulário completo, sequência estruturada
  (item 6.1) e painel de frequência por documento (item 5-b).
