# Skill AGY - Categorização e Agrupamento em Blocos Temáticos das Notas Brasil-China (MRE - Passo 2)

## 1. Contexto, Escopo de Atuação e Regra de Disparo Condicional

Esta **Skill** estabelece o protocolo técnico, analítico e metodológico de alto rigor para o agente **AntiGravity (AGY)** na execução do **Passo 2** da análise diplomática: a **categorização e divisão em blocos temáticos** das notas oficiais entre Brasil e China pré-selecionadas no Passo 1 (`skillagy_mre`).

### 1.1. Regra Estrita de Execução Condicional e Independência
- **Execução Sob Demanda Exclusiva**: Esta Skill representa um procedimento autônomo e complementar. O agente AGY **NÃO deve ler, nem executar este Passo 2 automaticamente** durante a execução da Skill do Passo 1 (`skillagy_mre.md`).
- **Gatilho de Acionamento**: Esta Skill será ativada **UNICAMENTE** quando o usuário solicitar expressamente a realização do Passo 2, categorização ou agrupamento em blocos das notas filtradas (ex: *"Execute o Passo 2 da análise MRE"*, *"Categorize as notas do MRE em blocos"*, ou *"Execute a skill de blocos temáticos MRE"*).
- **Independência Operacional**: Quando o usuário solicitar apenas o que a Skill `skillagy_mre` faz, o agente executará **estritamente** a triagem e filtragem do Passo 1. Quando o usuário solicitar a execução desta nova Skill, o agente executará a categorização e o agrupamento em blocos descritos neste documento.

### 1.2. Restrição Estrita de Ambiente e Pastas
- O agente deve atuar **EXCLUSIVAMENTE** na pasta:
  `notebooks/Análise Agente AntiGravity/`
- **Proibição de Alteração de Outras Pastas**: O agente **não deve** realizar leitura, escrita ou modificação em nenhuma outra pasta fora deste diretório.
- **Insumos de Entrada**: O insumo principal para este Passo 2 é obrigatoriamente o arquivo **`analise_mre.json`** (gerado no Passo 1 dentro da pasta `notebooks/Análise Agente AntiGravity/`). Não deve buscar conteúdos externos ou em outros diretórios.

---

## 2. Objetivos da Análise

### 2.1. Objetivo Principal
Classificar e agrupar as notas diplomáticas contidas em `analise_mre.json` em **blocos temáticos/categorias analíticas coesas**, reconhecendo que, embora todas as notas selecionadas abordem o relacionamento diplomático Brasil-China, elas possuem **finalidades, contextos, temas centrais e conteúdos qualitativamente distintos**.

### 2.2. Objetivos Específicos
1. **Mapeamento e Classificação Temática**: Identificar a finalidade primária e o contexto diplomático de cada nota, atribuindo-a a um bloco temático bem definido.
2. **Preservação e Estruturação em JSON**: Gerar um arquivo JSON (**`blocos_analise_mre.json`**) que reorganize as notas por blocos/categorias, preservando integralmente o texto e os metadados originais de cada nota.
3. **Construção de Relatório Qualitativo e Quantitativo em CSV**: Gerar um relatório em CSV (**`relatorio_blocos_mre.csv`**) que sintetize a distribuição dos blocos, apresente as estatísticas gerais de categorização e detalhe a justificativa analítica para a alocação de cada nota em seu respectivo bloco.

---

## 3. Diretrizes para Formação dos Blocos Temáticos e Categorização

### 3.1. Razoamento Analítico para Separação em Blocos
Na construção da análise do conteúdo presente nas notas do MRE, evidencia-se que existem notas que, ainda que reforcem o relacionamento diplomático entre Brasil e China, possuem finalidades, contextos institucionais e conteúdos específicos muito diferentes (por exemplo, um comunicado de transição energética versus um acordo de agronegócio ou uma declaração geopolítica do BRICS).

### 3.2. Blocos Temáticos de Referência
O agente deve analisar criticamente o texto de cada nota em `analise_mre.json` e alocá-la em um dos blocos temáticos principais (mas não limitados a):

1. **Comércio Exterior, Agronegócio e Economia**: Acordos comerciais, exportações/importações, barreiras sanitárias/alfandegárias, facilitação de comércio e cooperação agropecuária.
2. **Ciência, Tecnologia, Inovação e Espacial**: Cooperação em satélites (CBERS), inteligência artificial, semicondutores, biotecnologia, pesquisa científica e ecossistemas tecnológicos.
3. **Transição Energética, Meio Ambiente e Mudança do Clima**: Descarbonização, energia renovável (solar, eólica, hidrogênio verde), preservação ambiental e posições em conferências climáticas (COP).
4. **Cooperação Multilateral e Governança Global**: Atuação articulada e posições conjuntas no âmbito do BRICS, G20, ONU, OMC e fóruns internacionais multilaterais.
5. **Infraestrutura, Investimentos e Finanças**: Parcerias logísticas, financiamento de projetos de infraestrutura, investimentos diretos, conectividade (ex: Rota da Seda) e transações em moedas locais.
6. **Defesa, Segurança Internacional e Geopolítica**: Diálogos de paz, cooperação em defesa, segurança cibernética, não proliferação e posicionamentos geopolíticos regionais ou globais.
7. **Educação, Cultura e Intercâmbio Humano**: Acordos acadêmicos, bolsas de estudo, difusão cultural, turismo e integração entre universidades/institutos de pesquisa.
8. **Declarações Políticas, Visitas de Estado e Diplomacia Institucional**: Visitas bilaterais de alto nível (Chefes de Estado/Governo), mecanismos institucionais de consulta de alto nível (ex: COSBAN) e atos diplomáticos gerais.

> *Nota Flexível*: Caso surja um padrão temático relevante que não se enquadre perfeitamente nas categorias acima, o agente poderá propor e registrar um novo bloco temático devidamente fundamentado.

### 3.3. Critério de Alocação e Notas Multitemáticas
- **Bloco Primário (Categoria Principal)**: Toda nota é alocada no bloco correspondente à sua finalidade central ou engrenagem diplomática condutora.
- **Mapeamento de Temas Secundários**: Se uma nota abordar múltiplos temas relevantes (ex: visita oficial que firma acordos de comércio e tecnologia), ela será alocada no bloco primário predominante, e os temas secundários serão detalhados no relatório CSV.

---

## 4. Protocolo de Operação e Entregáveis do Agente AGY

### 4.1. Escopo de Trabalho
- Operação **estritamente restrita à pasta `notebooks/Análise Agente AntiGravity/`**.
- Leitura do arquivo de entrada: `analise_mre.json`.
- Geração dos arquivos de saída diretamente no mesmo diretório.

### 4.2. Entregável 1: Arquivo JSON (`blocos_analise_mre.json`)
- **Estrutura por Blocos**: Reorganização hierárquica das notas por categoria/bloco temático.
- **Estrutura Interna de Cada Bloco**:
  ```json
  {
    "nome_bloco": "Nome do Bloco Temático",
    "descricao_bloco": "Síntese da finalidade e contexto do bloco",
    "total_notas": 0,
    "notas": [
      { /* Objeto integral da nota preservando todos os campos e textos originais */ }
    ]
  }
  ```
- **Preservação do Conteúdo Original**: Todo o conteúdo de cada nota mantida no JSON reorganizado deve permanecer **100% fiel ao original** (título, data, parágrafos, links e metadados). Proibido realizar resumos, cortes ou edições nos textos das notas originais.

### 4.3. Entregável 2: Relatório CSV (`relatorio_blocos_mre.csv`)
- **Métricas Gerais de Categorização**:
  - Total de notas categorizadas.
  - Quantidade de blocos temáticos criados.
  - Distribuição quantitativa e percentual de notas por bloco.
- **Detalhamento Registro a Registro**:
  - `id_nota` / `titulo_nota`: Identificação clara da nota.
  - `data_nota`: Data de publicação.
  - `bloco_tematico_principal`: Nome do bloco primário atribuído.
  - `temas_secundarios`: Outros temas/tópicos presentes na nota.
  - `justificativa_categorizacao`: Explicação clara do motivo da alocação no bloco.
  - `palavras_chave`: Tópicos/termos de destaque.
  - `revisao_necessaria`: Indicação de `Sim` ou `Não` para casos com ambiguidade temática ou necessidade de validação do pesquisador.

---

## 5. Regras de Qualidade e Rigor Acadêmico

1. **Rigor de Análise Conteudística**: A alocação em blocos deve ser fruto de leitura densa e analítica do texto diplomático, evitando classificações superficiais baseadas apenas em palavras isoladas.
2. **Auditabilidade de Imprecisões**: Em notas transversais com forte sobreposição temática, o agente deve justificar a escolha do bloco primário no CSV e sinalizar `Revisão Necessária: Sim`.
3. **Integridade textual**: O conteúdo das notas dentro do arquivo JSON `blocos_analise_mre.json` deve manter 100% de integridade com o arquivo `analise_mre.json`.
