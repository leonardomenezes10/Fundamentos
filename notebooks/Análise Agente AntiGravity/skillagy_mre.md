# Skill AGY - Análise Diplomática do Relacionamento Brasil-China (MRE)

## 1. Contexto e Escopo de Atuação
Esta **Skill** estabelece o protocolo técnico, analítico e metodológico de alto rigor para o agente **AntiGravity (AGY)** na execução de triagens e análises de documentos diplomáticos do **Ministério das Relações Exteriores (MRE / Itamaraty)**.

### 1.1. Restrição Estrita de Ambiente e Pastas
- O agente deve atuar **EXCLUSIVAMENTE** na pasta:
  `notebooks/Análise Agente AntiGravity/`
- **Proibição de Alteração de Outras Pastas**: O agente **não deve** realizar leitura, escrita ou modificação em nenhuma outra pasta fora deste diretório (como `notebooks/MRE` ou a raiz do repositório).
- **Insumos de Entrada**: O agente usufruirá **apenas** dos arquivos JSON e dados disponibilizados diretamente pelo usuário dentro da pasta `notebooks/Análise Agente AntiGravity/`. Não deve buscar conteúdos externos ou em outros diretórios.

### 1.2. Foco Temático Exclusivo
O objetivo desta Skill é extrair **APENAS NOTAS QUE INDICAM O RELACIONAMENTO DIPLOMÁTICO ENTRE BRASIL E CHINA**, contemplando interações nas esferas **bilaterais e multilaterais** (ex: parcerias bilaterais, atuação no BRICS, G20, ONU, desde que o foco da interação Brasil-China seja relevante).

**NÃO SERÃO INCLUÍDAS** notas que relacionam a questão entre Brasil e China de modo superficial, ocasional, pontual, em meras listagens geográficas ou sem centralidade diplomática.

---

## 2. Objetivos da Análise

### 2.1. Objetivo Principal
Identificar e selecionar as notas oficiais do MRE que tratam do relacionamento diplomático entre Brasil e China no campo diplomático de forma relevante, não superficial, e importante para análise acadêmica. A partir disso, o agente deve selecionar todas as notas que atendam a este critério e excluir todas as que não atendam, criando um novo arquivo JSON chamado **`analise_mre.json`**.

### 2.2. Objetivos Específicos
1. **Mapeamento de Citações**: Identificar quais notas, dentre todas as presentes no JSON selecionado na pasta, mencionam a China no contexto diplomático com o Brasil.
2. **Identificação Temática**: Identificar a temática central da nota abordada (ex: Direitos Humanos, Tecnologia/Inovação, Segurança Internacional, Meio Ambiente, Comércio Exterior, Integração Regional, etc.).
3. **Contabilidade e Razão de Descarte**: Quantificar quantas notas de quantas notas foram selecionadas do total. Registrar quantas notas mencionavam a China de forma insuficiente ou superficial para entrar nessa análise, detalhando o motivo explícito da retirada.
4. **Construção dos Entregáveis**:
   - Construir um arquivo JSON (**`analise_mre.json`**) contendo **apenas** as notas selecionadas como ideais, mantendo a estrutura e o texto original completo das notas.
   - Construir um relatório em **CSV** com as métricas da seleção e a justificativa de exclusão de cada nota descartada.

---

## 3. Diretrizes para a Análise (Critérios de Relevância Diplomática Brasil-China)

Para garantir a validade acadêmica e científica da pesquisa, o agente deve aplicar rigorosamente os seguintes critérios de inclusão e exclusão:

### 3.1. O que É RELEVANTE para Inclusão
A nota deve ser **SELECIONADA** se atender integralmente aos seguintes aspectos:
- **Centralidade e Importância do Agente**: A China precisa ser um agente de importância central na nota, e a narrativa/análise deve girar em torno da relação, negociação, alinhamento, cooperação ou controvérsia entre Brasil e China.
- **Relevância Diplomática Bilateral ou Multilateral**: Encontros bilaterais de alto nível, atos e acordos assinados entre Brasil e China, ou posicionamentos conjuntos e estratégicos em fóruns multilaterais (ex: atuações articuladas Brasil-China no BRICS, G20 ou conferências da ONU).
- **Densidade do Conteúdo**: Notícias e comunicados que abordam agendas econômicas, tecnológicas, geopolíticas ou ambientais de impacto real entre os dois países.

### 3.2. O que NÃO DEVE ENTRAR na Análise (Critérios de Descarte)
A nota deve ser **EXCLUÍDA** se apresentar qualquer um dos seguintes cenários:
- **Menções Superficiais ou Ocasionais**: A China é citada apenas pontualmente em meio a uma lista genérica de países (ex: *"o embaixador recebeu representantes da China, França e Argentina"* ou *"exportações para vários destinos, incluindo a China"* sem aprofundamento diplomático).
- **Ausência de Eixo Temático Brasil-China**: Notas em que a relação diplomática bilateral/multilateral não é o tema nem a engrenagem condutora do texto.
- **Citações Meramente Protocolares ou Geográficas**: Menções acessórias que não adicionam substância ao estudo da política externa Brasil-China.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO**: Caso uma nota não atinja este padrão de relevância e seja incluída indevidamente, haverá distorção no trabalho acadêmico e científico. O rigor deve ser máximo. Na dúvida analítica sobre a pertinência diplomática, a nota deve ter sua imprecisão destacada explicitamente no relatório CSV.

---

## 4. Protocolo de Operação e Entregáveis do Agente AGY

### 4.1. Escopo de Trabalho
- Operação **restrita à pasta `notebooks/Análise Agente AntiGravity`**.
- O agente usufruirá exclusivamente do arquivo JSON adicionado pelo usuário nessa pasta.
- Não buscar conteúdos fora nem realizar alterações em outras pastas do repositório.

### 4.2. Entregável 1: Arquivo JSON (`analise_mre.json`)
- **Conteúdo**: Formado **apenas** pelas notas aprovadas na seleção de relevância Brasil-China.
- **Preservação de Conteúdo Original**: Todo o conteúdo de cada nota mantida no novo JSON deve estar **exatamente como originalmente estava no JSON antigo** (incluindo título, data, parágrafos, links e metadados). Não fazer cortes, resumos ou alterações no texto das notas selecionadas.
- Excluir do arquivo todas as notas descartadas.

### 4.3. Entregável 2: Relatório CSV (`relatorio_analise_mre.csv`)
- **Estatísticas Gerais**:
  - Total de notas analisadas.
  - Total de notas selecionadas (relevantes).
  - Total de notas descartadas (superficiais / irrelevantes).
- **Detalhamento das Notas**:
  - Identificador e Título da nota.
  - Status de Seleção (`Selecionada` / `Descartada`).
  - Temática Central (quando selecionada).
  - Justificativa do Descarte (quando descartada, explicando claramente por que a citação foi considerada insuficiente ou irrelevante).
  - Indicação Expressa de Revisão (`Revisão Necessária: Sim/Não`) e destaque das imprecisões ou pontos que exigem validação humana.

---

## 5. Regras de Qualidade e Rigor Acadêmico

1. **Vedação Absoluta a Generalizações e Imperfeições**: Por se tratar de uma pesquisa acadêmica e científica de alta relevância, são proibidas respostas incompletas, erros metodológicos, generalizações vazias ou seleções imprecisas.
2. **Auditoria de Imprecisões**: Qualquer potencial dúvida, ambiguidade linguística ou margem de interpretação no texto original da nota deve ser **expressamente indicada no CSV**, destacando o item que necessita de revisão humana.
3. **Fidelidade dos Dados Selecionados**: A integridade textual dos registros selecionados no arquivo `analise_mre.json` deve ser mantida em 100%, sem perda de dados.
