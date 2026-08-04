# Skill02 – Análise e Visualização Gráfica de Documentos

## Objetivo

Esta skill constitui o **Passo 02** do fluxo de trabalho de análise de documentos sobre inteligência artificial. Sua função é, a partir de um JSON já extraído pela Skill01 e indicado pelo usuário, produzir análises e visualizações gráficas sobre o conteúdo desse documento (ou, no caso da pasta "Análise Conjunta", sobre o conjunto de documentos de todos os países/blocos), conforme a demanda específica feita pelo usuário em cada prompt.

## Independência das skills

O Passo 01 (Skill01) e o Passo 02 (Skill02) são **isolados e independentes entre si**. Cada skill só é executada quando explicitamente demandada pelo usuário, e a leitura de uma não implica a leitura ou execução automática da outra. Não presumir, encadear ou antecipar a execução de uma skill a partir da outra: é o usuário quem determina, a cada momento, qual passo deve ser dado.

## Princípio de rigor acadêmico

Este trabalho integra uma pesquisa acadêmica séria e deve ser conduzido com o mais alto grau de rigor e perfeccionismo metodológico. Não são aceitáveis:

- Generalizações de qualquer tipo sobre o conteúdo do documento;
- Erros metodológicos graves, sejam eles de extração, classificação ou organização dos dados;
- Simplificações do texto original, sob qualquer justificativa de concisão ou clareza;
- Omissão de trechos por julgamento de relevância pessoal — a decisão sobre o que é substância do texto e o que é material acessório segue apenas os critérios objetivos descritos abaixo, nunca a impressão subjetiva de quem executa a extração;
- Adição de conteúdo, interpretação, resumo ou complemento que não exista literalmente no documento original.

A fidelidade integral ao texto-fonte é o critério inegociável de qualidade desta etapa.

## Regra geral de escopo

Toda atividade realizada no âmbito desta skill deve se restringir **exclusivamente** ao conteúdo da pasta `notebooks/Análise Documentos IA` e de suas subpastas (`Brasil`, `China`, `Estados Unidos`, `Europa`, `Índia`, `Análise Conjunta`).

- Não utilizar como referência, exemplo, padrão ou fonte de dados qualquer material, script, notebook ou documento localizado fora dessa pasta.
- Cada execução desta skill deve considerar apenas os documentos e arquivos já existentes dentro de "Análise Documentos IA".
- Essa restrição vale tanto para leitura de contexto quanto para gravação de resultados: nada deve ser lido de, nem escrito em, pastas fora de "Análise Documentos IA" durante a execução desta skill.

## Gatilho

Esta skill é executada sempre que o usuário indicar um JSON (produzido pela Skill01) presente em uma das pastas `Brasil`, `China`, `Estados Unidos`, `Europa`, `Índia` ou `Análise Conjunta`, e demandar uma análise ou visualização gráfica sobre o seu conteúdo.

## Protocolo de uso do JSON

Do JSON indicado pelo usuário, devem ser utilizados exclusivamente os campos:

- `titulo`
- `pais_ou_bloco`
- `texto_completo` — campo mais importante, base de toda a análise e visualização.

Os campos `elementos_descartados`, `data_extracao`, `data_publicacao` e `fonte` **não devem ser utilizados**. Em particular, o conteúdo de `elementos_descartados` não pode, sob nenhuma hipótese, entrar na análise do que for pedido — trata-se apenas de um registro de auditoria da extração (Skill01), sem qualquer valor analítico para este passo.

A extração do conteúdo de `texto_completo` para fins de análise deve ser feita de forma **integral, sem alterações e sem simplificações**. Nenhuma paráfrase, resumo prévio ou corte de trechos é permitido antes da análise — a leitura do texto que fundamenta os gráficos deve corresponder ao texto completo tal como registrado no JSON.

## Objetivos e finalidades da skill

1. **Construção de visualizações gráficas.** O objetivo principal é utilizar o conteúdo extraído (`texto_completo`) para produzir análises e visualizações gráficas sobre aquilo que for demandado pelo usuário.

2. **Ausência de gráfico fixo.** Não há nenhum tipo de gráfico específico ao qual esta skill esteja presa. A cada demanda, deve-se ler esta skill (Passo 02) e construir o gráfico ou a análise que o usuário pedir, adaptando a visualização ao que for solicitado.

3. **Rigor acadêmico na construção dos gráficos.** É preciso seguir rigor acadêmico, reduzir as possíveis lacunas deixadas pelos gráficos, reduzir imprecisões, não cometer erros metodológicos e ter o máximo de precisão possível na construção das visualizações.
   - Cada documento possui um tamanho diferente. Em análises comparadas entre documentos de países/blocos distintos, é necessário considerar essas distorções e realizar uma **análise relativa** (proporcional, normalizada) em vez de comparações diretas de valores absolutos. Essa comparação relativa é feita exclusivamente na pasta **Análise Conjunta**.
   - Na análise individual de cada documento, feita nas pastas de cada país (`Brasil`, `China`, `Estados Unidos`, `Europa`, `Índia`), essa preocupação com a comparação relativa **não se aplica**, pois há apenas um documento sendo analisado.

4. **Descrição e análise de cada visualização produzida.** A cada nova visualização criada, deve-se sempre apresentar:
   - O que foi construído;
   - Como ler o gráfico;
   - Uma interpretação do gráfico à luz do conteúdo do documento;
   - Quais ajustes poderiam ser feitos para melhorar a visualização;
   - Quais erros metodológicos ou fraquezas o gráfico eventualmente incorre, se existirem.

5. **Escopo do JSON por pasta.**
   - Nas pastas de país (`Brasil`, `China`, `Estados Unidos`, `Europa`, `Índia`), a análise e os gráficos devem utilizar **somente** o JSON atribuído àquele país e indicado pelo usuário. Nenhum outro JSON deve ser analisado além daquele indicado.
   - Na pasta **Análise Conjunta**, devem ser utilizados, de forma conjunta, os JSONs de todos os blocos (`Brasil`, `China`, `Estados Unidos`, `Europa`, `Índia`), para construir uma análise gráfica conjunta de todos os documentos, sempre respeitando a demanda específica feita pelo usuário.

## Resultado esperado

Gráficos acadêmicos, com visualização clara, fiéis ao conteúdo presente nos documentos analisados, e com o maior rigor acadêmico possível, voltados a um estudo de Relações Internacionais — cada um deles acompanhado da descrição, leitura, interpretação, possíveis ajustes e eventuais fraquezas metodológicas, conforme o item 4 acima.
