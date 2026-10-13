---
name: skill_extração
description: Etapa 01 do fluxo de análise da EBIA e do PBIA (IC FAPESP 2026). A partir do PDF anexado pelo pesquisador, extrai em português, de forma literal e sem excluir nada do corpo essencial do texto, o conteúdo dos intervalos de páginas definidos por ele (sem notas de rodapé e sem o conteúdo de gráficos e tabelas). As palavras repetidas de forma padronizada e excessiva NÃO são retiradas: são apenas marcadas com asterisco (palavra*), para que as skills 02 e 03 retirem o excesso. Entrega apenas JSON (PBIA sem anexos, PBIA com anexos e EBIA) e não produz relatório.
etapa: 01
versao: 1.1
data: 2026-10-13
---

# Skill de Extração — EBIA e PBIA (Etapa 01)

> **Aplicação obrigatória.** Toda extração feita na pasta `notebooks/A_IC FAPESP 2026/EBIA_PBIA/` **deve** passar por esta skill. Nenhuma extração pode ser feita fora deste protocolo, de forma parcial ou por atalho. Sempre que for pedido um comando de extração nesta pasta, o agente lê esta skill antes de começar e a cumpre por inteiro.

> ⚠️ **O COMANDO DO PESQUISADOR É A DECISÃO FINAL E É OBEDECIDO EM ÚLTIMA INSTÂNCIA.** Ele prevalece sobre qualquer regra desta skill e sobre qualquer julgamento do agente. Os comandos que o pesquisador já deu para a EBIA e o PBIA estão na seção 2 e são obrigatórios; um comando novo dele prevalece inclusive sobre esses. O agente não reinterpreta, não "melhora" e não deixa de cumprir um comando por achar outra solução mais adequada.

> ⚠️ **DIVISÃO DE TAREFAS DEFINIDA PELO PESQUISADOR.** A extração é **literal e não exclui nada** do corpo essencial do texto. As palavras que se repetem de forma padronizada e excessiva **não são retiradas aqui**: são apenas **marcadas com asterisco** (`palavra*`). **Quem retira o excesso são as skills 02 (análise individual) e 03 (análise conjunta).**

---

## 1. Contexto

### 1.1. A pesquisa e o pedido do pesquisador

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **EBIA_PBIA** reúne os dois documentos centrais da política brasileira de inteligência artificial: a **Estratégia Brasileira de Inteligência Artificial (EBIA)** e o **Plano Brasileiro de Inteligência Artificial (PBIA)**.

**O pedido:** o pesquisador anexa à conversa o **PDF** de um dos documentos e quer, como resultado, **um JSON com a extração literal de todo o texto desse PDF** que pertence ao corpo essencial do documento, no intervalo de páginas que ele definiu (seção 2). Nesse texto, as palavras que aparecem de forma padronizada e repetida, por seguirem um padrão textual, recebem um **asterisco** (seção 3.2), para que a análise possa retirar o excesso sem perder o restante do texto.

**Os dois documentos estão em português** e são extraídos e analisados nesse idioma. O agente não traduz nada.

Os dados produzidos aqui sustentam análises e visualizações que entram em relatórios científicos. Por isso, **qualquer erro de extração ou de marcação passa para todas as etapas seguintes** e compromete a validade dos resultados. Uma marcação indevida faz a análise retirar ocorrências reais de um termo, o que **prejudica totalmente as visualizações**.

### 1.2. Rigor acadêmico e metodológico

O agente deve agir com o rigor de um procedimento científico documentado:

- Cada comando pedido é executado conforme esta skill e o pedido do pesquisador, sem atalhos.
- Cada decisão relevante (incluir uma parte, marcar um padrão de repetição, deixar de marcar outro) é **explícita**, vale da mesma forma para todo o documento e é **informada ao pesquisador** na mensagem final (seção 4.5).
- O procedimento é **reprodutível**: outra pessoa que aplique esta skill ao mesmo PDF, com os mesmos comandos, deve chegar a um resultado equivalente, inclusive nas marcações.
- Se o **comando** do pesquisador for ambíguo, contraditório ou não estiver coberto por esta skill, o agente **para e pergunta**. Já as dúvidas sobre o **documento** (o que é corpo essencial, o que é padrão de repetição) são resolvidas pelo próprio agente, com os critérios da seção 3.2.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/EBIA_PBIA/`.
- **Arquivo-fonte:** o PDF anexado pelo pesquisador à conversa ou gravado por ele nesta pasta. Quando o PDF vier só como anexo, o agente avisa na mensagem final que, para a extração ser reproduzível, o arquivo deve ser gravado na pasta. O próprio agente só o grava por comando do pesquisador.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - usar outras versões ou extrações destes documentos que existam no repositório, como o PBIA em inglês da pasta `Planos Nacionais de IA` ou os JSONs do PBIA de outras pastas. A extração parte **só** do PDF anexado;
  - usar conhecimento prévio do modelo sobre a EBIA ou o PBIA, a internet ou outras edições dos documentos para completar, corrigir, datar ou interpretar o texto;
  - usar análises, resultados, códigos ou arquivos de **outras pastas** do repositório. As skills de `Planos Nacionais de IA` serviram de modelo para estas, mas os arquivos de lá não são insumo desta etapa;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O **arquivo-fonte** é **somente leitura**: nunca pode ser alterado, renomeado ou apagado.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| **01** | **Extração literal do texto essencial para JSON, com as repetições padronizadas marcadas por asterisco** | **esta skill** |
| 02 | Análise individual de cada JSON, em notebook, **retirando o excesso marcado** | `skill_análise_individual.md` |
| 03 | Análise conjunta da EBIA e do PBIA, em notebook, **retirando o excesso marcado** | `skill_análise_conjunta.md` |

A Etapa 01 **não faz análise**: não interpreta, não classifica por tema, não conta frequências para gráficos, não resume e não gera gráficos. **Também não retira repetições**: só as identifica e as marca. **O único produto desta etapa é o JSON.** Não há relatório de extração.

### 1.5. Autoridade do pesquisador e autonomia do agente

Ordem de precedência, da mais forte para a mais fraca:

1. **o comando atual do pesquisador;**
2. **os comandos do pesquisador registrados na seção 2;**
3. as demais regras desta skill;
4. o julgamento do agente, apenas no que os itens anteriores não definem.

- O pesquisador tem a **decisão final** sobre o que compõe o texto de cada documento e sobre o que é marcado. Se ele mandar incluir, marcar ou desmarcar algo, o agente cumpre, mesmo que contrarie os critérios desta skill. Se enxergar um risco no comando, o agente cumpre e menciona o risco em uma linha na mensagem final; nunca troca a decisão do pesquisador pela sua.
- Dentro do que o pesquisador não definiu, o agente tem **autonomia de julgamento** para compreender o documento, reconhecer o corpo essencial e identificar os padrões de repetição. As orientações da seção 3 não são uma lista fechada; o agente reconhece também os casos que elas não preveem.
- Autonomia não é arbítrio: toda marcação segue **todos** os critérios da seção 3.2.1, vale igualmente para todo o documento e é informada ao pesquisador. **Na dúvida, o agente não marca** e leva o caso ao pesquisador, porque uma marcação indevida retira da análise ocorrências reais.

---

## 2. Comandos do pesquisador para este corpus

Estes comandos foram dados pelo pesquisador e são **obrigatórios**. Prevalecem sobre as demais seções desta skill e só podem ser mudados por um novo comando dele.

### 2.1. Comandos comuns aos dois documentos

| Comando do pesquisador | Aplicação |
|---|---|
| O pesquisador anexa um PDF e quer como resultado um JSON com a extração do texto desse PDF | Seções 3 e 4 |
| Os textos estão em português | Extração em português, sem tradução; `document.language = "pt"` |
| **A extração é literal e não exclui nada** do corpo essencial do texto, no intervalo de páginas definido | Seções 3.1 e 3.3 |
| **Tudo o que estiver dentro do corpo essencial do texto entra na análise** | Seção 3.3 |
| Não incluir notas de rodapé nem elementos que não estejam no corpo essencial do texto | Seção 3.4 |
| Não incluir nos textos o conteúdo de gráficos e de tabelas | Seção 3.4 |
| **As palavras repetidas de forma excessiva, como parte de um padrão textual repetitivo, são apenas destacadas com asterisco** (`palavra*`). O asterisco é colocado **apenas quando o termo aparece de forma padronizada e repetida**. Repetições de baixa escala, poucas vezes, não são marcadas | Seção 3.2 |
| **A retirada do excesso não é feita na extração**: é feita pelas skills 02 e 03, que retiram só as repetições em excesso, e nunca o termo todo | Seção 1.4 |
| Não produzir relatórios | Seção 4.2 |

**Como se lê "literal, sem excluir nada".** Dentro do corpo essencial do texto e do intervalo de páginas definido, **nenhuma palavra é retirada, trocada ou resumida**, nem mesmo as repetidas, e o único acréscimo permitido é o asterisco de marcação. Continuam valendo os demais comandos que o pesquisador já deu: os intervalos de páginas e a exclusão das notas de rodapé, do conteúdo de gráficos e tabelas e dos elementos que não pertencem ao corpo do texto (cabeçalhos e rodapés de página, numeração de página). Se o pesquisador mandar incluir também algum desses elementos, vale o comando dele.

As páginas indicadas pelo pesquisador são sempre **páginas do arquivo PDF** (1 = primeira página do arquivo), e não a numeração impressa no documento.

### 2.2. PBIA: dois JSONs

| Parte do PDF | Páginas do PDF | Tratamento |
|---|---|---|
| Elementos pré-textuais: capa, organização, autores, edição, coordenação, ministérios que participaram e sumário | 1 a 10 | **Fora do recorte** |
| Texto, da Apresentação até o fim das Considerações finais | 11 a 48 | Entra nos dois JSONs |
| Anexo 1. Ações de impacto imediato e Anexo 2. Ações estruturantes | 49 a 93 | Entra **só** no JSON com anexos |
| Página em branco (94) e elementos pós-textuais: glossário de termos utilizados pelo PBIA, siglas e abreviaturas, referências | a partir da 94 | **Fora do recorte** |

| JSON | Páginas do PDF | Termina em |
|---|---|---|
| `PBIA_sem_anexos_extracao.json` | 11 a 48 | Fim das Considerações finais (p. 48) |
| `PBIA_com_anexos_extracao.json` | 11 a 93 | Fim do Anexo 2 (p. 93), com os Anexos 1 e 2 |

Ao receber o PDF do PBIA, o agente produz os dois JSONs, salvo comando diferente do pesquisador.

**Conferência das bordas.** Antes de extrair, o agente confere no PDF que: a p. 11 começa na Apresentação; a p. 48 encerra as Considerações finais; o Anexo 1 começa na p. 49; a p. 93 encerra o Anexo 2; e os elementos pós-textuais começam depois dela. Se algum desses pontos não se confirmar (por exemplo, outra edição do PDF), o agente **para e pergunta**.

*Decisão do pesquisador (2026-10-13).* O comando inicial fixava o fim da versão com anexos na p. 92. Na conferência do PDF, o Anexo 2 terminava na p. 93 (a Ação 54 começa na p. 92 e termina na p. 93), a p. 94 estava em branco e o glossário começava na p. 95. Consultado, o pesquisador decidiu que o JSON com anexos vai até a p. 93.

**Padrão repetitivo indicado pelo pesquisador (Anexos 1 e 2).** Cada ação dos anexos segue a mesma ficha, como neste trecho do PDF:

```text
● Ação 50: Guias Brasileiros de IA Responsável
Série de guias sobre IA no Brasil para promover o uso responsável e adaptado à realidade nacional.
   » Desafio: necessidade de promoção da confiança pública na IA e adaptação dos padrões globais à realidade brasileira.
   » Metas: elaboração e publicação do Guia para IA Ética e Responsável em três meses; lançamento do Guia de IA para o Setor Público em 6 meses; e realização de workshops e eventos periódicos para divulgação dos guias.
   » Impactos esperados: aumento do entendimento e da confiança da população, de servidores públicos e profissionais sobre o uso e as aplicações da IA; e promoção de práticas responsáveis na adoção e no desenvolvimento de IA, alinhadas com padrões globais e adaptadas ao contexto nacional.
   » Recursos (2024-2028): R$ 500 mil - Ministério da Justiça e Segurança Pública (MJSP) -.
   » Componentes da ação: iniciativa única.
```

As expressões fixas **"Ação NN"**, **"Desafio"**, **"Metas"**, **"Impactos esperados"**, **"Recursos (2024-2028)"** e **"Componentes da ação"** repetem-se em todas as ações e inflariam as palavras *ação*, *desafio*, *meta*, *impacto*, *esperado*, *recurso* e *componente*. Por comando do pesquisador, elas **ficam no texto** e as suas palavras recebem o asterisco. Tudo o mais fica exatamente como está, sem marcação:

| No PDF | No `text` do JSON |
|---|---|
| ● Ação 50: Guias Brasileiros de IA Responsável | `Ação* 50: Guias Brasileiros de IA Responsável` |
| Série de guias sobre IA no Brasil para promover o uso responsável e adaptado à realidade nacional. | `Série de guias sobre IA no Brasil para promover o uso responsável e adaptado à realidade nacional.` (sem marcação) |
| » Desafio: necessidade de promoção da confiança pública na IA e adaptação dos padrões globais à realidade brasileira. | `Desafio*: necessidade de promoção da confiança pública na IA e adaptação dos padrões globais à realidade brasileira.` |
| » Metas: elaboração e publicação do Guia para IA Ética e Responsável em três meses; (…) | `Metas*: elaboração e publicação do Guia para IA Ética e Responsável em três meses; (…)` |
| » Impactos esperados: aumento do entendimento e da confiança da população, (…) | `Impactos* esperados*: aumento do entendimento e da confiança da população, (…)` |
| » Recursos (2024-2028): R$ 500 mil - Ministério da Justiça e Segurança Pública (MJSP) -. | `Recursos* (2024-2028): R$ 500 mil - Ministério da Justiça e Segurança Pública (MJSP) -.` |
| » Componentes da ação: iniciativa única. | `Componentes* da* ação*: iniciativa única.` |

*(Nesta tabela, "(…)" só abrevia o exemplo; no JSON, o `text` é sempre integral. O " -." final do item de recursos também fica, porque está no original. O marcador "»" vai para o campo `number`.)*

- **Só as palavras da expressão fixa recebem asterisco.** O número da ação (*50*), o título da ação e o conteúdo que vem depois de cada expressão **não** são marcados.
- **Todas as palavras da expressão fixa são marcadas**, inclusive as gramaticais (*da* em *Componentes* da* ação**), para que a análise retire a ocorrência repetida inteira, também do total de palavras.
- **As mesmas palavras usadas no texto corrido não são marcadas** (por exemplo, *"as metas do plano"*, *"cada ação"*, *"recursos do FNDCT"*): são uso real e ficam na análise.
- A extração marca **todas** as ocorrências do padrão, inclusive a primeira. Quanto disso sai da análise é decidido pelas skills 02 e 03, que mantêm uma ocorrência de cada padrão e retiram só o excesso.

### 2.3. EBIA: um JSON

| Parte do PDF | Páginas do PDF | Tratamento |
|---|---|---|
| Elementos pré-textuais: capa e sumário | 1 e 2 | **Fora do recorte** |
| Texto | 3 a 52 | Entra |
| Páginas depois da p. 52, se houver | a partir da 53 | Fora do recorte |

| JSON | Páginas do PDF |
|---|---|
| `EBIA_extracao.json` | 3 a 52 |

Antes de extrair, o agente confere que a capa e o sumário terminam na p. 2 e que o texto começa na p. 3; se não for assim, **para e pergunta**. Páginas posteriores à p. 52 ficam fora por comando, e a mensagem final diz em uma linha o que continham. O pesquisador não indicou um padrão repetitivo específico para a EBIA: o agente verifica se há algum que atenda aos critérios da seção 3.2.1.

---

## 3. Diretrizes para a extração

### 3.1. Princípio geral: fidelidade integral

Dentro de cada unidade incluída, o texto deve ser **idêntico ao original**. O **único acréscimo permitido é o asterisco de marcação** da seção 3.2: retirados os asteriscos, o `text` volta a ser exatamente o texto do PDF (consideradas as normalizações da seção 3.5). A autonomia do agente vale para reconhecer o corpo essencial e identificar os padrões de repetição, e nunca para alterar **o que está escrito**. Fica **PROIBIDO**:

| Proibido | Exemplo do que não pode acontecer |
|---|---|
| **Exclusão** | Retirar do corpo do texto qualquer palavra, expressão, rótulo, título ou parágrafo, **inclusive os repetidos**. Repetições são marcadas, nunca retiradas |
| **Distorção** | Alterar palavras, sentido, tempo verbal, ênfase ou pontuação significativa |
| **Generalização** | Substituir um trecho específico por uma formulação genérica ("o plano prevê investimentos em IA") |
| **Viés** | Escolher, destacar, marcar ou omitir trechos por relevância presumida para Brasil, China ou qualquer hipótese da pesquisa |
| **Abreviação** | Resumir, cortar com reticências ("[...]", "..."), condensar parágrafos ou truncar textos longos |
| **Inflação por erro de leitura** | Duplicar trechos que o documento não duplica, repetir títulos ou cabeçalhos de página, incluir o mesmo parágrafo duas vezes por erro de leitura do layout, misturar ao corpo os elementos que ficam fora (seção 3.4) |
| **Marcação indevida** | Pôr asterisco em palavra que não pertence a um padrão que atenda a todos os critérios da seção 3.2.1, ou no conteúdo variável que vem depois da expressão fixa |
| **Correção** | Corrigir ortografia, acentuação, gramática ou estilo do original, ou acrescentar "[sic]" |
| **Paráfrase ou reordenação** | Reescrever, fundir ou reordenar parágrafos, itens ou seções |
| **Expansão** | Expandir siglas (*IA*, *MCTI*, *FNDCT*), completar frases ou acrescentar explicações. Siglas ficam exatamente como aparecem no original |
| **Tradução** | Traduzir qualquer trecho, inclusive os termos em inglês que o próprio documento usa (*workshops*, por exemplo) |

Exclusões, distorções e marcações indevidas alteram contagens de palavras, frequências e proporções e, com isso, **prejudicam diretamente as visualizações** das etapas seguintes.

### 3.2. Critério central: o que entra e o que é marcado

Para cada parte do intervalo de páginas definido pelo pesquisador, o agente se pergunta:

> **Este trecho pertence ao corpo essencial do texto do documento?**

- **Sim** → entra no JSON, literal e inteiro, **mesmo que se repita** em outro lugar do documento.
- **Não** (nota de rodapé, conteúdo de tabela ou de gráfico, figura, legenda, cabeçalho ou rodapé de página, numeração de página) → fica fora (seção 3.4).

Em seguida, para o texto que entrou, o agente pergunta:

> **Há palavras que aparecem aqui só porque o texto segue um padrão fixo, repetido em grande escala?**

- **Sim, e o caso atende a todos os critérios da seção 3.2.1** → as palavras da expressão fixa recebem asterisco em todas as ocorrências do padrão.
- **Não, ou há dúvida** → nada é marcado.

#### 3.2.1. Critérios para marcar com asterisco (comando do pesquisador)

Há pontos dos documentos em que as palavras se repetem constantemente apenas porque o texto segue um padrão: uma ficha aplicada a cada ação, um rótulo fixo no início de cada item, um subtítulo idêntico em cada seção. Essa repetição é **retórica e estrutural**: não corresponde ao uso real da palavra pelo documento e inflaria a análise. As palavras dessa expressão fixa são marcadas **somente se todos os critérios abaixo forem atendidos**:

1. **Forma fixa:** a mesma expressão (mesmas palavras, na mesma posição e com a mesma função: rótulo de campo, rubrica, subtítulo fixo) se repete em uma série de unidades paralelas, como as ações de um anexo ou os eixos de um capítulo.
2. **Função estrutural:** a expressão organiza o texto (nomeia o campo ou a parte) e não diz algo novo em cada ocorrência. Lida sem ela, cada unidade continua íntegra e compreensível.
3. **Grande escala:** a repetição é sistemática, em série, ao longo de uma parte inteira do documento, como a ficha das ações dos anexos do PBIA. **Repetições de baixa escala, que ocorrem poucas vezes, não são marcadas**: um subtítulo repetido em duas ou três seções fica sem asterisco.
4. **Efeito de inflação:** a repetição aumenta de forma relevante a contagem da palavra em relação ao uso dela no texto corrido. O agente compara quantas ocorrências da palavra vêm do padrão e quantas vêm do texto corrido.

**Regras da marcação:**

- **Formato:** asterisco imediatamente depois da palavra, sem espaço e antes de qualquer pontuação: `Desafio*:`, `Impactos* esperados*:`, `Componentes* da* ação*:`.
- **Todas as palavras da expressão fixa** são marcadas, inclusive as gramaticais. Números, datas e pontuação da expressão não recebem asterisco (`Recursos* (2024-2028):`, `Ação* 50:`).
- **Nunca se marca o conteúdo variável** que acompanha a expressão (o título ou o número da ação, o texto depois do rótulo), mesmo quando esse conteúdo se repete de uma ação para outra (por exemplo, *"iniciativa única"* em *Componentes da ação*). Repetições de conteúdo desse tipo em grande escala são apenas **informadas** ao pesquisador; marcá-las depende de comando dele.
- **Nunca se marca a palavra fora do padrão.** A mesma palavra no texto corrido fica sem asterisco em todas as ocorrências.
- **Todas as ocorrências do padrão são marcadas**, inclusive a primeira, da mesma forma em todo o documento e nos dois JSONs do PBIA.
- Cada padrão marcado é registrado no catálogo `extraction.repetition_patterns` (seção 4.3), que diz **qual expressão foi marcada, onde e em quantas ocorrências**. É esse catálogo que permite às skills 02 e 03 explicar quais termos foram retirados e em que circunstâncias.
- Se o próprio texto do PDF tiver asteriscos no corpo, o agente avisa o pesquisador antes de gravar, porque a marcação ficaria ambígua.

O padrão indicado pelo pesquisador (seção 2.2) é o exemplo de referência. O agente procura **outros padrões semelhantes** nos dois documentos, por exemplo:

- outras fichas ou campos fixos repetidos em cada item (*Objetivo:*, *Meta:*, *Responsável:*, *Prazo:*);
- o mesmo subtítulo repetido no início ou no fim de cada eixo ou capítulo;
- chamadas fixas repetidas antes de cada lista.

Cada candidato só é marcado se atender aos quatro critérios. **Na dúvida, não se marca**, e o caso vai para a mensagem final como ponto para decisão do pesquisador.

#### 3.2.2. Repetição de conteúdo entre o corpo e os anexos do PBIA

Se o corpo do PBIA (p. 11–48) já apresentar títulos ou descrições de ações que os anexos repetem, esses trechos **entram literalmente nos dois lugares**, sem exclusão. Como não se trata de uma expressão fixa usada como estrutura, mas de conteúdo repetido, **não recebem asterisco**. O agente mede quantas unidades e palavras se repetem e **informa** o pesquisador, que decide se algo deve ser feito.

### 3.3. O que COMPÕE o texto essencial (entra no JSON)

Por comando do pesquisador, **tudo o que estiver dentro do corpo essencial do texto, no intervalo de páginas da seção 2, entra, de forma literal e sem exclusões**:

| Elemento | Onde fica no JSON |
|---|---|
| **Título oficial** e **subtítulo**, como constam da capa ou da folha de rosto | Apenas nos metadados (`document.title`, `document.subtitle`), para identificação. Como a capa está fora do recorte definido pelo pesquisador, o título não é repetido dentro de `sections` |
| **Títulos internos**: partes, capítulos, eixos, seções, subseções, títulos dos anexos e das ações, inclusive os subtítulos repetidos | Uma unidade `type = "heading"` cada, na posição original, com o nível hierárquico em `level` |
| **Apresentação** (no PBIA, a análise começa nela) | Unidades com `category = "Foreword"` |
| **Sumário executivo** ou síntese inicial, se houver no intervalo | Unidades com `category = "Executive summary"` |
| **Corpo do documento**: introdução, contexto, diagnóstico, visão, princípios, objetivos, eixos, ações, medidas, metas, governança, financiamento descrito em texto, implementação, monitoramento e considerações finais | Uma unidade `type = "paragraph"` por parágrafo, com `category = "Body"` |
| **Listas** (com marcadores ou numeradas), inclusive os itens das fichas das ações | Uma unidade `type = "list_item"` por item, com o marcador ou a numeração original em `number`. Listas são texto, e não tabela |
| **Quadros ou boxes de texto corrido** | Unidades com `category = "Box"` |
| **Anexos 1 e 2 do PBIA** (só no JSON com anexos) | Unidades com `category = "Annex"` |
| **Endereços eletrônicos (URLs) e remissões** que fazem parte de uma frase do corpo ("ver Anexo 2") | Ficam no texto, como estão |

As categorias registram a posição estrutural do trecho, e não o tema. Elas permitem que o pesquisador, se quiser, exclua partes na análise **sem uma nova extração** (skill 02, seção 3.1).

### 3.4. O que fica fora do JSON (comandos anteriores do pesquisador)

#### 3.4.1. Fora do intervalo definido pelo pesquisador
- **PBIA:** p. 1 a 10 (pré-textuais) e p. 94 em diante (página em branco e pós-textuais: glossário, siglas e abreviaturas, referências). No JSON sem anexos, também as p. 49 a 93 (Anexos 1 e 2).
- **EBIA:** p. 1 e 2 (capa e sumário) e o que vier depois da p. 52.
- As páginas fora do recorte podem ser lidas **só** para preencher os metadados (título, subtítulo, emissor, data), nunca para o texto.

#### 3.4.2. Elementos que não pertencem ao corpo essencial do texto, dentro do intervalo
- **Notas de rodapé e notas de fim:** o texto da nota **e** o marcador dela no corpo (número ou símbolo sobrescrito, que a extração do PDF costuma colar à palavra ou à pontuação, como `dados12` ou `IA.3`).
- **Tabelas:** todo o conteúdo organizado em linhas e colunas, com título, cabeçalho, células, notas e fonte.
- **Gráficos, figuras, infográficos, mapas, diagramas e fluxogramas**, com os textos internos, os números em destaque, as legendas e as linhas de fonte ("Fonte: …").
- **Elementos de página e de diagramação:** cabeçalhos e rodapés de página, numeração de página, marcas d'água, chamadas de navegação, citações em destaque que reproduzem uma frase do corpo (a frase fica no corpo), assinaturas e cargos ao fim de apresentações, créditos de imagem.
- Se uma tabela ou um gráfico trouxer conteúdo central (por exemplo, recursos por eixo, ou ações apresentadas só em forma de tabela), o conteúdo continua fora, e a mensagem final **avisa** o pesquisador, que decide.

Na dúvida sobre se um trecho pertence ao corpo essencial do texto, **ele entra**, e o caso é informado ao pesquisador.

### 3.5. Normalizações técnicas permitidas

Apenas as normalizações abaixo são permitidas:

1. **Reunião de palavras hifenizadas por quebra de linha** do PDF (por exemplo, `regu-` + `lação` → `regulação`), somente quando a hifenização for artefato de diagramação. Os hífens da própria palavra ficam (`bem-estar`, `pós-graduação`, `tornar-se`, `desenvolvê-la`); na dúvida, prevalece a grafia da palavra em português.
2. **Remoção de quebras de linha internas** ao parágrafo, causadas pela diagramação.
3. **Redução de espaços em branco múltiplos** a um único espaço.
4. **Correção de caracteres corrompidos pela extração** (ligaduras como `ﬁ` → `fi`; acentos decompostos ou corrompidos pela camada de texto do PDF), com normalização Unicode NFC, sem nenhuma outra alteração. O texto não é passado para minúsculas e não perde acentos.
5. **Inserção do asterisco de marcação** (seção 3.2.1), único acréscimo permitido ao texto.

**Ordem de leitura:** em páginas com colunas, caixas laterais ou texto em volta de figuras, segue-se a ordem de leitura do documento, e não a ordem bruta da camada de texto do PDF. Quando a camada de texto não deixar clara a estrutura (colunas, notas, rótulos, caixas), o agente confere a imagem da página.

Qualquer outra intervenção no texto é **proibida**.

### 3.6. Casos de dúvida

- **Dúvida sobre se um trecho pertence ao corpo essencial:** ele entra, e o caso é informado.
- **Dúvida sobre se uma repetição deve ser marcada:** não se marca, e o caso é informado como ponto para decisão do pesquisador.
- Toda decisão vale para todos os casos semelhantes do documento e vai para a mensagem final.

O agente **para e pergunta** quando: a dúvida for sobre o **comando** do pesquisador; as páginas do PDF não corresponderem às indicadas na seção 2; o texto do PDF tiver asteriscos próprios no corpo; ou o arquivo-fonte não permitir uma extração confiável (texto em imagem, OCR falho, páginas ilegíveis).

---

## 4. Protocolo de operação e entregáveis

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar o insumo:** confirmar que o PDF foi anexado ou está na pasta, que é a EBIA ou o PBIA, que está em português e que é legível. Se não for, **parar e perguntar**.
3. **Verificar se já existe** o JSON pedido (seção 4.2). Se existir, **parar e perguntar** antes de prosseguir.
4. **Conferir as bordas** de página da seção 2. Se não se confirmarem, **parar e perguntar**.
5. **Ler o intervalo integralmente**, do início ao fim.
6. **Compreender a estrutura** e **mapear os candidatos a padrão de repetição**: quais expressões se repetem, quantas vezes, em que partes e com que efeito sobre a contagem das palavras. Aplicar os quatro critérios da seção 3.2.1 a cada candidato. No PBIA, o mapeamento é feito sobre o recorte com anexos e aplicado igualmente aos dois JSONs; verificar também a repetição de conteúdo entre o corpo e os anexos (seção 3.2.2).
7. **Segmentar** o texto essencial em unidades: um registro por título interno, por parágrafo ou por item de lista, na ordem original.
8. **Extrair** cada unidade literalmente, aplicando apenas as normalizações da seção 3.5, e **marcar** as palavras dos padrões aprovados.
9. **Preencher os metadados** **somente com informações que constam no próprio PDF**. Campo sem informação no documento → `null`. Nunca inferir, deduzir ou buscar fora.
10. **Registrar** cada padrão marcado no catálogo `extraction.repetition_patterns`.
11. **PBIA:** montar primeiro a sequência completa (p. 11–93) e obter a versão sem anexos cortando-a ao fim da p. 48, para que as unidades comuns aos dois JSONs sejam idênticas, inclusive nas marcações. Se um dos dois JSONs já existir, o outro é gerado de modo que as unidades comuns coincidam com as dele.
12. **Verificar** a extração conforme a seção 4.4.
13. **Gravar** apenas os JSONs (seção 4.2).
14. **Informar** ao pesquisador, na conversa (seção 4.5).

### 4.2. Entregáveis

São entregues **APENAS** os JSONs, gravados nesta pasta:

| Documento | Arquivo |
|---|---|
| PBIA sem anexos (p. 11–48) | `PBIA_sem_anexos_extracao.json` |
| PBIA com anexos (p. 11–93) | `PBIA_com_anexos_extracao.json` |
| EBIA (p. 3–52) | `EBIA_extracao.json` |

- **Sem relatórios.** Por comando do pesquisador, esta etapa não produz relatório de extração, nem em Markdown nem em CSV, e não cria a subpasta `relatorios_extracao/`. O que o pesquisador precisa saber vai na mensagem final da conversa (seção 4.5).
- Os dois JSONs do PBIA são **recortes definidos pelo pesquisador**, e não versões paralelas. Fora isso, há **um único JSON por recorte**: não se criam `_v2`, `_v3`, …
- Se o pesquisador indicar outro nome de arquivo, vale o nome indicado.
- Se o JSON **já existir**, o agente não o sobrescreve por conta própria: informa ao pesquisador e só o substitui **por comando dele**.
- Nenhum outro arquivo (resumos, gráficos, scripts, rascunhos, cópias do PDF) é deixado na pasta sem comando do pesquisador. Arquivos temporários ficam fora do repositório.

### 4.3. Estrutura do JSON

Codificação **UTF-8**, sem escapar caracteres especiais (`ensure_ascii=False`), indentação de 2 espaços. A estrutura é a mesma da pasta `Planos Nacionais de IA`, com os acréscimos `extraction.cut`, `extraction.page_range`, `extraction.repetition_marker`, `extraction.marked_words`, `extraction.repetition_patterns` e `sections[].marked_patterns`.

```json
{
  "document": {
    "title": "Título oficial, exatamente como no documento",
    "subtitle": "Subtítulo oficial, exatamente como no documento, ou null",
    "issuer": "Órgão ou instituição emissora, conforme o documento",
    "country_or_bloc": "País a que o documento se refere, conforme o documento",
    "date": "Data de publicação ou de aprovação, conforme o documento, ou null",
    "period": "Período de vigência, conforme o documento, ou null",
    "language": "pt",
    "source_file": "nome_do_arquivo_fonte.pdf",
    "source_sha256": "SHA-256 do PDF usado na extração, ou null se o agente não tiver acesso ao arquivo",
    "pages": 0
  },
  "extraction": {
    "skill": "skill_extração",
    "corpus": "EBIA_PBIA",
    "skill_version": "1.1",
    "date": "AAAA-MM-DD",
    "cut": "com_anexos",
    "page_range": [11, 93],
    "units_extracted": 0,
    "headings_extracted": 0,
    "paragraphs_extracted": 0,
    "list_items_extracted": 0,
    "words_extracted": 0,
    "characters_extracted": 0,
    "repetition_marker": "*",
    "marked_words": 0,
    "repetition_patterns": [
      {
        "id": 1,
        "expression": "Desafio:",
        "marked_as": "Desafio*:",
        "where": "Rótulo no início do item 'Desafio' da ficha de cada ação dos Anexos 1 e 2",
        "occurrences": 0,
        "marked_words": 0
      }
    ]
  },
  "sections": [
    {
      "id": 1,
      "type": "list_item",
      "level": null,
      "category": "Annex",
      "path": ["Título do anexo", "Título da ação, como no original"],
      "number": "»",
      "page": 0,
      "marked_patterns": [1],
      "text": "Desafio*: texto integral e literal do item."
    }
  ]
}
```

*(O exemplo mostra só a forma dos campos; os valores reais vêm do PDF.)*

**Regras do JSON:**
- `id`: inteiro sequencial a partir de 1, na ordem original do documento.
- `type`: `heading` (título interno), `paragraph` (parágrafo) ou `list_item` (item de lista).
- `level`: nível do título interno (1 = nível mais alto), conforme a numeração e a tipografia do documento; `null` nas demais unidades.
- `category`: posição estrutural do trecho, e **não** classificação temática: `Foreword`, `Executive summary`, `Body`, `Box` ou `Annex`.
- `path`: títulos internos acima da unidade, do nível mais alto ao mais baixo, com o texto literal **completo e sem asteriscos**; `[]` quando não houver. Serve apenas para localizar e agrupar as unidades.
- `number`: numeração ou marcador **puro**, exatamente como no original (`"1."`, `"a)"`, `"»"`), sem renumerar.
- `page`: página do **arquivo PDF** em que a unidade começa (1 = primeira página do arquivo), e não a numeração impressa.
- `text`: o texto literal e integral da unidade, com os asteriscos de marcação. Nunca vazio, nunca truncado, nunca com reticências inseridas pelo agente.
- `marked_patterns`: lista dos `id` de padrão de cada ocorrência marcada na unidade, **na ordem em que aparecem no `text`**; `[]` quando não houver. Uma ocorrência é o conjunto das palavras marcadas de uma mesma expressão fixa (no texto, palavras marcadas seguidas, separadas só por espaço, números ou pontuação).
- `cut`: `"sem_anexos"` ou `"com_anexos"` nos JSONs do PBIA; `null` na EBIA.
- `page_range`: primeira e última página do PDF cobertas pelo recorte, conforme o comando do pesquisador.
- `repetition_marker`: sempre `"*"`.
- `marked_words`: total de palavras marcadas com asterisco em todas as unidades.
- `repetition_patterns`: catálogo dos padrões marcados, um registro por expressão fixa, com `expression` (literal, como no original; partes variáveis indicadas de forma genérica, como em `"Ação NN:"`), `marked_as` (a mesma expressão com os asteriscos), `where` (em que circunstância ela aparece: em que parte do documento, em que posição e em que tipo de unidade), `occurrences` e `marked_words` (contados neste JSON). `[]` quando não houver padrão marcado.
- `words_extracted`: palavras separadas por espaço no `text` de todas as unidades.
- Os contadores do bloco `extraction` devem corresponder exatamente ao conteúdo de `sections`.

### 4.4. Verificação obrigatória antes da entrega

1. **Literalidade:** retirados os asteriscos de marcação, cada `text` do JSON, consideradas apenas as normalizações da seção 3.5, é encontrado no texto do PDF.
2. **Nada excluído do corpo:** toda parte do corpo essencial do texto no intervalo está no JSON, inclusive as repetições; o que ficou fora corresponde apenas à seção 3.4.
3. **Intervalo:** todas as unidades estão nas páginas do recorte (`page_range`); a primeira unidade está na página inicial e a última, na página final.
4. **Marcação correta e completa:** todo asterisco do texto pertence a uma ocorrência registrada em `marked_patterns` e a um padrão do catálogo; toda ocorrência de cada padrão no recorte está marcada; nenhuma palavra do texto corrido nem do conteúdo variável está marcada; os contadores do catálogo batem com o texto.
5. **Ausência de resíduos:** nenhum marcador de nota colado às palavras, cabeçalho, rodapé, número de página, linha de "Fonte:", célula de tabela ou texto de gráfico; nenhum trecho duplicado por erro de leitura.
6. **Identidade dos recortes do PBIA:** as unidades do JSON sem anexos são idênticas, campo a campo e com as mesmas marcações, às primeiras unidades do JSON com anexos; as unidades restantes do JSON com anexos começam na p. 49 ou depois e têm `category = "Annex"`.
7. **Ordem e hierarquia:** a sequência dos `id` reproduz a ordem do PDF, e `level` e `path` reproduzem a hierarquia dos títulos internos.
8. **Consistência:** os contadores do bloco `extraction` batem com o conteúdo efetivo do JSON.
9. **Validade técnica:** o JSON abre sem erro em um leitor padrão.

Se qualquer verificação falhar, o agente corrige antes de entregar. Se não conseguir corrigir, **informa a falha** ao pesquisador em vez de entregar um resultado incorreto.

### 4.5. Mensagem final ao pesquisador (sem arquivo)

No lugar de relatório, o agente escreve na conversa uma mensagem **curta e apenas informativa**, com:

- os arquivos gravados, as páginas cobertas e os totais (unidades por tipo e palavras);
- o que ficou de fora, por tipo e com as páginas, sem transcrever o conteúdo excluído;
- os padrões marcados com asterisco: a expressão, onde aparece, o número de ocorrências e de palavras marcadas;
- os candidatos que **não** foram marcados e por quê (qual critério da seção 3.2.1 não foi atendido);
- o que depende da decisão do pesquisador: repetições de conteúdo em grande escala que ficaram sem marcação, tabelas ou gráficos com conteúdo central, limitações do PDF e qualquer decisão do agente que possa alterar os resultados.

A mensagem não é insumo das etapas seguintes. O que vale adiante é o JSON (com o catálogo de padrões) e, acima de tudo, os comandos do pesquisador.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** os comandos do pesquisador são a decisão final e são obedecidos em última instância, inclusive contra as regras desta skill.
2. **Comandos registrados:** os intervalos de páginas, os recortes e as exclusões da seção 2 são cumpridos exatamente como foram dados.
3. **Literalidade sem exclusões:** dentro do corpo essencial do texto, nada é retirado, inclusive as repetições. O único acréscimo é o asterisco.
4. **Marcação com rigor:** só se marcam as palavras das expressões fixas que atendem aos quatro critérios da seção 3.2.1, em todas as suas ocorrências e em nenhum outro lugar. Na dúvida, não se marca.
5. **Divisão de tarefas:** a extração identifica e marca; a retirada do excesso é feita pelas skills 02 e 03.
6. **Neutralidade:** nenhum trecho é incluído, deixado de fora ou marcado por parecer mais ou menos relevante para Brasil, China ou para a governança da IA. O critério é **apenas** estrutural.
7. **Exclusividade das fontes:** só se usa o PDF anexado pelo pesquisador. Nenhum dado, metadado ou contexto vem de fora sem pedido expresso dele.
8. **Não inventar dados:** nenhum valor, data, nome ou trecho é deduzido, estimado ou completado. Informação ausente fica `null`.
9. **Transparência sobre limitações:** problemas do PDF são informados ao pesquisador e nunca contornados em silêncio.
10. **Sem relatórios:** só os JSONs são gravados.
11. **Preservação do material existente:** arquivos-fonte e JSONs existentes nunca são alterados ou apagados sem comando do pesquisador.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma extração imprecisa, incompleta ou com marcações indevidas compromete todas as etapas seguintes e a validade dos resultados publicados. O padrão exigido é o máximo, e **a decisão final é sempre do pesquisador**.
