# Skill AGY - Análise Conteudística, Temática e Vocabular por Blocos Diplomáticos (MRE - Passo 3)

## 1. Contexto, Escopo de Atuação e Regra de Disparo Condicional

Esta **Skill** estabelece o protocolo técnico, analítico e metodológico de alto rigor para o agente **AntiGravity (AGY)** na execução do **Passo 3** da análise diplomática: a **análise de conteúdo, decomposição temática e mapeamento de vocabulário** dentro dos blocos temáticos de notas oficiais entre Brasil e China (gerados nos Passos 1 e 2: `skillagy_mre` e `skillagy_mre_blocos`).

### 1.1. Regra Estrita de Execução Condicional e Independência
- **Execução Sob Demanda Exclusiva**: Esta Skill representa um procedimento autônomo e complementar. O agente AGY **NÃO deve ler, nem executar este Passo 3 automaticamente** durante a execução da Skill do Passo 1 (`skillagy_mre.md`) ou do Passo 2 (`skillagy_mre_blocos.md`).
- **Gatilho de Acionamento**: Esta Skill será ativada **UNICAMENTE** quando o usuário solicitar expressamente a realização do Passo 3, a análise de conteúdo, tópicos, temáticas ou vocabulários dos blocos (ex: *"Execute o Passo 3 da análise MRE"*, *"Analise as temáticas e vocabulários do bloco de Tecnologia"*, *"Faça a análise de conteúdo dos blocos MRE"*, ou *"Execute a skill de análise de tópicos e vocabulários por blocos"*).
- **Flexibilidade de Escopo por Demanda no Prompt**: O agente deve passar pelo(s) bloco(s) que forem especificamente demandados no prompt do usuário (por exemplo, analisar apenas um bloco específico como *"Comércio Exterior, Agronegócio e Economia"*, um conjunto de blocos selecionados, ou todos os blocos do arquivo, conforme solicitado).
- **Independência Operacional**: O agente deve manter a independência estrita entre os passos. O Passo 3 opera consumindo os insumos gerados nas etapas anteriores sem reescrever ou alterar as filtragens prévias.

### 1.2. Restrição Estrita de Ambiente e Pastas
- O agente deve atuar **EXCLUSIVAMENTE** na pasta:
  `notebooks/Análise Agente AntiGravity/`
- **Proibição de Alteração de Outras Pastas**: O agente **não deve** realizar leitura, escrita ou modificação em nenhuma outra pasta fora deste diretório.
- **Insumos de Entrada**: O insumo principal para este Passo 3 é obrigatoriamente o arquivo **`blocos_analise_mre.json`** (ou `analise_mre.json`), localizado na pasta `notebooks/Análise Agente AntiGravity/`. Não deve buscar conteúdos externos ou em outros diretórios.

---

## 2. Objetivos da Análise

### 2.1. Objetivo Principal
Decompor e mensurar o conteúdo interno do(s) bloco(s) temático(s) demandado(s) pelo usuário, identificando as **principais temáticas, tópicos específicos e vocabulários diplomáticos** empregados no(s) texto(s). A análise deve calcular a distribuição percentual desses assuntos **em cada nota individual do bloco** e de forma **consolidada no bloco como um todo**, apresentando uma justificativa metodológica detalhada para a quantificação e classificação.

### 2.2. Objetivos Específicos
1. **Mapeamento Temático e Taxonomia Vocabular**: Identificar e categorizar os eixos temáticos, tópicos secundários/emergentes e termos técnicos/diplomáticos presentes nas notas do(s) bloco(s) analisado(s).
2. **Mensuração Percentual por Nota**: Determinar a porcentagem (%) de presença relativa de cada temática/assunto no texto de cada nota pertencente ao bloco.
3. **Mensuração Percentual Consolidada por Bloco**: Calcular a porcentagem (%) agregada de cada assunto considerando o bloco em sua totalidade.
4. **Descrição e Fundamentação Metodológica**: Explicar detalhadamente a metodologia utilizada para a classificação, extração de vocabulário, ponderação semântica e cálculo das porcentagens.
5. **Construção do Entregável CSV**: Gerar o relatório estruturado em CSV (**`relatorio_analise_conteudo_blocos.csv`**) compilando os dados por nota, os dados consolidados do bloco e as justificativas metodológicas.

---

## 3. Diretrizes para Análise Temática, Tópicos e Vocabulário

### 3.1. Taxonomia Expandida de Temáticas, Tópicos e Vocabulários de Referência
O agente deve examinar os textos das notas utilizando uma taxonomia rica e abrangente, contemplando (mas não se limitando a) as seguintes grandes temáticas e suas respectivas famílias vocabulares:

1. **Tecnologia, Inovação e Espaço**:
   - *Tópicos*: Satélites de sensoriamento remoto (CBERS), Inteligência Artificial, Semicondutores, Biotecnologia, Conectividade 5G/6G, Cibersegurança, Pesquisa Científica, Ecossistemas de Inovação.
   - *Vocabulário Típico*: *tecnologia, inovação, satélite, CBERS, sensoriamento remoto, inteligência artificial, dados, cibernético, semicondutores, pesquisa e desenvolvimento (P&D), biotecnologia, ecossistema tecnológico*.
2. **Governança Global e Reforma Institucional**:
   - *Tópicos*: Reforma do Conselho de Segurança da ONU, Arquitetura Financeira Internacional (FMI/Banco Mundial), Multilateralismo Inclusivo, Normatização e Direito Internacional.
   - *Vocabulário Típico*: *governança global, reforma institucional, Conselho de Segurança, arquitetura financeira, multilateralismo, Nações Unidas, ordem internacional, legitimidade, representatividade*.
3. **Cooperação Bilateral e Sul-Sul**:
   - *Tópicos*: Parceria Estratégica Global, Transferência de Tecnologia, Capacitação Técnica, Cooperação Horizontal, Projetos Conjuntos Brasil-China.
   - *Vocabulário Típico*: *cooperação bilateral, Sul-Sul, parceria estratégica, complementaridade, capacitação, transferência de tecnologia, benefício mútuo, ganhos compartilhados*.
4. **Multilateralismo e Fóruns Plurilaterais**:
   - *Tópicos*: Atuação conjunta no BRICS, G20, Fórum CELAC-China, COSBAN, Reuniões Ministeriais e Cúpulas Internacionais.
   - *Vocabulário Típico*: *BRICS, G20, CELAC, COSBAN, convergência posicional, alinhamento multilateral, declaração conjunta, cúpula, consenso*.
5. **Direitos Humanos e Direito Internacional Humanitário**:
   - *Tópicos*: Proteção de civis em conflitos armados, Convenções de Genebra, Assistência Humanitária, Direitos Fundamentais, Combate à Fome e à Pobreza.
   - *Vocabulário Típico*: *direitos humanos, direito internacional humanitário, Convenções de Genebra, proteção de civis, assistência humanitária, dignidade humana, combate à pobreza*.
6. **Economia, Comércio Exterior e Agronegócio**:
   - *Tópicos*: Pauta exportadora (soja, carne bovina, aves, minério), barreiras tarifárias e não tarifárias, sanidade animal (febre aftosa), salvaguardas comerciais, defesa comercial, fluxos de trocas.
   - *Vocabulário Típico*: *comércio exterior, exportação, importação, balança comercial, agronegócio, sanidade animal, febre aftosa, salvaguardas, alfandegário, protocolo sanitário, MAPA, MDIC*.
7. **Transição Energética, Meio Ambiente e Mudança do Clima**:
   - *Tópicos*: Descarbonização, matriz elétrica renovável (solar, eólica, hidrelétrica), hidrogênio verde, preservação florestal/biodiversidade, metas da COP e Acordo de Paris.
   - *Vocabulário Típico*: *transição energética, descarbonização, energia renovável, hidrogênio verde, mudança do clima, COP, conservação ambiental, sustentabilidade, biodiversidade, crédito de carbono*.
8. **Infraestrutura, Investimentos e Finanças**:
   - *Tópicos*: Conectividade logística, ferrovias e portos, Rota da Seda (Belt and Road), Transações em Moedas Locais (Real/Renminbi), Investimento Direto Externo (IDE), Novo Banco de Desenvolvimento (NDB/Banco do BRICS).
   - *Vocabulário Típico*: *infraestrutura, investimento direto, conectividade, moedas locais, liquidação em yuan/real, NDB, financiamento, desenvolvimento de infraestrutura, concessões*.
9. **Defesa, Segurança Internacional e Geopolítica**:
   - *Tópicos*: Diálogos de Paz, Solução Diplomática de Conflitos (ex: crise na Ucrânia, Oriente Médio), Não Proliferação Nuclear, Segurança Cibernética, Estabilidade Geopolítica.
   - *Vocabulário Típico*: *segurança internacional, paz, solução pacífica, mediação, geopolítica, não proliferação, desarmamento, estabilidade regional, consulta de segurança*.
10. **Educação, Cultura e Intercâmbio Humano**:
    - *Tópicos*: Celebração do Ano Cultural, Bolsas de Estudo, Facilitação/Isenção de Vistos, Parcerias entre Universidades e Institutos de Pesquisa, Turismo.
    - *Vocabulário Típico*: *intercâmbio cultural, Ano Cultural, turismo, vistos, bolsas de estudo, cooperação acadêmica, laços entre os povos, difusão cultural*.
11. **Diplomacia Institucional e Atos Bilaterais**:
    - *Tópicos*: Visitas de Estado, Encontros Presidenciais, Reuniões de Chanceleres, Assinatura de Atos e Memorandos de Entendimento (MoUs).
    - *Vocabulário Típico*: *visita de Estado, atos bilaterais, memorando de entendimento, comunicado conjunto, diplomacia presidencial, chanceler, relacionamento diplomático*.
12. **Saúde Pública e Cooperação Sanitária**:
    - *Tópicos*: Vigilância epidemiológica, insumos farmacêuticos (IFA), protocolos de saúde pública, cooperação em pesquisa médica.
    - *Vocabulário Típico*: *saúde pública, vigilância sanitária, insumos farmacêuticos, vacinas, pesquisa médica, cooperação sanitária*.

> *Nota de Expansão Taxonômica*: O agente deve manter sensibilidade analítica para identificar novos tópicos ou subtemas emergentes que surjam no texto das notas e que enriqueçam a categorização vocabular.

---

## 4. Metodologia de Análise Conteudística e Cálculo Percentual

Para garantir total rigor científico, reprodutibilidade e transparência, o agente aplicará a seguinte metodologia de quantificação:

### 4.1. Análise Lexical-Semântica e Ponderação de Densidade
1. **Segmentação e Contagem Lexical**: Para cada nota, o agente identifica a contagem de termos, n-gramas e famílias vocabulares associados a cada uma das temáticas mapeadas.
2. **Ponderação por Centralidade Semântica**: Além da frequência bruta de termos, o agente pondera a importância do tópico no contexto da nota (título, primeiro parágrafo e objetivo principal da nota recebem peso relativo maior que menções acessórias).
3. **Normalização Percentual por Nota**: A soma dos pesos/densidades de todas as temáticas identificadas na nota equivale a 100%. A porcentagem de um assunto $T_i$ na nota $N$ é dada por:
   $$\text{Porcentagem Temática na Nota } (P_{N, T_i}) = \left( \frac{\text{Peso Semântico do Tópico } T_i \text{ na Nota } N}{\sum_{k} \text{Peso Semântico do Tópico } T_k \text{ na Nota } N} \right) \times 100$$

### 4.2. Cálculo Consolidado da Porcentagem no Bloco como um Todo
A porcentagem consolidada de uma temática $T_i$ no bloco $B$ reflete o peso acumulado daquele assunto no conjunto total de notas do bloco:
$$\text{Porcentagem Consolidada no Bloco } (P_{B, T_i}) = \left( \frac{\sum_{N \in B} \text{Peso Semântico do Tópico } T_i \text{ na Nota } N}{\sum_{N \in B} \sum_{k} \text{Peso Semântico do Tópico } T_k \text{ na Nota } N} \right) \times 100$$

### 4.3. Justificativa e Descrição Metodológica no Relatório
Para cada nota e para a consolidação do bloco, o relatório deve conter uma **descrição textual detalhada da metodologia**, incluindo:
- Termos vocabulares específicos encontrados.
- Lógica de atribuição das densidades temáticas.
- Fórmula e valores numéricos utilizados para derivar as porcentagens.
- Contexto de relevância diplomática do tópico no documento.

---

## 5. Protocolo de Operação e Entregável do Agente AGY

### 5.1. Escopo de Trabalho
- Operação **estritamente restrita à pasta `notebooks/Análise Agente AntiGravity/`**.
- Leitura do arquivo de entrada de blocos: `blocos_analise_mre.json` (ou `analise_mre.json`).
- Processamento dos blocos solicitados na instrução do usuário.
- Geração do relatório CSV diretamente no diretório `notebooks/Análise Agente AntiGravity/`.

### 5.2. Entregável Principal: Relatório CSV (`relatorio_analise_conteudo_blocos.csv`)

O arquivo CSV gerado deve estruturar as análises tanto em nível individual de nota quanto em nível consolidado do bloco, contendo as seguintes colunas obrigatórias:

1. **`nivel_registro`**: Define se a linha representa uma análise individual (`Nota`) ou uma síntese agregada (`Consolidado Bloco`).
2. **`bloco_analisado`**: Nome do bloco temático ao qual a nota ou consolidação pertence.
3. **`id_nota`**: Identificador interno da nota (preenchido para nível `Nota`; vazio para `Consolidado Bloco`).
4. **`num_nota`**: Número oficial da nota no MRE (preenchido para nível `Nota`; vazio para `Consolidado Bloco`).
5. **`data_nota`**: Data de publicação da nota no MRE.
6. **`titulo_nota`**: Título oficial da nota (para nível `Nota`) ou indicação de consolidação (ex: *"Consolidado Geral do Bloco: [Nome do Bloco]"*).
7. **`topico_tematica`**: Nome da temática/tópico analisado (ex: *"Tecnologia, Inovação e Espaço"*, *"Economia, Comércio Exterior e Agronegócio"*, etc.).
8. **`porcentagem_presenca`**: Valor percentual formatado (ex: `45.5%`) indicando a presença da temática na nota ou no bloco.
9. **`vocabularios_chave_identificados`**: Lista das palavras-chave, termos diplomáticos e expressões mais relevantes identificados para aquele tópico na nota/bloco.
10. **`justificativa_metodologica`**: Descrição detalhada e explícita explicando como foi feita a classificação, os termos contabilizados, a fórmula de ponderação semântica e a derivação do valor percentual.
11. **`revisao_necessaria`**: Indicação de `Sim` ou `Não` para sinalizar notas ou tópicos com ambiguidades vocabulares que exijam verificação pelo pesquisador acadêmico.

---

## 6. Regras de Qualidade e Rigor Acadêmico

1. **Rigor Científico e Transparência Metodológica**: São proibidas porcentagens estimadas sem fundamentação textual. Toda fração percentual informada no CSV deve ser devidamente justificada com base no vocabulário e na densidade temática demonstrados no texto oficial do MRE.
2. **Auditabilidade e Reprodutibilidade**: Qualquer pesquisador deve ser capaz de ler a coluna `justificativa_metodologica` e compreender com clareza exata como as porcentagens da nota e do bloco foram calculadas.
3. **Integridade de Dados e Preservação de Contexto**: A extração vocabular não deve descontextualizar as declarações diplomáticas. Os termos devem ser interpretados dentro do sentido diplomático oficial das notas do Itamaraty.
