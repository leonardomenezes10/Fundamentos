# Relatório — Análise Conjunta de Vocabulário dos 6 Planos Nacionais de IA

**Data:** 2026-08-05 (criação e extensão TF-IDF/dendrograma/mapa de similaridade, mesma data)
**Executor:** Skill 02_Análise_Vocab_B (revisão 2026-08-05), a partir da demanda explícita do usuário
**Artefatos produzidos:** `analise_geral.ipynb` (executado, sem erros, 46 células), `registro_analise_conjunta.md`, este relatório

---

## 1. O que foi feito

Foi executada, pela primeira vez de forma completa, a comparação de vocabulário entre os seis Planos
Nacionais de Inteligência Artificial reunidos neste projeto:

| Documento | País/bloco | Ano |
|---|---|---|
| "AI+" Initiative | China | 2025 |
| New Generation AI Development Plan | China | 2017 |
| America's AI Action Plan | Estados Unidos | 2025 |
| Apply AI Strategy | União Europeia | 2025 |
| AI Continent Action Plan | União Europeia | 2025 |
| PBIA | Brasil | 2025 |

O trabalho reaproveitou integralmente o pipeline de extração, remoção de termos funcionais, normalização
morfológica, tratamento de hífen/bigramas e desambiguação contextual já auditado individualmente para cada
um dos seis documentos (Skill 02_Análise_Vocab_A) — nenhuma dessas decisões foi revisitada ou alterada.
Sobre esse resultado já consolidado, foram aplicadas duas camadas adicionais, exclusivas da comparação
conjunta (Skill 02_Análise_Vocab_B): a exclusão de termos que apenas nomeiam a identidade nacional/
institucional de cada documento, e uma auditoria de consistência de rótulos entre documentos — que revelou
um problema crítico, detalhado na Seção 3.

A partir daí, foi calculada uma **matriz de similaridade de cosseno** entre os seis documentos, usando o
**vocabulário completo** de cada um (não um recorte de Top 50) — implementando diretamente a correção
metodológica que motivou a revisão da Skill B nesta mesma conversa: o corte de Top 50 é válido apenas para
gráficos de frequência de um único documento, nunca como base de um cálculo de similaridade entre
documentos.

## 2. Metodologia utilizada

**Idioma.** Os seis documentos estão, em `texto_completo`, integralmente em inglês (incluindo os dois
documentos chineses, traduzidos por CSET e New America/DigiChina, e o PBIA, publicado em inglês pelo
MCTI/CGEE) — o que torna a comparação lexical direta válida, sem necessidade de uma etapa de equivalência
entre idiomas.

**Vocabulário completo vs. Top 50.** Foram mantidas, deliberadamente separadas, duas bases vocabulares:
- a base de **similaridade** usa o vocabulário completo de cada documento, sem nenhum corte por rank;
- as visualizações de **frequência por documento** (pequenos múltiplos de Top 15, no final do notebook)
  continuam usando o corte de Top 50/Top 25 já estabelecido, exatamente como nos notebooks individuais.

**Exclusão de identificadores nacionais/institucionais.** Antes do cálculo de similaridade, foram excluídos
— documento a documento, nunca por uma lista fixa automática — os termos que apenas nomeiam o próprio país,
bloco ou instituição emissora de cada plano (ex.: "Brazil"/"Brazilian" no PBIA; "China" nos dois documentos
chineses; "United States"/"America"/"DOC" e demais siglas de agências nos EUA; "EU"/"European"/"Europe" nos
dois documentos europeus; "MCTI"/"CGEE"/"NIB"/"PBIA" no documento brasileiro). Ao todo, 27 termos foram
avaliados e excluídos; casos de fronteira (menções a "China" nos documentos dos EUA/UE, à "America"/"EU" no
PBIA, ao termo "Member States" na UE, e ao nome próprio "Trump" nos EUA) foram deliberadamente **mantidos**,
com justificativa registrada, por representarem referências a terceiros ou conteúdo temático substantivo —
não autoidentificação.

**Normalização relativa e métrica de similaridade.** Cada documento foi representado como um vetor de
frequência relativa (proporção de cada termo em relação ao total de tokens de conteúdo do próprio
documento), no espaço da união dos vocabulários dos seis documentos (5.119 termos distintos). A similaridade
entre cada par foi medida por similaridade de cosseno.

**Sequência de leitura (do mais específico ao mais amplo).** 1) coerência interna da China (os dois
documentos chineses entre si); 2) coerência interna da União Europeia (os dois documentos europeus entre
si); 3) comparação entre os três blocos com abordagem própria (China, UE e EUA); 4) posicionamento do PBIA
em relação a cada um dos cinco documentos e ao conjunto como um todo.

## 3. Achado metodológico crítico: rótulos inconsistentes entre documentos

A parte mais importante deste trabalho não foi o cálculo de similaridade em si, mas uma verificação prévia
de consistência que ele exigiu: **o mesmo conceito estava rotulado de forma diferente em documentos
diferentes**, o que teria invalidado silenciosamente qualquer comparação.

O caso mais grave: cinco dos seis documentos rotulavam o conceito de Inteligência Artificial simplesmente
como **"AI"**, mas o PBIA o rotulava como **"Artificial Intelligence (AI)"** — uma string diferente. Como
"AI" é, disparadamente, o termo mais frequente de **todos** os seis documentos (entre 3,3% e 6,5% do
vocabulário de cada um; 625 ocorrências no PBIA, quase 6% de todo o seu vocabulário), esse descompasso de
rótulo fazia o PBIA ter similaridade **zero** com os outros cinco documentos exatamente no termo que mais
pesa em qualquer um deles. Isso derrubava artificialmente a similaridade calculada do PBIA com o restante do
corpus — antes da correção, o PBIA aparecia como um documento isolado (similaridade de 0,09 a 0,18 com os
demais); depois de corrigido o rótulo, essa mesma similaridade sobe para 0,53–0,74, uma faixa muito mais
compatível com a similaridade observada entre os outros cinco documentos entre si (0,55–0,86). Duas
inconsistências menores do mesmo tipo (maiúscula/minúscula em "Public Sector"/"Private Sector" entre
documentos) também foram encontradas e corrigidas.

Essa correção foi aplicada **apenas** na base de comparação desta pasta — nenhum notebook, gráfico ou
registro individual de país foi alterado; os Top 25/Top 50 de cada documento continuam corretos como estão.

## 4. Principais achados da comparação

- **Coerência interna por bloco:** os dois documentos europeus (Apply AI Strategy e AI Continent Action
  Plan, ambos de 2025) são o par mais coeso de todo o corpus (0,86). Os dois documentos chineses (2025 e
  2017) também guardam coerência alta, porém menor (0,76) — possivelmente relacionado ao hiato de oito anos
  entre eles, embora o gráfico por si só não distinga essa hipótese de uma divergência substantiva de
  enquadramento entre os dois planos.
- **Entre blocos:** UE e EUA são os mais próximos entre si (0,79); a China é o bloco mais distinto tanto da
  UE (0,68) quanto, em menor grau, dos EUA (0,72).
- **Posicionamento do PBIA:** o PBIA aproxima-se mais dos dois documentos europeus e do documento
  estadunidense (0,71–0,74) do que dos dois documentos chineses (0,53–0,62). Sua similaridade ao conjunto
  dos outros cinco documentos (0,77) está na mesma ordem de grandeza da similaridade média entre esses cinco
  documentos entre si (0,69) — ou seja, uma vez corrigido o problema de rótulo da Seção 3, o PBIA **não** é
  um documento vocabularmente isolado do conjunto internacional, e se posiciona relativamente mais próximo
  do eixo EUA/UE do que do eixo chinês.

## 5. Extensão: TF-IDF, dendrograma e mapa de similaridade 2D

Após a matriz de similaridade de cosseno (Seção 4), o notebook foi estendido com uma segunda camada de
comparação e três visualizações adicionais — sem substituir a matriz original, que permanece a base
primária do método (item 6 da Skill B). Esta é a parte do trabalho que constrói, especificamente, o **mapa
de similaridade** que posiciona o PBIA em relação aos demais documentos.

**TF-IDF.** A similaridade de cosseno original usa frequência relativa pura, que trata "AI" (presente nos
seis documentos) com o mesmo peso metodológico de um termo presente em apenas um deles — mesmo o primeiro
não ajudando em nada a diferenciar os documentos entre si. TF-IDF pondera cada termo por quantos dos seis
documentos o contêm (fórmula suavizada padrão, `idf = ln(7/(1+df)) + 1`), reduzindo o peso do vocabulário
genérico do gênero "plano nacional de IA" e realçando o vocabulário que de fato distingue um documento dos
demais. Sob essa base mais discriminante, a ordem de proximidade do PBIA muda de forma relevante: por
frequência pura, o documento mais próximo do PBIA era o America's AI Action Plan (0,72); por TF-IDF, essa
posição passa para o AI Continent Action Plan (0,46 vs. 0,45 do documento estadunidense) — o Apply AI
Strategy seguiu sendo o mais próximo do PBIA nas duas bases. Ou seja: uma vez removido o peso do vocabulário
genérico compartilhado por todo o corpus, o PBIA aparece mais alinhado aos **dois** documentos europeus do
que ao documento estadunidense.

**Dendrograma.** Construído sobre a distância euclidiana exata derivada do cosseno TF-IDF (identidade
algébrica válida para vetores normalizados, não uma aproximação), com ligação `average` — escolhida, entre
três métodos testados, por maximizar a correlação cofenética (0,91, numa escala em que 1,0 é perfeito), ou
seja, por preservar melhor as distâncias reais entre os seis documentos. Confirma numericamente a leitura já
feita na matriz: os dois documentos europeus se unem primeiro, os dois chineses em segundo, o documento dos
EUA junta-se ao par europeu antes de qualquer documento chinês, e o PBIA só se junta ao conjunto por último,
no nível de maior distância da árvore.

**Mapa de similaridade 2D.** Como um mapa fiel a todos os 15 pares simultaneamente exigiria até 5 dimensões,
foi aplicado escalonamento multidimensional clássico (MDS de Torgerson-Gower, via decomposição espectral em
`scipy`) para reduzir a 2 dimensões. As duas dimensões capturam 58,3% da variância total de distância, com
stress-1 de Kruskal de 0,376 — um ajuste classificado como "pobre" pelo critério convencional. Essa
imprecisão foi diagnosticada, não escondida: uma tabela de checagem par a par mostra que a distorção se
concentra nos pares do **mesmo bloco** (China×China comprimido em 80%, UE×UE em 92%), enquanto as distâncias
que envolvem o PBIA — as maiores do corpus — são preservadas com fidelidade de 92-95%. Isso torna o mapa
confiável para leitura de agrupamento amplo (que "famílias" de documentos existem e onde o PBIA se encaixa
entre elas), mas não para comparar visualmente o quão parecidos são dois documentos do mesmo bloco — para
isso, a matriz numérica ou o dendrograma (objetivamente mais fiel, correlação cofenética 0,91) continuam
sendo as fontes corretas. No mapa, o eixo horizontal separa um polo chinês de um polo europeu/estadunidense;
o PBIA se destaca isoladamente no eixo vertical, refletindo ser o documento mais distante de todos os outros
cinco simultaneamente (não apenas de um bloco específico).

**Mapa radial centrado no PBIA.** Para responder diretamente "como o PBIA se compara a cada documento", sem
a distorção da projeção simultânea de 15 pares, foi construído um segundo mapa que usa o PBIA como centro e
posiciona cada um dos outros cinco documentos a uma distância exata (não projetada) igual à sua
dissimilaridade TF-IDF real. Do mais ao menos parecido com o PBIA: Apply AI Strategy (0,50) < AI Continent
Action Plan (0,54) < America's AI Action Plan (0,55) < New Generation AI Development Plan (0,60) < "AI+"
Initiative (0,67). Inspecionando os termos que mais pesam em cada extremo: a proximidade do PBIA ao Apply AI
Strategy vem de vocabulário de política pública compartilhado ("use", "data", "develop", "strategic"); já
parte da distância do PBIA ao "AI+" Initiative reflete o **formato** do documento brasileiro (plano extenso,
organizado em "Ações"/"Impactos"/"Desafios" numerados) mais do que uma diferença puramente temática — uma
ressalva importante para a leitura de qualquer uma dessas medidas de similaridade.

## 6. Lacunas que podem ser preenchidas

1. **Auditoria de identificadores não é exaustiva.** A exclusão de termos de autoidentificação nacional
   (Seção 3-c da Skill B) cobriu os casos de frequência alta/média já sinalizados nos registros individuais
   mais uma busca direcionada (nomes de país/bloco, siglas de agências, nome do próprio plano) — não uma
   varredura termo a termo de toda a cauda longa de cada vocabulário (750 a 2.280 termos distintos por
   documento). É possível que identificadores de baixíssima frequência (nomes de cidades, de outros
   programas nacionais específicos) tenham escapado; o efeito esperado sobre a similaridade é pequeno, mas
   não nulo.
2. **Cinco inconsistências residuais de rótulo, de impacto negligenciável, não corrigidas.** "Research &
   Development" (1 ocorrência não protegida no AI Continent Action Plan), "Machine Learning" (1, America's
   AI Action Plan), "Data Center" (1, New Generation AI Development Plan), "Public Service" e "Value Chain"
   (1 cada, Apply AI Strategy) — cada uma abaixo de 0,03% do vocabulário do respectivo documento. Formalizar
   essas correções nos notebooks individuais (replicando o padrão de bigrama já usado nos demais documentos)
   é uma tarefa de baixo risco e baixo esforço para uma iteração futura.
3. **[Resolvida — ver Seção 5] Sem dendrograma formal.** Foi construído um dendrograma formal com
   `scipy.cluster.hierarchy` (ligação `average`, correlação cofenética 0,91) na extensão desta mesma data.
   Continua valendo, como lacuna residual mais fina, não instalar `scikit-learn` para checagem cruzada da
   implementação manual de TF-IDF/MDS aqui usada.
4. **[Resolvida — ver Seção 5] Frequência relativa pura, não TF-IDF.** Uma segunda base ponderada por TF-IDF
   foi construída em paralelo à base original (que permanece válida e não foi substituída) e usada para o
   dendrograma e os dois mapas de similaridade descritos na Seção 5. Lacuna residual: a suavização de IDF
   escolhida (`smooth_idf`, padrão scikit-learn) é uma opção razoável, não a única válida — variantes como
   IDF probabilístico ou BM25 não foram testadas como alternativa.
5. **Tradução como limitação estrutural.** Quatro dos seis documentos (os dois chineses e, em menor medida,
   o PBIA) chegam ao corpus como texto traduzido para o inglês por terceiros — uma limitação que nenhuma
   etapa metodológica elimina, apenas registra, e que é inerente ao desenho da pesquisa, não a esta análise
   específica.

## 7. Onde encontrar cada artefato

- **Notebook executado** (código, tabelas e gráficos completos): `Análise Conjunta/analise_geral.ipynb`
- **Registro técnico auditável** (todas as decisões, com justificativa individual): `Análise Conjunta/registro_analise_conjunta.md`
- **Este relatório:** `Análise Conjunta/relatorio_analise_conjunta.md`
