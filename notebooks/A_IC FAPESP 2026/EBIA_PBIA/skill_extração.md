---
name: skill_extração
description: Etapa 01 do fluxo de análise da EBIA e do PBIA (IC FAPESP 2026). A partir do PDF anexado pelo pesquisador, extrai em português todo o texto do corpo essencial do documento, nos intervalos de páginas definidos por ele, sem notas de rodapé, sem o conteúdo de gráficos e tabelas e sem as repetições de padrão que inflam as contagens. Entrega apenas JSON (PBIA sem anexos, PBIA com anexos e EBIA) e não produz relatório.
etapa: 01
versao: 1.0
data: 2026-10-09
---

# Skill de Extração — EBIA e PBIA (Etapa 01)

> **Aplicação obrigatória.** Toda extração feita na pasta `notebooks/A_IC FAPESP 2026/EBIA_PBIA/` **deve** passar por esta skill. Nenhuma extração pode ser feita fora deste protocolo, de forma parcial ou por atalho. Sempre que for pedido um comando de extração nesta pasta, o agente lê esta skill antes de começar e a cumpre por inteiro.

> ⚠️ **O COMANDO DO PESQUISADOR É A DECISÃO FINAL E É OBEDECIDO EM ÚLTIMA INSTÂNCIA.** Ele prevalece sobre qualquer regra desta skill e sobre qualquer julgamento do agente. Os comandos que o pesquisador já deu para a EBIA e o PBIA estão na seção 2 e são obrigatórios; um comando novo dele prevalece inclusive sobre esses. O agente não reinterpreta, não "melhora" e não deixa de cumprir um comando por achar outra solução mais adequada.

---

## 1. Contexto

### 1.1. A pesquisa e o pedido do pesquisador

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **EBIA_PBIA** reúne os dois documentos centrais da política brasileira de inteligência artificial: a **Estratégia Brasileira de Inteligência Artificial (EBIA)** e o **Plano Brasileiro de Inteligência Artificial (PBIA)**.

**O pedido:** o pesquisador anexa à conversa o **PDF** de um dos documentos e quer, como resultado, **um JSON com a extração de todo o texto desse PDF** que pertence ao corpo essencial do documento, no intervalo de páginas que ele definiu (seção 2), sem os elementos que não são importantes para a análise ou que inflam o resultado.

**Os dois documentos estão em português** e são extraídos e analisados nesse idioma. O agente não traduz nada.

Os dados produzidos aqui sustentam análises e visualizações que entram em relatórios científicos. Por isso, **qualquer erro de extração passa para todas as etapas seguintes** e compromete a validade dos resultados.

### 1.2. Rigor acadêmico e metodológico

O agente deve agir com o rigor de um procedimento científico documentado:

- Cada comando pedido é executado conforme esta skill e o pedido do pesquisador, sem atalhos.
- Cada decisão relevante (incluir, excluir, retirar um rótulo repetitivo) é **explícita**, vale da mesma forma para todo o documento e é **informada ao pesquisador** na mensagem final (seção 4.5).
- O procedimento é **reprodutível**: outra pessoa que aplique esta skill ao mesmo PDF, com os mesmos comandos, deve chegar a um resultado equivalente.
- Se o **comando** do pesquisador for ambíguo, contraditório ou não estiver coberto por esta skill, o agente **para e pergunta**. Já as dúvidas sobre o **documento** (o que é texto essencial, o que infla a contagem) são resolvidas pelo próprio agente, com o critério da seção 3.2.

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
| **01** | **Extração do texto essencial de cada documento para JSON** | **esta skill** |
| 02 | Análise individual de cada JSON, em notebook | `skill_análise_individual.md` |
| 03 | Análise conjunta da EBIA e do PBIA, em notebook | `skill_análise_conjunta.md` |

A Etapa 01 **não faz análise**: não interpreta, não classifica por tema, não conta termos, não resume e não gera gráficos. A função dela é entregar uma base textual fiel, limpa e sem inflação para as etapas seguintes. **O único produto desta etapa é o JSON.** Não há relatório de extração.

### 1.5. Autoridade do pesquisador e autonomia do agente

Ordem de precedência, da mais forte para a mais fraca:

1. **o comando atual do pesquisador;**
2. **os comandos do pesquisador registrados na seção 2;**
3. as demais regras desta skill;
4. o julgamento do agente, apenas no que os itens anteriores não definem.

- O pesquisador tem a **decisão final** sobre o que compõe o texto de cada documento. Se ele mandar incluir ou excluir algo, o agente cumpre, mesmo que contrarie os critérios desta skill. Se enxergar um risco no comando, o agente cumpre e menciona o risco em uma linha na mensagem final; nunca troca a decisão do pesquisador pela sua.
- Dentro do que o pesquisador não definiu, o agente tem **autonomia de julgamento**: compreende o documento e decide, com bom senso, o que é texto essencial, o que infla as contagens e o que não deve entrar na análise. As orientações da seção 3 não são uma lista fechada: o agente reconhece também os casos que elas não preveem.
- Autonomia não é arbítrio: toda decisão segue o critério central da seção 3.2, vale igualmente para todo o documento e é informada ao pesquisador. Decisões que mudariam um recorte definido por ele (por exemplo, retirar conteúdo dos anexos por estar repetido no corpo) **não** são tomadas sem perguntar.

---

## 2. Comandos do pesquisador para este corpus

Estes comandos foram dados pelo pesquisador e são **obrigatórios**. Prevalecem sobre as demais seções desta skill e só podem ser mudados por um novo comando dele.

### 2.1. Comandos comuns aos dois documentos

| Comando do pesquisador | Aplicação |
|---|---|
| O pesquisador anexa um PDF e quer como resultado um JSON com a extração de todo o texto desse PDF | Seções 3 e 4 |
| Os textos estão em português | Extração em português, sem tradução; `document.language = "pt"` |
| Excluir os elementos que não são importantes para a análise ou que inflam o resultado | Seção 3.2 |
| Não incluir notas de rodapé nem elementos que não estejam no corpo essencial do texto | Seção 3.4 |
| **Tudo o que estiver dentro do corpo essencial do texto entra na análise** | Seção 3.3 |
| Não incluir nos textos o conteúdo de gráficos e de tabelas | Seção 3.4 |
| Retirar o excesso das palavras que se repetem constantemente apenas por seguirem um padrão do texto, quando isso ocorre em grande escala. **Não retirar a palavra como um todo**, só a parte em que ela se repete de forma retórica. Repetições de baixa escala, que ocorrem poucas vezes, não são tratadas | Seção 3.2.1 |
| Não produzir relatórios | Seção 4.2 |

As páginas indicadas pelo pesquisador são sempre **páginas do arquivo PDF** (1 = primeira página do arquivo), e não a numeração impressa no documento.

### 2.2. PBIA: dois JSONs

| Parte do PDF | Páginas do PDF | Tratamento |
|---|---|---|
| Elementos pré-textuais: capa, organização, autores, edição, coordenação, ministérios que participaram e sumário | 1 a 10 | **Excluídos** |
| Texto, da Apresentação até o fim das Considerações finais | 11 a 48 | Entra nos dois JSONs |
| Anexo 1. Ações de impacto imediato e Anexo 2. Ações estruturantes | 49 a 92 | Entra **só** no JSON com anexos |
| Elementos pós-textuais: glossário de termos utilizados pelo PBIA e siglas e abreviaturas | a partir da 93 | **Excluídos** |

| JSON | Páginas do PDF | Termina em |
|---|---|---|
| `PBIA_sem_anexos_extracao.json` | 11 a 48 | Fim das Considerações finais (p. 48) |
| `PBIA_com_anexos_extracao.json` | 11 a 92 | Fim da p. 92, com os Anexos 1 e 2 |

Ao receber o PDF do PBIA, o agente produz os dois JSONs, salvo comando diferente do pesquisador.

**Conferência das bordas.** O pesquisador indicou a análise da p. 11 até a p. 93, com a retirada dos elementos pós-textuais, e fixou o fim da versão com anexos ao fim da p. 92. Antes de extrair, o agente confere no PDF que: a p. 11 começa na Apresentação; a p. 48 encerra as Considerações finais; o Anexo 1 começa na p. 49; a p. 92 encerra o Anexo 2; e a p. 93 traz apenas elementos pós-textuais. Se algum desses pontos não se confirmar (por exemplo, outra edição do PDF ou texto do Anexo 2 na p. 93), o agente **para e pergunta**.

**Padrão repetitivo indicado pelo pesquisador (Anexos 1 e 2).** Cada ação dos anexos segue a mesma ficha, como neste trecho:

```text
● Ação 50: Guias Brasileiros de IA Responsável
Série de guias sobre IA no Brasil para promover o uso responsável e adaptado à realidade nacional.
   » Desafio: necessidade de promoção da confiança pública na IA e adaptação dos padrões globais à realidade brasileira.
   » Metas: elaboração e publicação do Guia para IA Ética e Responsável em três meses; lançamento do Guia de IA para o Setor Público em 6 meses; e realização de workshops e eventos periódicos para divulgação dos guias.
   » Impactos esperados: aumento do entendimento e da confiança da população, de servidores públicos e profissionais sobre o uso e as aplicações da IA; e promoção de práticas responsáveis na adoção e no desenvolvimento de IA, alinhadas com padrões globais e adaptadas ao contexto nacional.
   » Recursos (2024-2028): R$ 500 mil - Ministério da Justiça e Segurança Pública (MJSP) -.
   » Componentes da ação: iniciativa única.
```

Os rótulos **"Ação NN"**, **"Desafio"**, **"Metas"**, **"Impactos esperados"**, **"Recursos (2024-2028)"** e **"Componentes da ação"** repetem-se em todas as ações e inflariam as palavras *ação*, *desafio*, *meta*, *impacto*, *esperado*, *recurso* e *componente*. Por comando do pesquisador, esses rótulos saem do `text` e ficam registrados no campo `label`. O conteúdo que vem depois de cada rótulo fica integralmente:

| No PDF | `type` | `label` | `text` |
|---|---|---|---|
| ● Ação 50: Guias Brasileiros de IA Responsável | `heading` | `Ação 50` | Guias Brasileiros de IA Responsável |
| Série de guias sobre IA no Brasil para promover o uso responsável e adaptado à realidade nacional. | `paragraph` | `null` | Série de guias sobre IA no Brasil para promover o uso responsável e adaptado à realidade nacional. |
| » Desafio: necessidade de promoção da confiança pública na IA e adaptação dos padrões globais à realidade brasileira. | `list_item` | `Desafio` | necessidade de promoção da confiança pública na IA e adaptação dos padrões globais à realidade brasileira. |
| » Metas: elaboração e publicação do Guia para IA Ética e Responsável em três meses; (…) | `list_item` | `Metas` | elaboração e publicação do Guia para IA Ética e Responsável em três meses; (…) |
| » Impactos esperados: aumento do entendimento e da confiança da população, (…) | `list_item` | `Impactos esperados` | aumento do entendimento e da confiança da população, (…) |
| » Recursos (2024-2028): R$ 500 mil - Ministério da Justiça e Segurança Pública (MJSP) -. | `list_item` | `Recursos (2024-2028)` | R$ 500 mil - Ministério da Justiça e Segurança Pública (MJSP) -. |
| » Componentes da ação: iniciativa única. | `list_item` | `Componentes da ação` | iniciativa única. |

*(Nesta tabela, "(…)" só abrevia o exemplo; no JSON, o `text` é sempre integral. O " -." final do item de recursos também fica, porque está no original.)*

As mesmas palavras, quando usadas no texto corrido (por exemplo, *"as metas do plano"*, *"cada ação"*, *"recursos do FNDCT"*), **ficam**: o que sai é só a repetição do rótulo.

### 2.3. EBIA: um JSON

| Parte do PDF | Páginas do PDF | Tratamento |
|---|---|---|
| Elementos pré-textuais: capa e sumário | 1 e 2 | **Excluídos** |
| Texto | 3 a 52 | Entra |
| Páginas depois da p. 52, se houver | a partir da 53 | Fora do recorte |

| JSON | Páginas do PDF |
|---|---|
| `EBIA_extracao.json` | 3 a 52 |

Antes de extrair, o agente confere que a capa e o sumário terminam na p. 2 e que o texto começa na p. 3; se não for assim, **para e pergunta**. Páginas posteriores à p. 52 ficam fora por comando, e a mensagem final diz em uma linha o que continham. O pesquisador não indicou um padrão repetitivo específico para a EBIA: o agente verifica se há algum de grande escala (seção 3.2.1).

---

## 3. Diretrizes para a extração

### 3.1. Princípio geral: fidelidade integral

Dentro de cada unidade incluída, o texto deve ser **idêntico ao original**. A autonomia do agente vale para decidir **o que entra** e para retirar os **rótulos repetitivos** da seção 3.2.1, e nunca para alterar **o que está escrito**. Fica **PROIBIDO**:

| Proibido | Exemplo do que não pode acontecer |
|---|---|
| **Distorção** | Alterar palavras, sentido, tempo verbal, ênfase ou pontuação significativa |
| **Generalização** | Substituir um trecho específico por uma formulação genérica ("o plano prevê investimentos em IA") |
| **Viés** | Escolher, destacar ou omitir trechos por relevância presumida para Brasil, China ou qualquer hipótese da pesquisa |
| **Abreviação** | Resumir, cortar com reticências ("[...]", "..."), condensar parágrafos ou truncar textos longos |
| **Inflação de dados** | Duplicar trechos, repetir títulos ou cabeçalhos de página, incluir o mesmo parágrafo duas vezes por erro de leitura do layout, misturar elementos excluídos ao corpo, deixar no texto os rótulos repetitivos da seção 3.2.1 |
| **Correção** | Corrigir ortografia, acentuação, gramática ou estilo do original, ou acrescentar "[sic]" |
| **Paráfrase ou reordenação** | Reescrever, fundir ou reordenar parágrafos, itens ou seções |
| **Expansão** | Expandir siglas (*IA*, *MCTI*, *FNDCT*), completar frases ou acrescentar explicações. Siglas ficam exatamente como aparecem no original |
| **Tradução** | Traduzir qualquer trecho, inclusive os termos em inglês que o próprio documento usa (*workshops*, por exemplo) |

Distorções, abreviações e inflações alteram contagens de palavras, frequências e proporções e, com isso, **prejudicam diretamente as visualizações** das etapas seguintes.

### 3.2. Critério central: o que deve estar, o que não deve e o que infla

Para cada parte do intervalo de páginas definido pelo pesquisador, o agente se pergunta:

> **Este trecho é texto do documento, escrito pelo emissor como parte do corpo essencial do seu conteúdo, e aparece aqui uma única vez?**

- **Sim** → entra no JSON.
- **É moldura editorial ou aparato de consulta** (capa, créditos, sumário, glossário, lista de siglas, cabeçalhos e rodapés) → não entra.
- **É conteúdo, mas repetido** (o mesmo texto dito de novo em outro lugar) → entra só uma vez, na posição em que de fato integra o texto (com a ressalva da seção 3.2.2).
- **É nota de rodapé, tabela, gráfico, figura ou legenda** → não entra (seção 3.4).
- **É rótulo de um padrão repetitivo de grande escala** → o rótulo sai do texto e o conteúdo que ele introduz fica (seção 3.2.1).

**O que infla a análise.** O agente deve reconhecer, em cada documento, o que faria um termo ser contado mais vezes do que o documento efetivamente o emprega:

| Fonte de inflação | Tratamento |
|---|---|
| Cabeçalhos e rodapés de página repetidos (título do documento, nome do capítulo), numeração de página, marcas d'água | Não entram |
| Sumário, glossário e listas de siglas, que repetem os títulos e os termos do corpo | Não entram (já ficam fora pelos intervalos da seção 2) |
| Citações ou números em destaque que reproduzem uma frase ou um dado do corpo | Não entram; a frase fica só no corpo |
| Rótulos de padrões repetitivos de grande escala (por exemplo, a ficha das ações dos anexos do PBIA) | Seção 3.2.1 |
| Trecho lido duas vezes pela extração do PDF (colunas, caixas laterais) | Corrigir a leitura para que o trecho apareça uma vez |

Esses exemplos não esgotam os casos. Diante de um padrão novo, o agente aplica o mesmo raciocínio e informa a decisão ao pesquisador.

#### 3.2.1. Padrões repetitivos de grande escala (comando do pesquisador)

Há pontos dos documentos em que as palavras se repetem constantemente apenas porque o texto segue um padrão: uma ficha aplicada a cada ação, um rótulo fixo no início de cada item, um subtítulo idêntico em cada seção. Essa repetição é **retórica e estrutural**: não corresponde ao uso real da palavra pelo documento e inflaria a análise. Por comando do pesquisador:

1. **Retira-se só a parte repetida pelo padrão (o rótulo), nunca a palavra como um todo.** A mesma palavra usada no texto corrido permanece em todas as ocorrências.
2. **Rótulo no início de um parágrafo ou de um item** (como `Desafio:` ou `Ação 50:`) → sai do `text` e vai para o campo `label`, literal, sem o sinal que o separava do texto (dois-pontos, travessão). Se o rótulo introduzir uma sublista, cada item da sublista recebe o mesmo `label`.
3. **Rótulo que funciona como título repetido** (o mesmo subtítulo em várias seções) → não vira unidade própria; fica apenas no `path` das unidades abaixo dele, o que preserva a estrutura sem multiplicar a contagem.
4. **Só se tratam padrões de grande escala**: repetições sistemáticas, em série, ao longo de uma parte inteira do documento, como os rótulos repetidos em cada uma das ações dos anexos do PBIA. **Repetições de baixa escala, que ocorrem poucas vezes, não se tratam**: um subtítulo repetido em duas ou três seções fica como está. Entre esses extremos, o agente decide pelo efeito na contagem, comparando quantas ocorrências da palavra vêm do padrão e quantas vêm do texto corrido.
5. **O conteúdo que o rótulo introduz é texto do documento e fica**, mesmo quando se repete de uma ação para outra (por exemplo, *"iniciativa única"* em *Componentes da ação*). Repetições desse tipo em grande escala são apenas **informadas** ao pesquisador; retirá-las depende de comando dele.
6. Cada padrão tratado vale da mesma forma para todo o documento e para os dois JSONs do PBIA, e é informado na mensagem final, com o número de ocorrências retiradas.

O padrão indicado pelo pesquisador (seção 2.2) é o exemplo de referência. O agente procura **outros padrões semelhantes** nos dois documentos, por exemplo:

- outras fichas ou campos fixos repetidos em cada item (*Objetivo:*, *Meta:*, *Responsável:*, *Prazo:*);
- o mesmo subtítulo repetido no início ou no fim de cada eixo ou capítulo;
- chamadas fixas repetidas antes de cada lista.

#### 3.2.2. Repetição entre o corpo e os anexos do PBIA

Se o corpo do PBIA (p. 11–48) já apresentar títulos ou descrições de ações que os anexos repetem literalmente, o JSON com anexos teria esses trechos duas vezes. Como retirar trechos dos anexos muda o recorte "com anexos" definido pelo pesquisador, o agente **não decide sozinho**: verifica se a repetição ocorre, mede quantas unidades e palavras se repetem e **pergunta** ao pesquisador antes de gravar o JSON com anexos. Essa verificação não afeta o JSON sem anexos.

### 3.3. O que COMPÕE o texto essencial (entra no JSON)

Por comando do pesquisador, **tudo o que estiver dentro do corpo essencial do texto, no intervalo de páginas da seção 2, entra na análise**:

| Elemento | Onde fica no JSON |
|---|---|
| **Título oficial** e **subtítulo**, como constam da capa ou da folha de rosto | Apenas nos metadados (`document.title`, `document.subtitle`), para identificação. Como a capa foi excluída pelo pesquisador, o título não é repetido dentro de `sections` |
| **Títulos internos**: partes, capítulos, eixos, seções, subseções, títulos dos anexos e das ações | Uma unidade `type = "heading"` cada, na posição original, com o nível hierárquico em `level` (exceto os rótulos repetidos da seção 3.2.1) |
| **Apresentação** (no PBIA, a análise começa nela) | Unidades com `category = "Foreword"` |
| **Sumário executivo** ou síntese inicial, se houver no intervalo | Unidades com `category = "Executive summary"` |
| **Corpo do documento**: introdução, contexto, diagnóstico, visão, princípios, objetivos, eixos, ações, medidas, metas, governança, financiamento descrito em texto, implementação, monitoramento e considerações finais | Uma unidade `type = "paragraph"` por parágrafo, com `category = "Body"` |
| **Listas** (com marcadores ou numeradas) | Uma unidade `type = "list_item"` por item, com o marcador ou a numeração original em `number`. Listas são texto, e não tabela |
| **Quadros ou boxes de texto corrido** com conteúdo próprio, que não repetem o corpo | Unidades com `category = "Box"` |
| **Anexos 1 e 2 do PBIA** (só no JSON com anexos) | Unidades com `category = "Annex"` |

As categorias registram a posição estrutural do trecho, e não o tema. Elas permitem que o pesquisador, se quiser, exclua partes na análise **sem uma nova extração** (skill 02, seção 3.1).

### 3.4. O que NÃO COMPÕE o texto essencial (fica fora do JSON)

#### 3.4.1. Fora do intervalo definido pelo pesquisador
- **PBIA:** p. 1 a 10 (pré-textuais) e p. 93 em diante (pós-textuais: glossário, siglas e abreviaturas). No JSON sem anexos, também as p. 49 a 92 (Anexos 1 e 2).
- **EBIA:** p. 1 e 2 (capa e sumário) e o que vier depois da p. 52.
- As páginas excluídas podem ser lidas **só** para preencher os metadados (título, subtítulo, emissor, data), nunca para o texto.

#### 3.4.2. Excluídos por comando do pesquisador, dentro do intervalo
- **Notas de rodapé e notas de fim:** o texto da nota **e** o marcador dela no corpo (número ou símbolo sobrescrito, que a extração do PDF costuma colar à palavra ou à pontuação, como `dados12` ou `IA.3`).
- **Tabelas:** todo o conteúdo organizado em linhas e colunas, com título, cabeçalho, células, notas e fonte.
- **Gráficos, figuras, infográficos, mapas, diagramas e fluxogramas**, com os textos internos, os números em destaque, as legendas e as linhas de fonte ("Fonte: …").
- Se uma tabela ou um gráfico trouxer conteúdo central (por exemplo, recursos por eixo, ou ações apresentadas só em forma de tabela), o conteúdo continua fora, e a mensagem final **avisa** o pesquisador, que decide.
- **Elementos fora do corpo essencial do texto** que apareçam no intervalo: cabeçalhos e rodapés de página, numeração de página, marcas d'água, chamadas de navegação, citações em destaque que repetem o corpo, assinaturas e cargos ao fim de apresentações, créditos de imagem.

#### 3.4.3. Links e remissões
- **Links e URLs:** retira-se apenas o endereço, sem alterar o restante da frase. Se a retirada deixar a frase sem sentido, o endereço fica.
- **Remissões no texto** a tabelas, figuras ou anexos (por exemplo, "ver Anexo 2") **permanecem**, porque fazem parte da frase.

### 3.5. Normalizações técnicas permitidas

Apenas as normalizações abaixo são permitidas:

1. **Reunião de palavras hifenizadas por quebra de linha** do PDF (por exemplo, `regu-` + `lação` → `regulação`), somente quando a hifenização for artefato de diagramação. Os hífens da própria palavra ficam (`bem-estar`, `pós-graduação`, `tornar-se`, `desenvolvê-la`); na dúvida, prevalece a grafia da palavra em português.
2. **Remoção de quebras de linha internas** ao parágrafo, causadas pela diagramação.
3. **Redução de espaços em branco múltiplos** a um único espaço.
4. **Correção de caracteres corrompidos pela extração** (ligaduras como `ﬁ` → `fi`; acentos decompostos ou corrompidos pela camada de texto do PDF), com normalização Unicode NFC, sem nenhuma outra alteração. O texto não é passado para minúsculas e não perde acentos.
5. **Retirada dos rótulos repetitivos** da seção 3.2.1, com registro em `label` ou em `path`.

**Ordem de leitura:** em páginas com colunas, caixas laterais ou texto em volta de figuras, segue-se a ordem de leitura do documento, e não a ordem bruta da camada de texto do PDF. Quando a camada de texto não deixar clara a estrutura (colunas, notas, rótulos, caixas), o agente confere a imagem da página.

Qualquer outra intervenção no texto é **proibida**.

### 3.6. Casos de dúvida

Quando não estiver claro se um trecho deve entrar, o agente **decide** com o critério da seção 3.2, aplica a mesma decisão a todos os casos semelhantes do documento e a **informa** na mensagem final, entre os pontos para decisão do pesquisador quando ela puder alterar de forma relevante os resultados.

O agente **para e pergunta** quando: a dúvida for sobre o **comando** do pesquisador; as páginas do PDF não corresponderem às indicadas na seção 2; a decisão mudar um recorte definido por ele (seção 3.2.2); ou o arquivo-fonte não permitir uma extração confiável (texto em imagem, OCR falho, páginas ilegíveis).

---

## 4. Protocolo de operação e entregáveis

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar o insumo:** confirmar que o PDF foi anexado ou está na pasta, que é a EBIA ou o PBIA, que está em português e que é legível. Se não for, **parar e perguntar**.
3. **Verificar se já existe** o JSON pedido (seção 4.2). Se existir, **parar e perguntar** antes de prosseguir.
4. **Conferir as bordas** de página da seção 2. Se não se confirmarem, **parar e perguntar**.
5. **Ler o intervalo integralmente**, do início ao fim, antes de decidir qualquer exclusão.
6. **Compreender a estrutura** e **mapear os padrões repetitivos** (seção 3.2.1): quais rótulos se repetem, quantas vezes e em que partes. No PBIA, verificar também a repetição entre o corpo e os anexos (seção 3.2.2).
7. **Segmentar** o texto essencial em unidades: um registro por título interno, por parágrafo ou por item de lista, na ordem original.
8. **Extrair** cada unidade literalmente, aplicando apenas as normalizações da seção 3.5.
9. **Preencher os metadados** **somente com informações que constam no próprio PDF**. Campo sem informação no documento → `null`. Nunca inferir, deduzir ou buscar fora.
10. **PBIA:** montar primeiro a sequência completa (p. 11–92) e obter a versão sem anexos cortando-a ao fim da p. 48, para que as unidades comuns aos dois JSONs sejam idênticas. Se um dos dois JSONs já existir, o outro é gerado de modo que as unidades comuns coincidam com as dele.
11. **Verificar** a extração conforme a seção 4.4.
12. **Gravar** apenas os JSONs (seção 4.2).
13. **Informar** ao pesquisador, na conversa (seção 4.5).

### 4.2. Entregáveis

São entregues **APENAS** os JSONs, gravados nesta pasta:

| Documento | Arquivo |
|---|---|
| PBIA sem anexos (p. 11–48) | `PBIA_sem_anexos_extracao.json` |
| PBIA com anexos (p. 11–92) | `PBIA_com_anexos_extracao.json` |
| EBIA (p. 3–52) | `EBIA_extracao.json` |

- **Sem relatórios.** Por comando do pesquisador, esta etapa não produz relatório de extração, nem em Markdown nem em CSV, e não cria a subpasta `relatorios_extracao/`. O que o pesquisador precisa saber vai na mensagem final da conversa (seção 4.5).
- Os dois JSONs do PBIA são **recortes definidos pelo pesquisador**, e não versões paralelas. Fora isso, há **um único JSON por recorte**: não se criam `_v2`, `_v3`, …
- Se o pesquisador indicar outro nome de arquivo, vale o nome indicado.
- Se o JSON **já existir**, o agente não o sobrescreve por conta própria: informa ao pesquisador e só o substitui **por comando dele**.
- Nenhum outro arquivo (resumos, gráficos, scripts, rascunhos, cópias do PDF) é deixado na pasta sem comando do pesquisador. Arquivos temporários ficam fora do repositório.

### 4.3. Estrutura do JSON

Codificação **UTF-8**, sem escapar caracteres especiais (`ensure_ascii=False`), indentação de 2 espaços. A estrutura é a mesma da pasta `Planos Nacionais de IA`, com os acréscimos `extraction.cut`, `extraction.page_range`, `extraction.labels_removed` e `sections[].label`.

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
    "skill_version": "1.0",
    "date": "AAAA-MM-DD",
    "cut": "sem_anexos",
    "page_range": [11, 48],
    "units_extracted": 0,
    "headings_extracted": 0,
    "paragraphs_extracted": 0,
    "list_items_extracted": 0,
    "labels_removed": 0,
    "words_extracted": 0,
    "characters_extracted": 0
  },
  "sections": [
    {
      "id": 1,
      "type": "heading",
      "level": 1,
      "category": "Foreword",
      "path": [],
      "number": null,
      "label": null,
      "page": 11,
      "text": "Título interno literal"
    },
    {
      "id": 2,
      "type": "paragraph",
      "level": null,
      "category": "Foreword",
      "path": ["Título interno literal"],
      "number": null,
      "label": null,
      "page": 11,
      "text": "Texto integral e literal do parágrafo."
    }
  ]
}
```

**Regras do JSON:**
- `id`: inteiro sequencial a partir de 1, na ordem original do documento.
- `type`: `heading` (título interno), `paragraph` (parágrafo) ou `list_item` (item de lista).
- `level`: nível do título interno (1 = nível mais alto), conforme a numeração e a tipografia do documento; `null` nas demais unidades.
- `category`: posição estrutural do trecho, e **não** classificação temática: `Foreword`, `Executive summary`, `Body`, `Box` ou `Annex`.
- `path`: títulos internos acima da unidade, do nível mais alto ao mais baixo, com o texto literal **completo, como no original** (inclusive o rótulo, como em `"Ação 50: Guias Brasileiros de IA Responsável"`) e com os títulos repetidos que não viraram unidade (seção 3.2.1); `[]` quando não houver. Serve apenas para localizar e agrupar as unidades.
- `number`: numeração ou marcador **puro**, exatamente como no original (`"1."`, `"a)"`, `"»"`), sem renumerar.
- `label`: rótulo repetitivo retirado do `text` (seção 3.2.1), literal, sem o sinal que o separava do texto (`"Desafio"`, `"Recursos (2024-2028)"`, `"Ação 50"`); `null` quando não houver. **Não é conteúdo analisado.**
- `page`: página do **arquivo PDF** em que a unidade começa (1 = primeira página do arquivo), e não a numeração impressa.
- `text`: nunca vazio, nunca truncado, nunca com reticências inseridas pelo agente e nunca começando por um rótulo tratado.
- `cut`: `"sem_anexos"` ou `"com_anexos"` nos JSONs do PBIA; `null` na EBIA.
- `page_range`: primeira e última página do PDF cobertas pelo recorte, conforme o comando do pesquisador.
- `labels_removed`: número de unidades com `label` preenchido.
- `words_extracted`: palavras separadas por espaço no `text` de todas as unidades.
- Os contadores do bloco `extraction` devem corresponder exatamente ao conteúdo de `sections`.

### 4.4. Verificação obrigatória antes da entrega

1. **Literalidade:** cada `text` do JSON, consideradas apenas as normalizações da seção 3.5, é encontrado no texto do PDF.
2. **Intervalo:** todas as unidades estão nas páginas do recorte (`page_range`); a primeira unidade está na página inicial e a última, na página final.
3. **Conciliação:** toda parte do intervalo está no JSON ou foi excluída por um motivo previsto nesta skill.
4. **Ausência de inflação e de resíduos:** nenhum marcador de nota colado às palavras, cabeçalho, rodapé, número de página, linha de "Fonte:", célula de tabela ou texto de gráfico; nenhum `text` começa por um rótulo tratado; nenhum trecho repetido além do que o próprio documento repete no seu texto.
5. **Identidade dos recortes do PBIA:** as unidades do JSON sem anexos são idênticas, campo a campo, às primeiras unidades do JSON com anexos; as unidades restantes do JSON com anexos começam na p. 49 ou depois e têm `category = "Annex"`.
6. **Ordem e hierarquia:** a sequência dos `id` reproduz a ordem do PDF, e `level` e `path` reproduzem a hierarquia dos títulos internos.
7. **Consistência:** os contadores do bloco `extraction` batem com o conteúdo efetivo do JSON.
8. **Validade técnica:** o JSON abre sem erro em um leitor padrão.

Se qualquer verificação falhar, o agente corrige antes de entregar. Se não conseguir corrigir, **informa a falha** ao pesquisador em vez de entregar um resultado incorreto.

### 4.5. Mensagem final ao pesquisador (sem arquivo)

No lugar de relatório, o agente escreve na conversa uma mensagem **curta e apenas informativa**, com:

- os arquivos gravados, as páginas cobertas e os totais (unidades por tipo e palavras);
- o que ficou de fora, por tipo e com as páginas, sem transcrever o conteúdo excluído;
- os padrões repetitivos tratados, com o rótulo e o número de ocorrências retiradas;
- o que depende da decisão do pesquisador: tabelas ou gráficos com conteúdo central, repetições de conteúdo em grande escala que ficaram no texto, limitações do PDF e qualquer decisão do agente que possa alterar os resultados.

A mensagem não é insumo das etapas seguintes. O que vale adiante é o JSON e, acima de tudo, os comandos do pesquisador.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** os comandos do pesquisador são a decisão final e são obedecidos em última instância, inclusive contra as regras desta skill.
2. **Comandos registrados:** os intervalos de páginas, os recortes e as exclusões da seção 2 são cumpridos exatamente como foram dados.
3. **Autonomia com critério:** no que o pesquisador não definiu, o agente decide o que entra e o que infla, com o critério da seção 3.2, de forma consistente em todo o documento e informada ao pesquisador.
4. **Fidelidade integral:** o texto de cada unidade é **100% fiel** ao original. Só os rótulos repetitivos saem do texto, e ficam registrados em `label` ou em `path`.
5. **Neutralidade:** nenhum trecho é mantido ou retirado por parecer mais ou menos relevante para Brasil, China ou para a governança da IA. O critério é **apenas** estrutural.
6. **Exclusividade das fontes:** só se usa o PDF anexado pelo pesquisador. Nenhum dado, metadado ou contexto vem de fora sem pedido expresso dele.
7. **Não inventar dados:** nenhum valor, data, nome ou trecho é deduzido, estimado ou completado. Informação ausente fica `null`.
8. **Transparência sobre limitações:** problemas do PDF são informados ao pesquisador e nunca contornados em silêncio.
9. **Sem relatórios:** só os JSONs são gravados.
10. **Preservação do material existente:** arquivos-fonte e JSONs existentes nunca são alterados ou apagados sem comando do pesquisador.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma extração imprecisa, enviesada, incompleta ou inflada compromete todas as etapas seguintes e a validade dos resultados publicados. O padrão exigido é o máximo, e **a decisão final é sempre do pesquisador**.
