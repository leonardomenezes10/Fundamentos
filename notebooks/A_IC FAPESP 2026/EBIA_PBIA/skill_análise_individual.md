---
name: skill_análise_individual
description: Etapa 02 do fluxo de análise da EBIA e do PBIA (IC FAPESP 2026). Orienta a análise de UM JSON por vez (EBIA, PBIA sem anexos ou PBIA com anexos), em português, em notebook Jupyter, a partir do JSON produzido pela skill 01. Produz visualizações e interpretações com metodologia explícita, escolhas registradas e fragilidades apontadas, sem relatórios em arquivo.
etapa: 02
versao: 1.0
data: 2026-10-09
---

# Skill de Análise Individual — EBIA e PBIA (Etapa 02)

> **Aplicação obrigatória.** Toda análise de um documento **isolado** (não comparado) feita na pasta `notebooks/A_IC FAPESP 2026/EBIA_PBIA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook de análise individual, o agente lê esta skill e a cumpre por inteiro. Esta skill **não** cobre a análise conjunta da EBIA e do PBIA: essa é regida pela skill 03 (`skill_análise_conjunta.md`).

> ⚠️ **O COMANDO DO PESQUISADOR É A DECISÃO FINAL E É OBEDECIDO EM ÚLTIMA INSTÂNCIA.** Ele prevalece sobre qualquer regra desta skill e sobre qualquer escolha do agente: o que analisar, como analisar, com que recortes e parâmetros, e o que manter. O agente propõe e aponta riscos, mas não decide no lugar do pesquisador. Visualizações e tabelas **só vão para a pasta `resultados/` por comando dele** (seção 4.4), e nenhum relatório é produzido.

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **EBIA_PBIA** reúne a Estratégia Brasileira de Inteligência Artificial (**EBIA**) e o Plano Brasileiro de Inteligência Artificial (**PBIA**). O PBIA está em dois recortes definidos pelo pesquisador: **sem** e **com** os Anexos 1 e 2 (ações de impacto imediato e ações estruturantes). A análise de cada JSON serve para conhecer o vocabulário, os enfoques e as ênfases do documento, como base para a análise conjunta e para a compreensão da política brasileira de governança da IA.

Os dois documentos estão **em português**, e a análise é feita nesse idioma, sem tradução.

As visualizações e interpretações produzidas aqui podem ser incorporadas a relatórios científicos. Por isso, **cada gráfico precisa ser metodologicamente defensável, reprodutível e acompanhado da explicação de como foi construído**.

### 1.2. Rigor acadêmico e transparência metodológica

- Cada comando pedido é executado conforme esta skill e o pedido do pesquisador.
- **Toda** escolha metodológica (pré-processamento, listas de palavras, recortes, limiares, parâmetros, tipo de gráfico, tratamentos de inflação) fica **visível no código** e **descrita em texto** no próprio notebook, logo após a visualização que ela afeta.
- O procedimento é **reprodutível**: o mesmo JSON, com os mesmos parâmetros, gera os mesmos números e as mesmas figuras. Procedimentos aleatórios (como o bootstrap) usam semente fixa e registrada.
- Se o **comando** do pesquisador for ambíguo, contraditório ou não estiver coberto por esta skill, o agente **para e pergunta**. Não deve presumir.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/EBIA_PBIA/`.
- **Insumos permitidos:** (a) o JSON produzido pela **skill 01** desta pasta (`EBIA_extracao.json`, `PBIA_sem_anexos_extracao.json` ou `PBIA_com_anexos_extracao.json`); (b) os comandos do pesquisador.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - usar o PBIA em inglês da pasta `Planos Nacionais de IA` ou qualquer outra extração destes documentos que exista no repositório;
  - investigar outras páginas, pastas ou notebooks do repositório para buscar padrões de resposta, resultados anteriores ou modelos de análise. O pipeline e a estrutura de notebook descritos aqui reproduzem o fluxo já validado pelo pesquisador, adaptado ao português, e tudo o que o agente precisa está nesta skill;
  - se espelhar em outras resoluções, análises ou interpretações sobre a EBIA ou o PBIA, sejam do repositório, da internet ou do conhecimento prévio do modelo;
  - usar informações externas para completar, contextualizar ou interpretar o texto;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O JSON da skill 01 é **somente leitura**: o notebook nunca o modifica.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| 01 | Extração do texto essencial de cada documento para JSON | `skill_extração.md` |
| **02** | **Análise individual de cada JSON, em notebook, com visualizações e interpretações** | **esta skill** |
| 03 | Análise conjunta da EBIA e do PBIA, com normalização relativa | `skill_análise_conjunta.md` |

A Etapa 02 parte **exclusivamente** do JSON da Etapa 01. Se o JSON pedido não existir, o agente não faz a análise: informa ao pesquisador que a skill 01 precisa ser executada antes.

### 1.5. Autoridade do pesquisador e autonomia do agente

Ordem de precedência, da mais forte para a mais fraca:

1. **o comando atual do pesquisador;**
2. **as decisões que o pesquisador já tomou para estes notebooks** (parâmetros que fixou, recortes que pediu, termos que mandou manter ou retirar);
3. as regras desta skill;
4. o julgamento do agente, apenas no que os itens anteriores não definem.

- As ordens e os comandos do pesquisador são a **decisão final** sobre o que analisar, como analisar e o que manter. O agente não altera decisões do pesquisador por conta própria, não reverte um parâmetro que ele fixou e não omite uma ordem recebida. Quando uma ordem tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.
- Mudanças pedidas em gráficos existentes são **acrescentadas, e não substituídas** (seção 4.5).
- Dentro do que o pesquisador não definiu, o agente tem **autonomia** para compreender o que infla a análise, o que deve estar nela e o que não deve, e para aplicar os tratamentos necessários, conforme a seção 3.5. Toda decisão tomada com essa autonomia fica visível no código, é explicada no texto e pode ser revertida pelo pesquisador com a alteração de um parâmetro.

---

## 2. Objetivos

### 2.1. Objetivo principal

Analisar, em notebook Jupyter (`.ipynb`), o conteúdo de **um** JSON (EBIA, PBIA sem anexos ou PBIA com anexos) e produzir **visualizações gráficas e interpretações** que permitam conhecer os termos mais comuns, o enfoque dado pelo texto, as proporções entre temas e as ênfases do documento. A metodologia adotada, as escolhas feitas e as fragilidades identificadas ficam explícitas.

### 2.2. Objetivos específicos

1. **Verificar o insumo:** confirmar que o JSON vem da skill 01 desta pasta, está íntegro e corresponde ao documento e ao recorte pedidos.
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
| `document.title` e `document.subtitle` | Identificação do documento nas tabelas, figuras e textos. **Não entram na contagem por padrão** (`INCLUIR_TITULO_NA_CONTAGEM = False`), porque vêm da capa, que o pesquisador excluiu da análise. Incluí-los é decisão do pesquisador |
| `sections[].text` | **Conteúdo analisado**: o texto integral e literal de cada unidade (títulos internos, parágrafos e itens de lista) |
| `sections[].type` | Filtro: os títulos internos (`heading`) **entram por padrão** (`INCLUIR_TITULOS_INTERNOS = True`) |
| `sections[].category` | Filtro: todas as categorias **entram por padrão** (`CATEGORIAS_EXCLUIDAS = []`). Retirar `Foreword`, `Executive summary`, `Box` ou `Annex` é decisão do pesquisador |
| `sections[].label` | **Nunca é conteúdo.** Os rótulos repetitivos retirados na extração, por comando do pesquisador, não voltam para a contagem. Podem servir de agrupador (por exemplo, frequências por campo das fichas das ações: *Desafio*, *Metas*, *Impactos esperados*) quando o pesquisador pedir |
| `sections[].id` | Apenas como **índice de posição** da unidade no documento (para gráficos de distribuição), nunca como conteúdo |
| `sections[].path` | Apenas como **agrupador estrutural** (por exemplo, por eixo ou por anexo), quando o pesquisador pedir, nunca como conteúdo |
| `extraction` | Apenas para **verificação** de integridade e identificação do recorte (`cut`, `page_range`) |

**Fica fora da análise o conteúdo periférico:** numeração (`number`), rótulo (`label`), nível (`level`), página (`page`) e os demais metadados (`issuer`, `date`, `period` etc.). Se o pesquisador quiser incluir algum desses campos, a inclusão deve ser pedida expressamente e registrada.

Todo filtro aplicado é informado no perfil do documento: quantas unidades e quantos tokens ele retirou.

### 3.2. Análise integral do conteúdo

- A análise cobre **todo** o texto das unidades selecionadas. É proibido amostrar, cortar, resumir ou analisar apenas parte do documento.
- Recortes do tipo "os *N* mais frequentes" servem **apenas à visualização**. A tabela completa, com todos os termos, fica disponível para exportação.
- **Empates no ponto de corte.** Nas seções-padrão, o desempate é alfabético, e o notebook informa quantos e quais termos empatados ficaram de fora. **Quando o pesquisador pedir um recorte "top N"**, o corte é ampliado até incluir todos os termos empatados com o *N*-ésimo, como ele já determinou: o notebook informa quantos termos foram acrescentados e qual é o primeiro que fica de fora, e marca no gráfico onde termina o *N* pedido.
- É proibido abreviar, truncar ou parafrasear trechos citados do documento. Citações são literais.

### 3.3. Pré-processamento padrão (português)

O pré-processamento é o mesmo para os três JSONs, para que os resultados sejam comparáveis na skill 03. Qualquer alteração é feita nos parâmetros do notebook e registrada.

| Passo | Procedimento | Justificativa |
|---|---|---|
| 1 | Processamento de cada unidade com o spaCy, modelo `pt_core_news_sm` | Tokenização, lematização e classes gramaticais em português, com ferramenta aberta e documentada |
| 2 | Reunião de palavras compostas com hífen (*bem-estar*, *pós-graduação*, *público-privado*, *técnico-científico*) em um só token, **exceto** as formas verbais com pronome átono em ênclise ou mesóclise (*tornar-se*, *desenvolvê-la*, *far-se-á*), identificadas pela lista editável `PRONOMES_CLITICOS`: nelas, o verbo fica separado do pronome | Evita que o composto seja contado como palavras soltas, sem impedir a lematização do verbo; o pronome sai como palavra gramatical |
| 3 | **Token** = palavra do texto: sequência de letras (inclusive acentuadas e *ç*), com hífen interno. Siglas (*IA*, *MCTI*, *LGPD*) são tokens. Contrações (*do*, *na*, *pelo*) contam como um token, como aparecem no texto. Números, pontuação e símbolos (*R$*, *%*) não são tokens | Define com precisão o denominador das taxas |
| 4 | Lematização e conversão para minúsculas, **sem retirar acentos** (*sistemas* → *sistema*; *públicas* → *público*) | Agrupa as flexões de uma mesma palavra. Os acentos distinguem palavras diferentes (*é*/*e*, *público*/*publico*) |
| 5 | Correções explícitas de lematização, listadas no código (`CORRECOES_DE_LEMA`) | Corrige erros do modelo sem intervenção oculta. Erros evidentes (lema inexistente, troca de classe) são corrigidos pelo agente e explicados. Escolhas de sentido, como manter *dados* (no sentido de informação) separado de *dado*, são do pesquisador |
| 6 | **Tokens de conteúdo** = substantivos, nomes próprios, verbos, adjetivos e advérbios, fora da lista de *stopwords* do spaCy para o português (verificada pelo lema), fora dos verbos modais (`LEMAS_MODAIS`) e com pelo menos 2 caracteres | Concentra a análise em palavras com carga semântica |

> ⚠️ **A lista de *stopwords* do spaCy para o português retira palavras de conteúdo.** Na versão instalada no ambiente (spaCy 3.8, 416 entradas), ela não traz só palavras gramaticais: inclui substantivos, adjetivos e verbos com carga semântica e frequentes em textos de política de IA, como *sistema*, *estado*, *conselho*, *apoio*, *área*, *nível*, *valor*, *grupo*, *parte*, *relação*, *questão*, *forma*, *tempo*, *povo*, *poder*, *usar*, *novo*, *grande* e *possível*. Aplicada como está, ela tira esses termos da contagem sem aviso (por exemplo, *sistema* em "sistemas de IA"). Por isso:
> 1. a lista é aplicada como está por padrão, para manter um procedimento documentado e igual para os três JSONs;
> 2. o perfil do documento exibe, **antes de qualquer visualização**, todos os lemas de classes de conteúdo descartados pela lista, com as frequências;
> 3. o agente avisa o pesquisador dos descartados com frequência relevante;
> 4. manter algum deles (`STOPWORDS_MANTIDAS`) é **decisão do pesquisador**, registrada na configuração e aplicada igualmente aos três JSONs.

- A lista também traz formas flexionadas (*deve*, *podem*, *foram*). Como a verificação é feita pelo lema, para que todas as flexões de uma palavra recebam o mesmo tratamento, essas entradas só têm efeito quando o lematizador devolve a própria forma.
- Verbos de sentido leve que **não** estão na lista (por exemplo, *haver*) contam como conteúdo. Se pesarem nos resultados, o agente aponta, e o pesquisador decide.
- **Títulos com iniciais maiúsculas** (como os títulos das ações: *Guias Brasileiros de IA Responsável*) tendem a ser marcados pelo modelo como nome próprio e a ficar sem lematização, o que divide uma palavra em duas contagens (*guias* e *guia*). O agente confere os pares divididos e os corrige por `CORRECOES_DE_LEMA`, com uma regra que vale igualmente para os três JSONs.
- **Verbos modais:** `LEMAS_MODAIS = ["dever", "poder"]`, identificados pelo lema com classe `VERB` ou `AUX`, ficam fora da contagem de conteúdo e são medidos à parte (seção 3.4). O substantivo *poder* (*poder público*) não é modal; ele sai da contagem apenas porque está na lista de *stopwords*, e o pesquisador pode mantê-lo pela `STOPWORDS_MANTIDAS` sem trazer de volta o verbo.
- `STOPWORDS_ADICIONAIS` e `STOPWORDS_MANTIDAS` são listas editáveis no código, vazias por padrão.
- *IA* e *inteligência artificial* não são unificados por padrão, porque isso alteraria o texto. A unificação, se desejada, é feita por regra explícita na configuração.
- Como todos os lemas passam para minúsculas, as siglas aparecem assim nas tabelas e figuras (*ia*, *mcti*).

### 3.4. Medidas adotadas

| Medida | Definição |
|---|---|
| Frequência absoluta | Número de ocorrências do lema no documento |
| Frequência por 1.000 tokens | (frequência ÷ total de tokens do documento) × 1.000. O denominador é o total de tokens (palavras), **incluindo** *stopwords* |
| Alcance | Número e percentual de unidades em que o lema aparece |
| Dispersão | DP de Gries (2008), normalizado por Lijffijt & Gries (2012): 0 = ocorrências proporcionais ao tamanho das unidades; 1 = concentração máxima |
| Bigramas | Pares de tokens de conteúdo **adjacentes no texto original**, na mesma frase, sem pontuação entre eles. Não se formam pares artificiais pela remoção de *stopwords*. Por isso, expressões ligadas por preposição (*governança de dados*) não formam bigrama, e os pares mais comuns em português tendem a ser substantivo + adjetivo (*inteligência artificial*, *setor público*) |
| Intervalo de confiança | Bootstrap por reamostragem de **unidades**, com semente fixa. A reamostragem por unidade respeita a dependência entre palavras do mesmo parágrafo |
| Modais | Ocorrências dos lemas de `LEMAS_MODAIS` com classe `VERB` ou `AUX`, por 1.000 tokens. O português não tem etiqueta gramatical própria para modais, como o `MD` do inglês |

Medidas que dependem fortemente da extensão do texto (como a razão tipo/token) **não** são usadas como indicador de riqueza vocabular sem a devida ressalva.

### 3.5. Autonomia na análise: o que infla, o que deve estar e o que não deve

O agente deve **compreender** o documento analisado e reconhecer o que faria um termo pesar mais do que o documento efetivamente o emprega. A regra que separa os casos é:

- **Inflação é artefato.** É tudo o que multiplica um termo sem que o documento o tenha escrito mais vezes no seu texto: resíduos de extração que tenham escapado da skill 01 (cabeçalhos repetidos, marcadores de nota colados a palavras, rótulos repetitivos que ficaram no texto, trechos duplicados), ou um bloco de texto idêntico repetido em várias unidades por razão de diagramação. A inflação **deve ser tratada** pelo agente, com autonomia.
- **Frequência real é resultado.** Termos que o documento de fato repete muito, inclusive termos genéricos como *ia*, *brasil*, *plano* ou *estratégia*, **não são inflação**. Eles ficam na análise e são comentados na interpretação e nas fragilidades. Retirá-los é decisão do pesquisador.
- **Repetição de conteúdo mantida na extração.** Conteúdo que se repete de forma padronizada, mas que a extração manteve por ser texto do documento (por exemplo, valores idênticos nas fichas das ações dos anexos, como *iniciativa única* em *Componentes da ação*), não é retirado pelo agente: o notebook mostra o seu peso nas contagens, e o agente o aponta ao pesquisador, que decide.

**Como tratar a inflação.**
1. Usar os parâmetros da configuração (`UNIDADES_EXCLUIDAS`, com o `id` e o motivo de cada unidade retirada; `STOPWORDS_ADICIONAIS`; `CORRECOES_DE_LEMA`), nunca intervenções escondidas no meio do código.
2. Explicar o tratamento no bloco *Método e escolhas* da visualização afetada, com o efeito numérico (quantas unidades ou ocorrências foram retiradas).
3. Quando a inflação vier do próprio JSON, informar ao pesquisador que a extração pode ser corrigida pela skill 01. O notebook não altera o JSON.

**Limites da autonomia.** O agente não usa a autonomia para retirar termos ou trechos que produzam resultados incômodos, para confirmar hipóteses da pesquisa ou para contrariar uma escolha já feita pelo pesquisador.

### 3.6. Vieses proibidos

- Escolher termos, categorias, recortes ou parâmetros para **confirmar uma hipótese** da pesquisa.
- Destacar apenas os resultados convenientes ou omitir os inconvenientes.
- Ajustar limiares ou listas depois de ver os resultados sem registrar a alteração e o motivo.
- Atribuir ao documento intenções, motivações ou posições políticas que não estejam no texto.
- Tratar frequência como importância política sem a devida mediação interpretativa.

### 3.7. Regras para as visualizações

1. **Padrão acadêmico:** fonte de pelo menos 9 pt, figuras gravadas em PNG (300 dpi) e PDF quando houver comando de gravação.
2. **Cor fixa por documento** (`COR_DOCUMENTO`), a mesma em todos os notebooks da pasta. Paleta inicial, editável pelo pesquisador, em tons de verde (Brasil), como na pasta `Planos Nacionais de IA`: EBIA `#00441B` (verde-escuro), PBIA sem anexos `#2E9E4F` (o verde do PBIA em `Planos Nacionais de IA`) e PBIA com anexos `#A1D99B` (verde-claro). Como os tons são da mesma cor, os gráficos com mais de um documento identificam cada um também por rótulo direto e por marcador, e o tom claro recebe contorno escuro.
3. **Números no padrão brasileiro**, com vírgula decimal e ponto de milhar, sem alterar os valores.
4. Cada gráfico tem título, eixos com a unidade de medida e legenda quando necessária. Barras começam em zero. Não se usa deslocamento aleatório (*jitter*) nem qualquer recurso que altere os valores.
5. Os termos aparecem como estão no texto, em português. O título de cada gráfico informa o documento e, no PBIA, o recorte (sem anexos ou com anexos).
6. Abaixo de cada gráfico, o notebook imprime uma **síntese factual** com os números principais.
7. Cada seção de visualização indica a sua origem: *"Visualização prévia: base inicial para a construção de novos gráficos"* ou *"Visualização construída por comando do pesquisador"*.

---

## 4. Protocolo de operação

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar** que o JSON pedido existe e passa nas verificações de integridade.
3. **Verificar o ambiente:** o modelo `pt_core_news_sm` precisa estar instalado no ambiente do repositório. Se não estiver, o agente informa ao pesquisador e só o instala com a autorização dele. A versão do modelo fica no registro de execução.
4. **Configurar** os parâmetros na célula de configuração do notebook. Nenhum parâmetro fica espalhado pelo código.
5. **Examinar** o texto processado em busca de inflação (seção 3.5) e tratá-la, se houver.
6. **Gerar** cada visualização com a sua tabela correspondente.
7. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
8. **Informar** ao pesquisador, de forma breve e na conversa, o que foi produzido, os tratamentos de inflação aplicados, as palavras de conteúdo retiradas pela lista de *stopwords* e os pontos que exigem a decisão dele.

### 4.2. Estrutura obrigatória do notebook

Um notebook por JSON, gravado nesta pasta com o nome `Análise_<SIGLA>.ipynb`: `Análise_EBIA.ipynb`, `Análise_PBIA_sem_anexos.ipynb` e `Análise_PBIA_com_anexos.ipynb`. O código é o mesmo nos três; muda só a configuração.

1. **Apresentação** (primeira célula, em Markdown): título, projeto, etapa, insumo e o aviso de que as visualizações são prévias e de que nada vai para `resultados/` sem comando do pesquisador. Em seguida: **1. Do que se trata**; **2. Finalidade**; **3. Insumo e recorte do conteúdo** (no PBIA, qual recorte e quais páginas); **4. Método** (visão geral, em tabela); **5. Transparência das escolhas**; **6. Princípios** (vínculo com esta skill, primazia do pesquisador e ausência de comparação).
2. **Configuração:** todos os parâmetros editáveis, comentados, em uma única célula. No mínimo: `SIGLA`, `ARQUIVO_JSON`, `NOME_SAIDA`, `VERSAO_SAIDA`, `SALVAR_SAIDAS = False`, `SOBRESCREVER = False`, `INCLUIR_TITULO_NA_CONTAGEM = False`, `INCLUIR_TITULOS_INTERNOS = True`, `CATEGORIAS_EXCLUIDAS = []`, `UNIDADES_EXCLUIDAS = {}`, `IDIOMA_ESPERADO = "pt"`, `MODELO_SPACY = "pt_core_news_sm"`, `CLASSES_DE_CONTEUDO`, `TAMANHO_MINIMO_LEMA = 2`, `STOPWORDS_ADICIONAIS = []`, `STOPWORDS_MANTIDAS = []`, `LEMAS_MODAIS = ["dever", "poder"]`, `PRONOMES_CLITICOS`, `CORRECOES_DE_LEMA = {}`, `COR_DOCUMENTO`, `TOP_N_LEMAS = 25`, `TOP_N_DISPERSAO = 15`, `TOP_N_BIGRAMAS = 20`, `FREQ_MINIMA_BIGRAMA = 2`, `N_BOOTSTRAP = 2000`, `NIVEL_CONFIANCA = 0.95`, `SEMENTE = 2026`.
3. **Ambiente, estilo e funções:** restrição de pasta (o notebook só roda de dentro de `EBIA_PBIA`), pasta de saída versionada, estilo das figuras e funções do pipeline, comentadas e **idênticas em todos os notebooks da pasta**.
4. **Carregamento e verificação** do JSON, que interrompe a execução se: o arquivo não existir; não tiver sido produzido pela skill 01 para este corpus (`extraction.skill = "skill_extração"` e `extraction.corpus = "EBIA_PBIA"`); o recorte (`extraction.cut`) não corresponder à `SIGLA`; os `id` não forem sequenciais; houver unidade vazia; o número de unidades divergir do registrado; faltar o título; o idioma não for `pt`; ou algum `text` começar por um dos rótulos registrados em `label`. O SHA-256 do JSON é exibido.
5. **Pré-processamento e perfil** do documento: os filtros aplicados e o efeito de cada um; **a tabela dos lemas de classes de conteúdo descartados pela lista de *stopwords*, com as frequências**; o número de unidades com rótulo retirado na extração (informativo).
6. **Análises e visualizações**, cada uma seguida do bloco de texto da seção 4.3. Conjunto-padrão: extensão das unidades textuais; lemas de conteúdo mais frequentes; distribuição dos lemas ao longo do documento; expressões recorrentes (bigramas). Outras análises entram **por comando do pesquisador**, por exemplo: extensão e frequências por eixo ou por parte (`path`); frequências por campo das fichas das ações (`label`, no PBIA com anexos); categorias temáticas com intervalo de confiança; modais; expressões ligadas por preposição (*substantivo + de + substantivo*).
7. **Registro de execução** (parâmetros, versões do ambiente e do modelo, *hash* do insumo, lista de saídas) e **síntese** final.

### 4.3. Bloco de texto após cada visualização

Logo após cada visualização, o notebook contém:

| Item | Conteúdo |
|---|---|
| **Método e escolhas** | O que foi medido, como, com quais parâmetros, e quais escolhas foram feitas (inclusive as do pesquisador e os tratamentos de inflação) |
| **Como ler** | Instrução objetiva de leitura do gráfico |
| **Interpretação** | Texto breve que interpreta o gráfico **com base nos valores efetivamente obtidos** |
| **Fragilidades e ajustes possíveis** | Limitações do método ou dos dados e ajustes que poderiam ser considerados, **quando necessário** (por exemplo, palavras retiradas pela lista de *stopwords*, erros de lematização em português, efeito dos anexos nas contagens) |

**Regras da interpretação:**
- É redigida **somente depois da execução**, a partir dos números exibidos. Antes da execução, o campo fica marcado como pendente. Nunca se escreve interpretação antecipada ou "esperada".
- Cita os valores que a sustentam (frequências, taxas, intervalos).
- Separa **observação** (o que os números mostram) de **inferência** (o que eles podem sugerir), e marca a inferência como tal.
- Não extrapola para além do documento analisado e não faz comparações com outros documentos nem entre os dois recortes do PBIA (isso é tarefa da skill 03).

### 4.4. Pasta `resultados` e ausência de relatórios

- **Nenhum relatório em arquivo é produzido.** As explicações ficam no próprio notebook, e o que o pesquisador precisa saber vai na conversa.
- Visualizações e tabelas **só vão para a pasta `resultados/` quando o pesquisador der o comando**, e da forma que ele exigir.
- **Nenhuma** visualização é adicionada automaticamente a `resultados/`. Sem o comando, o notebook apenas exibe as visualizações e as tabelas, sem gravá-las (`SALVAR_SAIDAS = False`).
- Quando houver gravação, as saídas vão para `resultados/<SIGLA>/<VERSAO_SAIDA>/`. Resultados anteriores nunca são sobrescritos: uma nova execução com mudanças usa uma nova versão (`v2`, `v3`, …).
- Versões interativas (site) de um gráfico só são feitas por comando do pesquisador, com os mesmos dados do notebook, e o link é registrado no próprio notebook.

### 4.5. Mudanças pedidas pelo pesquisador

- Mudanças em gráficos ou tabelas existentes viram **seções novas, acrescentadas** ao notebook (no fim, ou logo abaixo da figura quando o pesquisador pedir assim), com os seus parâmetros na própria célula nova. As células, figuras e códigos existentes ficam intactos.
- Quando o pesquisador pedir ajuste numa seção nova criada por comando dele, ajusta-se essa seção no lugar, e as anteriores continuam intactas.
- O agente não reescreve nem apaga seções anteriores para acomodar uma mudança, salvo comando do pesquisador.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final e são obedecidos em última instância.
2. **Autonomia com transparência:** o agente reconhece e trata o que infla a análise, sempre por parâmetros visíveis e com explicação no texto.
3. **Fidelidade ao insumo:** analisa-se apenas o texto das unidades do JSON da skill 01, sem cortes, abreviações ou acréscimos, e sem os rótulos retirados na extração.
4. **Transparência total:** todo método e toda escolha estão no código **e** na descrição em texto que acompanha a visualização.
5. **Reprodutibilidade:** parâmetros centralizados, semente fixa, versões registradas, *hash* do insumo registrado.
6. **Neutralidade:** nenhum instrumento ou parâmetro é escolhido para produzir um resultado desejado.
7. **Não inventar dados:** nenhum valor é estimado, ajustado ou arredondado para "melhorar" um gráfico. Divergências inesperadas são explicadas, não corrigidas à força.
8. **Exclusividade das fontes:** só se usa o JSON do documento, desta pasta. Os materiais de outras pastas não são consultados.
9. **Fragilidades declaradas:** limitações conhecidas (palavras de conteúdo na lista de *stopwords*, erros de lematização em português, ambiguidade de termos, efeito da estrutura do documento nas contagens) são sempre declaradas.
10. **Escopo individual:** esta skill não compara documentos nem recortes. Toda comparação segue a skill 03.
11. **Sem relatórios:** nenhum relatório em arquivo é produzido.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma visualização sem método explícito, com escolhas ocultas ou com interpretação não sustentada pelos dados compromete a validade dos resultados publicados. O padrão exigido é o máximo, e **a decisão final é sempre do pesquisador**.
