---
name: skill_análise_conjunta
description: Etapa 03 do fluxo de análise da EBIA e do PBIA (IC FAPESP 2026). Orienta a análise CONJUNTA e comparativa da EBIA e do PBIA, em português, em notebook Jupyter, a partir dos JSONs literais produzidos pela skill 01. Identifica as palavras marcadas com asterisco (palavra*) e retira, com a mesma regra em todos os documentos, só o excesso dessas repetições padronizadas, nunca o termo todo, explicando no notebook o que saiu. Compara em termos relativos (ocorrências por 1.000 tokens), trata corretamente os dois recortes do PBIA (sem e com anexos) e não produz relatórios em arquivo.
etapa: 03
versao: 1.1
data: 2026-10-13
---

# Skill de Análise Conjunta — EBIA e PBIA (Etapa 03)

> **Aplicação obrigatória.** Toda análise **conjunta ou comparativa** feita na pasta `notebooks/A_IC FAPESP 2026/EBIA_PBIA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook de análise conjunta, o agente lê esta skill e a cumpre por inteiro. Esta skill **amplia** a skill 02 (`skill_análise_individual.md`): todas as regras da skill 02 valem aqui, com os acréscimos e as mudanças descritos abaixo.

> ⚠️ **O COMANDO DO PESQUISADOR É A DECISÃO FINAL E É OBEDECIDO EM ÚLTIMA INSTÂNCIA.** Ele prevalece sobre qualquer regra desta skill e sobre qualquer escolha do agente: quais documentos e recortes comparar, em que ordem, com quais filtros e limiares, e o que manter. O agente propõe e aponta riscos, mas não decide no lugar do pesquisador. Visualizações e tabelas **só vão para a pasta `resultados/` por comando dele** (seção 4.4), e nenhum relatório é produzido.

> ⚠️ **DIVISÃO DE TAREFAS DEFINIDA PELO PESQUISADOR.** Os JSONs da skill 01 trazem o texto **literal e completo**, com as palavras repetidas de forma padronizada **marcadas com asterisco** (`palavra*`). **Cabe a esta skill, como à skill 02, retirar o excesso dessas repetições** e reproduzir as visualizações sem a inflação que elas causariam, **com a mesma regra em todos os documentos** (skill 02, seção 3.2). Sai **só o excesso marcado, nunca o termo todo**. Exclusões inadequadas prejudicam totalmente a análise: nada além disso é retirado sem comando do pesquisador.

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A análise conjunta da Estratégia Brasileira de Inteligência Artificial (**EBIA**) e do Plano Brasileiro de Inteligência Artificial (**PBIA**) permite identificar **continuidades e mudanças, semelhanças, distinções, enfoques e ênfases** de vocabulário, de prioridades e de concepções de governança entre a estratégia e o plano brasileiros de IA.

Os dois documentos estão **em português**, e a comparação é feita nesse idioma, sem tradução.

Os resultados podem ser incorporados a relatórios científicos. Uma comparação mal construída produz **conclusões falsas**: por exemplo, entre valores absolutos de documentos de tamanhos diferentes, entre dois recortes sobrepostos do mesmo documento como se fossem independentes, ou entre um documento inflado por repetições padronizadas e outro sem elas. Por isso, esta skill exige comparação **relativa**, procedimento **idêntico** para todos os documentos (inclusive na retirada do excesso marcado) e tratamento correto dos dois recortes do PBIA (seção 3.3).

### 1.2. Rigor acadêmico e transparência metodológica

Valem integralmente as regras da skill 02 (seção 1.2):
- cada comando pedido é executado conforme esta skill e o pedido do pesquisador;
- toda escolha metodológica, inclusive a retirada do excesso marcado, está visível no código **e** descrita em texto logo após a visualização que ela afeta;
- o procedimento é reprodutível, com semente fixa e parâmetros registrados;
- se o **comando** do pesquisador for ambíguo, o agente para e pergunta.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/EBIA_PBIA/`.
- **Insumos permitidos:** (a) os JSONs produzidos pela **skill 01** desta pasta (`EBIA_extracao.json`, `PBIA_sem_anexos_extracao.json` e `PBIA_com_anexos_extracao.json`); (b) os comandos do pesquisador.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - usar o PBIA em inglês da pasta `Planos Nacionais de IA` ou qualquer outra extração destes documentos que exista no repositório;
  - investigar outras páginas, pastas ou notebooks do repositório para buscar padrões de resposta, resultados anteriores ou modelos de análise;
  - se espelhar em outras resoluções, análises ou interpretações sobre a EBIA ou o PBIA;
  - usar informações externas para contextualizar ou interpretar as diferenças encontradas;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O notebook conjunto **reprocessa** os JSONs da skill 01 com o mesmo pipeline e a mesma retirada do excesso marcado. Ele **não** usa números copiados dos notebooks individuais. Assim, todos os documentos são tratados no mesmo processamento e com os mesmos parâmetros.
- Os JSONs são **somente leitura**: o notebook nunca acrescenta nem tira asteriscos.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| 01 | Extração literal do texto essencial para JSON, com as repetições padronizadas marcadas por asterisco | `skill_extração.md` |
| 02 | Análise individual de cada JSON, retirando o excesso marcado | `skill_análise_individual.md` |
| **03** | **Análise conjunta e comparativa da EBIA e do PBIA, retirando o excesso marcado com a mesma regra em todos os documentos, com normalização relativa** | **esta skill** |

### 1.5. Autoridade do pesquisador e autonomia do agente

Ordem de precedência, da mais forte para a mais fraca:

1. **o comando atual do pesquisador;**
2. **as decisões que o pesquisador já tomou para estas análises** (documentos e recortes escolhidos, parâmetros fixados, termos mantidos ou retirados);
3. as regras desta skill e da skill 02;
4. o julgamento do agente, apenas no que os itens anteriores não definem.

- As ordens e os comandos do pesquisador são a **decisão final**: quais documentos e recortes comparar, em que ordem, com quais filtros e limiares. O agente pode propor instrumentos e apontar riscos, mas não impõe escolhas. Quando uma ordem tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.
- Mudanças pedidas em gráficos existentes são **acrescentadas, e não substituídas** (skill 02, seção 4.5).
- **A autonomia do agente não inclui excluir termos.** O que sai da análise é **apenas** o excesso marcado com asterisco e o que o pesquisador mandar retirar (skill 02, seção 3.6). Se o agente identificar outra possível inflação ou uma assimetria entre os documentos, ele a **mostra e informa** ao pesquisador, sem retirá-la (seção 3.7).

---

## 2. Objetivos

### 2.1. Objetivo principal

Comparar, em notebook Jupyter (`.ipynb`), o conteúdo extraído da EBIA e do PBIA e produzir **visualizações gráficas e interpretações comparativas sem a inflação das repetições padronizadas marcadas na extração**. A comparação é feita sempre em **termos relativos (ocorrências por 1.000 tokens)**, e não absolutos, para permitir verificar continuidades e mudanças, semelhanças, distinções, diferentes enfoques, diferentes ênfases, termos mais comuns e termos mais distintivos de cada documento.

### 2.2. Objetivos específicos

1. **Verificar os insumos:** confirmar que os JSONs vêm da skill 01 desta pasta, estão íntegros, têm marcações coerentes com os seus catálogos de padrões e que os dois recortes do PBIA estão aninhados como esperado.
2. **Retirar o excesso marcado** com a mesma regra em todos os documentos e **explicar** no notebook quais termos saíram de cada documento, quantas vezes e em que circunstâncias.
3. **Expor a disparidade de tamanho** entre os documentos, que justifica a normalização relativa.
4. **Comparar os termos mais frequentes** de cada documento, em ocorrências por 1.000 tokens.
5. **Identificar semelhanças:** termos com peso relativo parecido nos dois documentos.
6. **Identificar distinções:** termos significativamente mais característicos de um documento do que do outro (análise de *keyness*).
7. **Comparar o vocabulário** compartilhado e exclusivo, com as ressalvas de tamanho.
8. **Comparar os enfoques temáticos**, quando o pesquisador definir as categorias, com intervalos de confiança para cada documento e para a diferença entre eles.
9. **Comparar a ênfase normativa** (verbos modais), quando pedido.
10. **Medir o efeito dos anexos** no PBIA, quando pedido (seção 3.3).
11. **Interpretar** cada visualização com base nos valores obtidos, apontando método, escolhas e fragilidades.
12. **Registrar** parâmetros, versões e saídas para garantir a reprodutibilidade.

---

## 3. Diretrizes para a análise

### 3.1. Insumo: o que entra e o que não entra

Igual à skill 02 (seção 3.1). De cada JSON são usados o título e o subtítulo (só para identificação: **não entram na contagem por padrão**), o texto integral e literal de cada unidade (`sections[].text`), as marcações com asterisco e o catálogo de padrões (`marked_patterns` e `extraction.repetition_patterns`), e, apenas como filtros, índice de posição ou agrupadores, os campos `type`, `category`, `id` e `path`. **Os mesmos filtros valem para todos os documentos.**

### 3.2. Identidade de procedimento

- **Mesmo pipeline e mesmos parâmetros** para todos os documentos comparados. O pré-processamento é o da skill 02 (seção 3.4), inclusive a lista de *stopwords*, as palavras mantidas por decisão do pesquisador, os modais e as correções de lema.
- **Mesma retirada do excesso marcado** em todos os documentos, pela regra da skill 02 (seção 3.2): em cada documento, de cada padrão do seu catálogo, a primeira ocorrência fica e as demais saem, da contagem dos termos e do total de tokens. Ocorrências sem asterisco nunca saem por esta regra.
- **Mesmo idioma:** todos os JSONs devem estar em português (`document.language = "pt"`). O carregamento confere isso e interrompe a execução se algum divergir.
- **Simetria.** Nenhum documento é tratado como referência privilegiada, nem a EBIA nem o PBIA. A convenção de sentido das medidas (por exemplo, valores positivos = mais característico do primeiro documento do par) é declarada e mantida em todas as figuras.
- **Ordem e cores fixas.** Os documentos aparecem sempre na ordem definida em `DOCUMENTOS` (EBIA, PBIA sem anexos, PBIA com anexos) e com as cores de `COR_DOCUMENTO`, as mesmas dos notebooks individuais.

### 3.3. Os dois recortes do PBIA

O JSON do PBIA com anexos **contém integralmente** o JSON sem anexos: as unidades das p. 11–48 são as mesmas nos dois, com as mesmas marcações. Os dois recortes, portanto, **não são documentos independentes**, e isso tem quatro consequências:

1. **Os dois recortes do PBIA nunca entram juntos** como documentos distintos no mesmo teste de *keyness*, no mesmo gráfico de dispersão ou na mesma comparação de vocabulário. Compará-los diretamente mediria a sobreposição, e não uma diferença.
2. **A comparação EBIA × PBIA é feita com um recorte do PBIA por vez**, definido em `COMPARACOES`. Qual recorte usar é **decisão do pesquisador**. Se o comando não disser, o notebook faz as duas comparações, em seções separadas e com os mesmos parâmetros (EBIA × PBIA sem anexos; EBIA × PBIA com anexos), para que o pesquisador veja o efeito dos anexos sem que o agente escolha por ele. O recorte nunca é escolhido depois de ver os resultados.
3. **A retirada do excesso marcado é feita em cada recorte como documento inteiro.** Os padrões da ficha das ações só existem nos anexos, e por isso só atuam no recorte com anexos; os padrões que ocorram no corpo atuam igualmente nos dois recortes.
4. **O efeito dos anexos**, quando o pesquisador pedir, é medido entre partes **disjuntas** do PBIA com anexos: o corpo (unidades sem `category = "Annex"`) contra os anexos (unidades com `category = "Annex"`). A retirada do excesso marcado é feita antes, no recorte com anexos inteiro, e só depois o texto é dividido. Nunca se compara o recorte sem anexos com o recorte com anexos.

O carregamento confere que as unidades do JSON sem anexos são idênticas, com as mesmas marcações, às primeiras unidades do JSON com anexos. Se não forem, a execução é interrompida e o agente informa ao pesquisador que os recortes precisam ser refeitos pela skill 01.

### 3.4. Comparação relativa: ocorrências por 1.000 tokens

A EBIA e o PBIA (em qualquer recorte) têm **tamanhos diferentes**. Comparar frequências absolutas favoreceria o documento mais longo e produziria distorções. Por isso, **toda comparação entre documentos é feita em ocorrências por 1.000 tokens**:

> **taxa por 1.000 tokens = (ocorrências do termo no documento ÷ total de tokens do documento) × 1.000**

- **Token** é definido como na skill 02: palavra do texto (sequência de letras, inclusive acentuadas, com hífen interno; siglas incluídas), sem números, pontuação, símbolos e endereços eletrônicos.
- **O denominador é o total de tokens do documento, incluindo *stopwords* e sem as palavras do excesso marcado.** É a mesma base para todos os termos e para todas as categorias.
- Com essa normalização, os termos ficam em **pé de igualdade**: uma taxa de 5 por 1.000 tem o mesmo significado em um documento de 5.000 tokens e em um de 50.000.
- Valores **absolutos** aparecem apenas na tabela de perfil, para **expor a disparidade de tamanho**, e como informação auxiliar nas tabelas. Eles **nunca** são usados para afirmar que um documento enfatiza algo mais do que outro.

### 3.5. Pares de comparação

- As comparações são feitas **por par**, conforme `COMPARACOES` (seção 3.3). As medidas descritivas (taxas por 1.000 tokens, termos mais comuns, vocabulário) são apresentadas para os dois documentos do par lado a lado.
- Os gráficos de dois eixos (dispersão de semelhanças, convergência e divergência) comparam os dois documentos do par.
- A *keyness* compara diretamente os dois documentos do par. O modo "um contra os demais" da pasta `Planos Nacionais de IA` **não se aplica aqui**, porque somaria na referência recortes sobrepostos do PBIA.
- A correção para comparações múltiplas (Bonferroni) considera o total de testes de **todos** os pares feitos no notebook.

### 3.6. Critérios para afirmar uma diferença

| Comparação | Critério |
|---|---|
| Termo a termo (*keyness*) | Frequência combinada mínima `FREQ_MINIMA_COMPARACAO = 5`; **G²** de log-verossimilhança (Dunning, 1993; Rayson & Garside, 2000) ≥ `LIMIAR_G2 = 6,63` (p < 0,01; 1 grau de liberdade) **e** \|*Log Ratio*\| (Hardie, 2014) ≥ `LIMIAR_LOG_RATIO = 1` (ao menos o dobro da frequência relativa). Os dois critérios são exigidos juntos |
| Comparações múltiplas | Informa-se quantos termos distintivos resistem à correção de Bonferroni (`ALFA_BONFERRONI = 0,01`) |
| Frequência zero | Correção de 0,5 apenas no cálculo do *Log Ratio*; o termo é marcado como *exclusivo* |
| Categorias temáticas | Diferença afirmada apenas quando o intervalo de confiança da diferença (bootstrap por unidades, semente fixa) **não inclui zero** |
| Zonas descritivas | Zonas de convergência e divergência por razão entre taxas (`RAZAO_ZONA_NEUTRA = 2`) são **descritivas** e não são teste de significância. A tabela informa quais termos passam nos critérios de *keyness* |

Os limiares são parâmetros editáveis e são fixados **antes** da interpretação. Todos os critérios são calculados **depois** da retirada do excesso marcado.

### 3.7. O que infla ou desequilibra a comparação

Vale a seção 3.6 da skill 02 (**sai só o excesso marcado e o que o pesquisador mandar; frequência real é resultado**), com um cuidado a mais: na comparação, o problema não é só a inflação de um documento, mas a **assimetria** entre os documentos.

- **Marcação equivalente.** O agente verifica se padrões do mesmo tipo foram marcados nos dois documentos. Se um documento tiver um padrão de repetição marcado e o outro tiver padrão do mesmo tipo sem marcação, a comparação ficaria inflada de um lado só: o agente mostra a assimetria, com o efeito numérico, e informa ao pesquisador que a marcação é corrigida pela skill 01. Ele **não** retira as ocorrências não marcadas por conta própria.
- **Diferenças de estrutura.** A EBIA é uma estratégia; o PBIA é um plano com ações, metas, impactos e recursos, que nos anexos se repetem em formato de ficha. Um documento pode ter apresentação, sumário executivo ou quadros e o outro não. Quando a estrutura distorcer a comparação, o agente mostra o efeito e propõe filtros simétricos (seção 3.1), que só são aplicados por decisão do pesquisador quando mudarem o objeto da comparação.
- **Conteúdo da ficha.** As expressões fixas da ficha das ações saem pela retirada do excesso marcado, mas o conteúdo da ficha fica, porque é texto do documento: valores repetidos (*iniciativa única*) e termos dos desafios e dos impactos esperados (*aumento*, *redução*) podem parecer distintivos do PBIA com anexos em parte por causa do formato. O notebook mostra quanto de cada termo distintivo vem dos anexos, e o agente aponta o efeito ao pesquisador, que decide.
- **Diferenças de grafia não são diferenças de conteúdo.** Se um documento escreve *inteligência artificial* por extenso onde o outro usa *IA*, os termos *inteligência*, *artificial* e *ia* podem aparecer como distintivos só por isso. O agente mede o efeito e o aponta; unificar é decisão do pesquisador (skill 02, seção 3.4).
- **Exclusões simétricas.** Um termo retirado por decisão do pesquisador sai de todos os documentos. O agente aponta as formas relacionadas (por exemplo, *brasil* e *brasileiro*) para que o pesquisador decida se também saem.
- Toda decisão desse tipo fica na configuração, é explicada no texto e pode ser revertida pelo pesquisador.

### 3.8. Regras para as visualizações

Valem todas as regras da skill 02 (seção 3.8), com os acréscimos:
1. **Toda visualização comparativa usa taxas por 1.000 tokens** (ou medidas derivadas delas), calculadas sem o excesso marcado, nunca contagens absolutas.
2. Os documentos aparecem sempre na **mesma ordem** e com as **mesmas cores**, e cada um é identificado também por rótulo direto ou marcador, porque os três tons são da mesma cor.
3. O sentido de toda medida assimétrica (*Log Ratio*, eixos X e Y) é escrito no próprio gráfico.
4. O **recorte do PBIA** usado (sem anexos ou com anexos) é escrito no título ou na legenda de cada figura.

### 3.9. Vieses proibidos

Valem todos os da skill 02 (seção 3.7), e mais:
- comparar valores absolutos de documentos de tamanhos diferentes como se fossem comparáveis;
- retirar o excesso marcado de um documento e não do outro, ou retirar ocorrências não marcadas de um deles;
- afirmar que um documento "enfatiza mais" um tema com base em diferenças que não passaram pelos critérios da seção 3.6;
- tratar os dois recortes do PBIA como documentos independentes;
- escolher o recorte do PBIA, o sentido da comparação ou os limiares depois de ver os resultados, ou para favorecer uma leitura;
- tratar a EBIA ou o PBIA com procedimento diferente do outro;
- atribuir as diferenças a posições políticas dos governos sem considerar o gênero, a extensão, a função e a data de cada documento.

---

## 4. Protocolo de operação

### 4.1. Procedimento passo a passo

1. **Ler esta skill e a skill 02** por inteiro antes de começar.
2. **Verificar** que os JSONs pedidos existem e que o modelo `pt_core_news_sm` está instalado (skill 02, seção 4.1).
3. **Configurar** os parâmetros na célula de configuração (documentos, pares de comparação, pré-processamento, limiares comparativos).
4. **Processar** todos os documentos com o mesmo pipeline e **retirar o excesso marcado** de cada um com a mesma regra.
5. **Verificar** a equivalência de tratamento entre os documentos, inclusive das marcações (seção 3.7), e o aninhamento dos recortes do PBIA (seção 3.3).
6. **Expor o perfil comparativo** e a disparidade de tamanho, antes e depois da retirada do excesso marcado.
7. **Gerar** cada visualização comparativa com a sua tabela correspondente.
8. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
9. **Registrar** a execução (parâmetros, versões, *hash* de todos os insumos, lista de saídas).
10. **Informar** ao pesquisador, de forma breve e na conversa, o que foi produzido, o excesso retirado de cada documento, as assimetrias encontradas e os pontos que exigem a decisão dele.

### 4.2. Estrutura obrigatória do notebook

Nome do arquivo: `Análise_Conjunta_EBIA_PBIA.ipynb`, gravado nesta pasta. Outro conjunto de comparações, pedido pelo pesquisador, recebe um sufixo descritivo, sem sobrescrever o notebook existente.

1. **Apresentação** (primeira célula, em Markdown): título, projeto, etapa, insumos e o aviso de que as visualizações são prévias e de que nada vai para `resultados/` sem comando do pesquisador. Em seguida: **1. Do que se trata**; **2. Finalidade**; **3. Insumos e recorte do conteúdo** (os recortes do PBIA e as páginas de cada um); **4. Repetições marcadas e retirada do excesso** (o que o asterisco indica e a regra comum aos documentos); **5. Por que a comparação é relativa**; **6. Os dois recortes do PBIA** (por que não são comparados entre si); **7. Método** (visão geral, em tabela); **8. Transparência das escolhas**; **9. Princípios** (vínculo com esta skill, primazia do pesquisador e simetria entre os documentos).
2. **Configuração:** todos os parâmetros editáveis em uma única célula: `DOCUMENTOS` (sigla → JSON, na ordem das figuras: `EBIA`, `PBIA_sem_anexos`, `PBIA_com_anexos`); `COMPARACOES` (por padrão, `[("EBIA", "PBIA_sem_anexos"), ("EBIA", "PBIA_com_anexos")]`); `MARCADOR_REPETICAO = "*"` e `RETIRAR_EXCESSO_MARCADO = True`; os mesmos parâmetros de pré-processamento e de recorte dos notebooks individuais; e os parâmetros comparativos (`TOP_N_COMPARACAO`, `FREQ_MINIMA_COMPARACAO`, `LIMIAR_G2`, `LIMIAR_LOG_RATIO`, `TOP_N_KEYNESS`, `ALFA_BONFERRONI`, `RAZAO_ZONA_NEUTRA`, `N_ROTULOS_DISPERSAO`, `N_BOOTSTRAP`, `NIVEL_CONFIANCA`, `SEMENTE`), com `SALVAR_SAIDAS = False`.
3. **Ambiente, estilo e funções:** restrição de pasta, estilo, funções do pipeline e da retirada do excesso marcado (**idênticas** às da skill 02) e funções comparativas.
4. **Carregamento e verificação** de todos os JSONs, com as verificações da skill 02 (inclusive as das marcações), a conferência do idioma e a conferência do aninhamento dos recortes do PBIA (seção 3.3).
5. **Pré-processamento** e **perfil comparativo**, com a disparidade de tamanho antes e depois da retirada do excesso marcado, os filtros aplicados a cada documento e os lemas de conteúdo descartados pela lista de *stopwords* em cada um.
6. **Repetições marcadas e retiradas** (seção obrigatória, antes das visualizações): para cada documento, o catálogo dos padrões, a tabela por termo e o texto explicativo da skill 02 (seção 3.2, item 5); em seguida, uma tabela comparativa dos termos afetados, com a taxa por 1.000 tokens antes e depois da retirada em cada documento, e a indicação das assimetrias de marcação encontradas (seção 3.7).
7. **Análises e visualizações comparativas**, sem o excesso marcado, para cada par de `COMPARACOES`, cada uma seguida do bloco de texto da seção 4.3. Conjunto-padrão: termos mais comuns, lado a lado; semelhanças (termos compartilhados); distinções (*keyness*); vocabulário compartilhado e exclusivo. Outras análises entram **por comando do pesquisador**, por exemplo: convergência e divergência de unigramas e bigramas; efeito dos anexos no PBIA (seção 3.3); enfoques temáticos; modais; comparação por eixo ou por parte.
8. **Registro de execução** e **síntese** final.

### 4.3. Bloco de texto após cada visualização

Igual à skill 02 (seção 4.3): **Método e escolhas** (com o efeito da retirada do excesso marcado em cada documento), **Como ler**, **Interpretação** (redigida só depois da execução, a partir dos valores obtidos, separando observação de inferência) e **Fragilidades e ajustes possíveis** (quando necessário). Na interpretação comparativa, toda afirmação de diferença indica o critério da seção 3.6 que a sustenta e o recorte do PBIA a que se refere.

### 4.4. Pasta `resultados` e ausência de relatórios

- **Nenhum relatório em arquivo é produzido.** As explicações ficam no próprio notebook, e o que o pesquisador precisa saber vai na conversa.
- Visualizações e tabelas **só vão para a pasta `resultados/` quando o pesquisador der o comando**, e da forma que ele exigir.
- **Nenhuma** visualização é adicionada automaticamente a `resultados/`. Sem o comando, o notebook apenas exibe as visualizações e as tabelas, sem gravá-las (`SALVAR_SAIDAS = False`).
- Quando houver gravação, as saídas vão para `resultados/Conjunta_EBIA_PBIA/<VERSAO_SAIDA>/`. Resultados anteriores nunca são sobrescritos.
- Versões interativas (site) só são feitas por comando do pesquisador, com os mesmos dados do notebook, e o link é registrado no próprio notebook.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final e são obedecidos em última instância.
2. **Retirada só do excesso marcado, igual em todos os documentos:** sai apenas a repetição em excesso das palavras marcadas com asterisco; a primeira ocorrência de cada padrão e todas as ocorrências sem asterisco ficam. Nunca se retira o termo todo.
3. **Nenhuma exclusão arbitrária:** além do excesso marcado, só sai o que o pesquisador mandar, e sempre de todos os documentos. Inflações não marcadas e assimetrias são mostradas e informadas, não retiradas.
4. **Explicação do que saiu:** o notebook diz quais termos foram retirados de cada documento, quantas vezes e em que circunstâncias, com os números de antes e de depois.
5. **Comparação relativa obrigatória:** nenhuma conclusão comparativa se apoia em valores absolutos.
6. **Identidade de procedimento:** mesmo pipeline, mesmos parâmetros e mesmos filtros para todos os documentos.
7. **Recortes sobrepostos não são comparados entre si:** a EBIA é comparada com um recorte do PBIA por vez, e o efeito dos anexos é medido entre partes disjuntas.
8. **Significância com tamanho de efeito:** diferenças termo a termo só são afirmadas quando passam pelos dois critérios. Diferenças entre categorias só são afirmadas quando o intervalo de confiança da diferença não inclui zero.
9. **Fidelidade ao insumo:** analisa-se apenas o texto das unidades dos JSONs da skill 01.
10. **Transparência total:** todo método e toda escolha estão no código **e** na descrição em texto.
11. **Reprodutibilidade:** parâmetros centralizados, semente fixa, versões e *hashes* registrados.
12. **Neutralidade e simetria:** nenhum documento é privilegiado e nenhum parâmetro é escolhido para produzir um resultado desejado.
13. **Exclusividade das fontes:** só se usam os JSONs desta pasta. Os materiais de outras pastas não são consultados.
14. **Fragilidades declaradas:** instabilidade de frequências baixas, diferenças de gênero, extensão, função e data dos documentos, inflação não marcada, palavras de conteúdo na lista de *stopwords* e erros de lematização em português são sempre declarados.
15. **Sem relatórios:** nenhum relatório em arquivo é produzido.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma comparação que ignore a diferença de tamanho entre os documentos, que trate recortes sobrepostos como independentes, que compare um documento inflado com outro limpo, que retire termos indevidamente ou que esconda escolhas metodológicas compromete a validade dos resultados publicados. O padrão exigido é o máximo, e **a decisão final é sempre do pesquisador**.
