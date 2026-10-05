---
name: skill_análise_individual
description: Etapa 02 do fluxo de análise dos Planos Nacionais de IA (IC FAPESP 2026). Orienta a análise de UM plano por vez (PBIA, Winning the Race, UE, China etc.), em notebook Jupyter, a partir do JSON produzido pela skill 01. Produz visualizações e interpretações com metodologia explícita, escolhas registradas e fragilidades apontadas.
etapa: 02
versao: 1.0
data: 2026-10-04
---

# Skill de Análise Individual — Planos Nacionais de IA (Etapa 02)

> **Aplicação obrigatória.** Toda análise de um plano **isolado** (não comparado) feita na pasta `notebooks/A_IC FAPESP 2026/Planos Nacionais de IA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook de análise individual, o agente lê esta skill e a cumpre por inteiro. Esta skill **não** cobre análises conjuntas ou comparativas: essas são regidas pela skill 03 (`skill_análise_comparativa.md`).

> ⚠️ **OS COMANDOS DO PESQUISADOR SÃO OBEDECIDOS EM ÚLTIMA INSTÂNCIA.** Eles prevalecem sobre qualquer regra desta skill. Visualizações, relatórios e outras saídas **só vão para a pasta `resultados/` por comando do pesquisador** (seção 4.4).

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **Planos Nacionais de IA** reúne as estratégias e os planos governamentais de IA, como o Plano Brasileiro de Inteligência Artificial (**PBIA**), o plano dos Estados Unidos (*Winning the Race*), o da União Europeia e o da China, entre outros. A análise de cada plano serve para conhecer o seu vocabulário, os seus enfoques e as suas ênfases, como base para a comparação entre os planos e para situar a política brasileira em relação às demais, em especial à chinesa.

Todos os planos estão **em inglês**, e a análise é feita nesse idioma.

As visualizações e interpretações produzidas aqui podem ser incorporadas a relatórios científicos. Por isso, **cada gráfico precisa ser metodologicamente defensável, reprodutível e acompanhado da explicação de como foi construído**.

### 1.2. Rigor acadêmico e transparência metodológica

- Cada comando pedido é executado conforme esta skill e o pedido do pesquisador.
- **Toda** escolha metodológica (pré-processamento, listas de palavras, recortes, limiares, parâmetros, tipo de gráfico, tratamentos de inflação) fica **visível no código** e **descrita em texto** no próprio notebook, logo após a visualização que ela afeta.
- O procedimento é **reprodutível**: o mesmo JSON, com os mesmos parâmetros, gera os mesmos números e as mesmas figuras. Procedimentos aleatórios (como o bootstrap) usam semente fixa e registrada.
- Se o **comando** do pesquisador for ambíguo, contraditório ou não estiver coberto por esta skill, o agente **para e pergunta**. Não deve presumir.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/Planos Nacionais de IA/`.
- **Insumos permitidos:** (a) o JSON do plano produzido pela **skill 01** (`<SIGLA>_extracao.json`, um único por plano); (b) as instruções do pesquisador.
- O **relatório de extração** (`relatorios_extracao/`) **não é insumo** desta etapa: ele é apenas informativo para o pesquisador e não é consultado nem levado em consideração.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - investigar outras páginas, pastas ou notebooks do repositório para buscar padrões de resposta, resultados anteriores ou modelos de análise. O pipeline e a estrutura de notebook descritos aqui reproduzem o fluxo já validado pelo pesquisador na pasta `Declarações IA`, e tudo o que o agente precisa está nesta skill;
  - se espelhar em outras resoluções, análises ou interpretações sobre o mesmo plano, sejam do repositório, da internet ou do conhecimento prévio do modelo;
  - usar informações externas para completar, contextualizar ou interpretar o texto;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O JSON da skill 01 é **somente leitura**: o notebook nunca o modifica.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| 01 | Extração do texto essencial de cada plano para JSON + relatório informativo | `skill_extração.md` |
| **02** | **Análise individual de cada plano, em notebook, com visualizações e interpretações** | **esta skill** |
| 03 | Análise conjunta e comparativa dos planos, com normalização relativa | `skill_análise_comparativa.md` |

A Etapa 02 parte **exclusivamente** do JSON da Etapa 01. Se o JSON do plano não existir, o agente não faz a análise: informa ao pesquisador que a skill 01 precisa ser executada antes.

### 1.5. Autoridade do pesquisador e autonomia do agente

- As **ordens e comandos do pesquisador são a decisão final e são obedecidos em última instância** sobre o que analisar, como analisar e o que manter. O agente não altera decisões do pesquisador por conta própria nem omite uma ordem recebida. Quando uma ordem tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.
- Dentro do que o pesquisador não definiu, o agente tem **autonomia** para compreender o que infla a análise, o que deve estar nela e o que não deve, e para aplicar os tratamentos necessários, conforme a seção 3.5. Toda decisão tomada com essa autonomia fica visível no código, é explicada no texto e pode ser revertida pelo pesquisador com a alteração de um parâmetro.

---

## 2. Objetivos

### 2.1. Objetivo principal

Analisar, em notebook Jupyter (`.ipynb`), o conteúdo extraído de **um** plano e produzir **visualizações gráficas e interpretações** que permitam conhecer os termos mais comuns, o enfoque dado pelo texto, as proporções entre temas e as ênfases do documento. A metodologia adotada, as escolhas feitas e as fragilidades identificadas ficam explícitas.

### 2.2. Objetivos específicos

1. **Verificar o insumo:** confirmar que o JSON vem da skill 01, está íntegro e corresponde ao plano pedido.
2. **Descrever o documento:** extensão, número de unidades (títulos internos, parágrafos e itens), tokens e vocabulário.
3. **Identificar os termos mais frequentes** (lemas), com frequência absoluta, frequência por 1.000 tokens e grau de dispersão ao longo do texto.
4. **Identificar expressões recorrentes** de duas palavras (bigramas).
5. **Atender** as demandas definidas pelo comando do pesquisador.
6. **Interpretar** cada visualização com base nos valores obtidos, apontando método, escolhas e fragilidades.

---

## 3. Diretrizes para a análise

### 3.1. Insumo: o que entra e o que não entra

Do JSON da skill 01 são usados **apenas**:

| Campo | Uso |
|---|---|
| `document.title` e `document.subtitle` | Identificação do plano nas tabelas, figuras e textos. **Entram na contagem por padrão** (`INCLUIR_TITULO_NA_CONTAGEM = True`), como unidade 0, porque título e subtítulo fazem parte do texto essencial do plano. Retirá-los é decisão do pesquisador |
| `sections[].text` | **Conteúdo analisado**: o texto integral e literal de cada unidade (títulos internos, parágrafos e itens de lista) |
| `sections[].type` | Filtro: os títulos internos (`heading`) **entram por padrão** (`INCLUIR_TITULOS_INTERNOS = True`) |
| `sections[].category` | Filtro: todas as categorias **entram por padrão** (`CATEGORIAS_EXCLUIDAS = []`). Retirar `Foreword`, `Executive summary`, `Box` ou `Annex` é decisão do pesquisador |
| `sections[].id` | Apenas como **índice de posição** da unidade no documento (para gráficos de distribuição), nunca como conteúdo |
| `sections[].path` | Apenas como **agrupador estrutural** (por exemplo, extensão ou frequências por pilar ou eixo), quando o pesquisador pedir, nunca como conteúdo |
| `extraction` | Apenas para **verificação** de integridade |

**Fica fora da análise o conteúdo periférico:** numeração (`number`), nível (`level`), página (`page`) e os demais metadados (`issuer`, `date`, `period` etc.). Se o pesquisador quiser incluir algum desses campos, a inclusão deve ser pedida expressamente e registrada.

Todo filtro aplicado é informado no perfil do documento: quantas unidades e quantos tokens ele retirou.

### 3.2. Análise integral do conteúdo

- A análise cobre **todo** o texto das unidades selecionadas. É proibido amostrar, cortar, resumir ou analisar apenas parte do documento.
- Recortes do tipo "os *N* mais frequentes" servem **apenas à visualização**. A tabela completa, com todos os termos, fica disponível para exportação.
- Quando houver **empate no ponto de corte** de um recorte, o notebook informa quantos e quais termos empatados ficaram de fora e qual critério de desempate foi usado (ordem alfabética).
- É proibido abreviar, truncar ou parafrasear trechos citados do documento. Citações são literais.

### 3.3. Pré-processamento padrão

O pré-processamento é o mesmo para todos os planos, para que os resultados sejam comparáveis na skill 03. Qualquer alteração é feita nos parâmetros do notebook e registrada.

| Passo | Procedimento | Justificativa |
|---|---|---|
| 1 | Processamento de cada unidade com o spaCy, modelo `en_core_web_sm` | Tokenização, lematização e classes gramaticais com ferramenta aberta e documentada |
| 2 | Reunião de palavras compostas com hífen (*multi-stakeholder*, *human-centric*, *state-of-the-art*) em um só token | Evita que o composto seja contado como palavras soltas, o que distorce frequências |
| 3 | **Token** = sequência de letras (com hífen interno ou sigla com pontos, como *U.S.*). Números, pontuação e símbolos não são tokens | Define com precisão o denominador das taxas |
| 4 | Lematização e conversão para minúsculas (ex.: *risks* → *risk*) | Agrupa flexões de uma mesma palavra |
| 5 | Correções explícitas de lematização, listadas no código (ex.: *datum* → *data*) | Corrige erros conhecidos do modelo sem intervenção oculta |
| 6 | **Tokens de conteúdo** = substantivos, nomes próprios, verbos, adjetivos e advérbios, fora da lista de *stopwords* do spaCy (verificada pelo lema) e com pelo menos 2 caracteres | Concentra a análise em palavras com carga semântica |

- Listas de *stopwords* adicionais ou de palavras a manter ficam em listas editáveis no código, vazias por padrão.
- A lista de *stopwords* do spaCy inclui palavras como *may*, *must*, *should*, *will* e *can*, que ficam fora da contagem de conteúdo e são tratadas à parte, como modais (seção 3.4).
- *AI* e *artificial intelligence* não são unificados por padrão, porque isso alteraria o texto. A unificação, se desejada, é feita por regra explícita na configuração.

### 3.4. Medidas adotadas

| Medida | Definição |
|---|---|
| Frequência absoluta | Número de ocorrências do lema no documento |
| Frequência por 1.000 tokens | (frequência ÷ total de tokens do documento) × 1.000. O denominador é o total de tokens (palavras), **incluindo** *stopwords* |
| Alcance | Número e percentual de unidades em que o lema aparece |
| Dispersão | DP de Gries (2008), normalizado por Lijffijt & Gries (2012): 0 = ocorrências proporcionais ao tamanho das unidades; 1 = concentração máxima |
| Bigramas | Pares de tokens de conteúdo **adjacentes no texto original**, na mesma frase, sem pontuação entre eles. Não se formam pares artificiais pela remoção de *stopwords* |
| Intervalo de confiança | Bootstrap por reamostragem de **unidades**, com semente fixa. A reamostragem por unidade respeita a dependência entre palavras do mesmo parágrafo |
| Modais | Verbos modais identificados pela etiqueta gramatical (`MD`), por 1.000 tokens |

Medidas que dependem fortemente da extensão do texto (como a razão tipo/token) **não** são usadas como indicador de riqueza vocabular sem a devida ressalva.

### 3.5. Autonomia na análise: o que infla, o que deve estar e o que não deve

O agente deve **compreender** o plano analisado e reconhecer o que faria um termo pesar mais do que o plano efetivamente o emprega. A regra que separa os casos é:

- **Inflação é artefato.** É tudo o que multiplica um termo sem que o plano o tenha escrito mais vezes no seu texto: resíduos de extração que tenham escapado da skill 01 (cabeçalhos repetidos, marcadores de nota colados a palavras, rótulos estruturais repetidos como unidades próprias, trechos duplicados), ou um bloco de texto idêntico repetido em várias unidades por razão de diagramação. A inflação **deve ser tratada** pelo agente, com autonomia.
- **Frequência real é resultado.** Termos que o plano de fato repete muito, inclusive termos genéricos como *ai*, o nome do próprio país ou a sigla do plano, **não são inflação**. Eles ficam na análise e são comentados na interpretação e nas fragilidades. Retirá-los é decisão do pesquisador.

**Como tratar a inflação.**
1. Usar os parâmetros da configuração (`UNIDADES_EXCLUIDAS`, com o `id` e o motivo de cada unidade retirada; `STOPWORDS_ADICIONAIS`; `CORRECOES_DE_LEMA`), nunca intervenções escondidas no meio do código.
2. Explicar o tratamento no bloco *Método e escolhas* da visualização afetada, com o efeito numérico (quantas unidades ou ocorrências foram retiradas).
3. Quando a inflação vier do próprio JSON, informar ao pesquisador que a extração pode ser corrigida pela skill 01. O notebook não altera o JSON.

**Limites da autonomia.** O agente não usa a autonomia para retirar termos ou trechos que produzam resultados incômodos, para confirmar hipóteses da pesquisa ou para contrariar uma escolha já feita pelo pesquisador.

### 3.6. Vieses proibidos

- Escolher termos, categorias, recortes ou parâmetros para **confirmar uma hipótese** da pesquisa.
- Destacar apenas os resultados convenientes ou omitir os inconvenientes.
- Ajustar limiares ou listas depois de ver os resultados sem registrar a alteração e o motivo.
- Atribuir ao plano intenções, motivações ou posições políticas que não estejam no texto.
- Tratar frequência como importância política sem a devida mediação interpretativa.

### 3.7. Regras para as visualizações

1. **Padrão acadêmico:** fonte de pelo menos 9 pt, figuras gravadas em PNG (300 dpi) e PDF quando houver comando de gravação.
2. **Cor fixa por plano** (`COR_DOCUMENTO`), a mesma em todos os notebooks da pasta. Paleta inicial, editável pelo pesquisador: Brasil `#2E9E4F` (verde), Estados Unidos `#1F3F8F` (azul-escuro), União Europeia `#EDB120` (amarelo), China `#B2182B` (vermelho). Planos do mesmo país ou bloco recebem tons da mesma cor. Como verde e vermelho se confundem para leitores com daltonismo, os gráficos com mais de um plano identificam cada um também por rótulo direto ou marcador.
3. **Números no padrão brasileiro**, com vírgula decimal e ponto de milhar, sem alterar os valores.
4. Cada gráfico tem título, eixos com a unidade de medida e legenda quando necessária. Barras começam em zero. Não se usa deslocamento aleatório (*jitter*) nem qualquer recurso que altere os valores.
5. Os termos aparecem como estão no texto do plano (em inglês), sem tradução nos rótulos.
6. Abaixo de cada gráfico, o notebook imprime uma **síntese factual** com os números principais.
7. Cada seção de visualização indica a sua origem: *"Visualização prévia: base inicial para a construção de novos gráficos"* ou *"Visualização construída por comando do pesquisador"*.

---

## 4. Protocolo de operação

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar** que o JSON do plano existe e passa nas verificações de integridade.
3. **Configurar** os parâmetros na célula de configuração do notebook. Nenhum parâmetro fica espalhado pelo código.
4. **Examinar** o texto processado em busca de inflação (seção 3.5) e tratá-la, se houver.
5. **Gerar** cada visualização com a sua tabela correspondente.
6. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
7. **Informar** ao pesquisador, de forma breve, o que foi produzido, os tratamentos de inflação aplicados e os pontos que exigem a atenção dele.

### 4.2. Estrutura obrigatória do notebook

Nome do arquivo: `Análise_<SIGLA>.ipynb`, gravado nesta pasta.

1. **Apresentação** (primeira célula, em Markdown): título, projeto, etapa, insumo e o aviso de que as visualizações são prévias e de que nada vai para `resultados/` sem comando do pesquisador. Em seguida: **1. Do que se trata**; **2. Finalidade**; **3. Insumo e recorte do conteúdo**; **4. Método** (visão geral, em tabela); **5. Transparência das escolhas**; **6. Princípios** (vínculo com esta skill e ausência de comparação).
2. **Configuração:** todos os parâmetros editáveis, comentados, em uma única célula. No mínimo: `SIGLA`, `ARQUIVO_JSON`, `NOME_SAIDA`, `VERSAO_SAIDA`, `SALVAR_SAIDAS = False`, `SOBRESCREVER = False`, `INCLUIR_TITULO_NA_CONTAGEM = True`, `INCLUIR_TITULOS_INTERNOS = True`, `CATEGORIAS_EXCLUIDAS = []`, `UNIDADES_EXCLUIDAS = {}`, `IDIOMA_ESPERADO = "en"`, `MODELO_SPACY = "en_core_web_sm"`, `CLASSES_DE_CONTEUDO`, `TAMANHO_MINIMO_LEMA = 2`, `STOPWORDS_ADICIONAIS = []`, `STOPWORDS_MANTIDAS = []`, `CORRECOES_DE_LEMA`, `TOP_N_LEMAS = 25`, `TOP_N_DISPERSAO = 15`, `TOP_N_BIGRAMAS = 20`, `FREQ_MINIMA_BIGRAMA = 2`, `N_BOOTSTRAP = 2000`, `NIVEL_CONFIANCA = 0.95`, `SEMENTE = 2026`.
3. **Ambiente, estilo e funções:** restrição de pasta (o notebook só roda de dentro de `Planos Nacionais de IA`), pasta de saída versionada, estilo das figuras e funções do pipeline, comentadas e **idênticas em todos os notebooks da pasta**.
4. **Carregamento e verificação** do JSON, que interrompe a execução se: o arquivo não existir; não tiver sido produzido pela skill 01 para este corpus (`extraction.skill` e `extraction.corpus`); os `id` não forem sequenciais; houver unidade vazia; o número de unidades divergir do registrado; faltar o título; ou o idioma não for `en`. O SHA-256 do JSON é exibido.
5. **Pré-processamento e perfil** do documento, com os filtros aplicados e os lemas de classes de conteúdo descartados pela lista de *stopwords*, com as suas frequências.
6. **Análises e visualizações**, cada uma seguida do bloco de texto da seção 4.3. Conjunto-padrão: extensão das unidades textuais; lemas de conteúdo mais frequentes; distribuição dos lemas ao longo do documento; expressões recorrentes (bigramas). Outras análises (por exemplo, extensão e frequências por pilar ou eixo, categorias temáticas com intervalo de confiança, modais) entram **por comando do pesquisador**.
7. **Registro de execução** (parâmetros, versões do ambiente, *hash* do insumo, lista de saídas) e **síntese** final.

### 4.3. Bloco de texto após cada visualização

Logo após cada visualização, o notebook contém:

| Item | Conteúdo |
|---|---|
| **Método e escolhas** | O que foi medido, como, com quais parâmetros, e quais escolhas foram feitas (inclusive as do pesquisador e os tratamentos de inflação) |
| **Como ler** | Instrução objetiva de leitura do gráfico |
| **Interpretação** | Texto breve que interpreta o gráfico **com base nos valores efetivamente obtidos** |
| **Fragilidades e ajustes possíveis** | Limitações do método ou dos dados e ajustes que poderiam ser considerados, **quando necessário** |

**Regras da interpretação:**
- É redigida **somente depois da execução**, a partir dos números exibidos. Antes da execução, o campo fica marcado como pendente. Nunca se escreve interpretação antecipada ou "esperada".
- Cita os valores que a sustentam (frequências, taxas, intervalos).
- Separa **observação** (o que os números mostram) de **inferência** (o que eles podem sugerir), e marca a inferência como tal.
- Não extrapola para além do plano analisado e não faz comparações com outros planos (isso é tarefa da skill 03).

### 4.4. Pasta `resultados`

- Visualizações, tabelas, relatórios e quaisquer outras saídas **só vão para a pasta `resultados/` quando o pesquisador der o comando**, e da forma que ele exigir.
- **Nenhuma** visualização é adicionada automaticamente a `resultados/`. Sem o comando, o notebook apenas exibe as visualizações e as tabelas, sem gravá-las (`SALVAR_SAIDAS = False`).
- Quando houver gravação, as saídas vão para `resultados/<SIGLA>/<VERSAO_SAIDA>/`. Resultados anteriores nunca são sobrescritos: uma nova execução com mudanças usa uma nova versão (`v2`, `v3`, …).
- Versões interativas (site) de um gráfico só são feitas por comando do pesquisador, com os mesmos dados do notebook, e o link é registrado no próprio notebook.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final e são obedecidos em última instância.
2. **Autonomia com transparência:** o agente reconhece e trata o que infla a análise, sempre por parâmetros visíveis e com explicação no texto.
3. **Fidelidade ao insumo:** analisa-se apenas o texto das unidades do JSON da skill 01, sem cortes, abreviações ou acréscimos.
4. **Transparência total:** todo método e toda escolha estão no código **e** na descrição em texto que acompanha a visualização.
5. **Reprodutibilidade:** parâmetros centralizados, semente fixa, versões registradas, *hash* do insumo registrado.
6. **Neutralidade:** nenhum instrumento ou parâmetro é escolhido para produzir um resultado desejado.
7. **Não inventar dados:** nenhum valor é estimado, ajustado ou arredondado para "melhorar" um gráfico. Divergências inesperadas são explicadas, não corrigidas à força.
8. **Exclusividade das fontes:** só se usa o JSON do plano. O relatório de extração e os materiais de outras pastas não são consultados.
9. **Fragilidades declaradas:** limitações conhecidas (erros de lematização, ambiguidade de termos, efeito da estrutura do plano nas contagens) são sempre declaradas.
10. **Escopo individual:** esta skill não compara planos. Toda comparação segue a skill 03.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma visualização sem método explícito, com escolhas ocultas ou com interpretação não sustentada pelos dados compromete a validade dos resultados publicados. O padrão exigido é o máximo.
