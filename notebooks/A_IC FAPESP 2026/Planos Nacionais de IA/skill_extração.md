---
name: skill_extração
description: Etapa 01 do fluxo de análise dos Planos Nacionais de IA (IC FAPESP 2026). Extrai o texto essencial e literal de cada plano (título, subtítulo, títulos internos e corpo do texto) para um único JSON por plano e registra, em um relatório de texto apenas informativo, o que foi incluído, o que foi excluído e o que pode precisar de revisão.
etapa: 01
versao: 1.0
data: 2026-10-04
---

# Skill de Extração — Planos Nacionais de IA (Etapa 01)

> **Aplicação obrigatória.** Toda extração de plano feita na pasta `notebooks/A_IC FAPESP 2026/Planos Nacionais de IA/` **deve** passar por esta skill. Nenhuma extração pode ser feita fora deste protocolo, de forma parcial ou por atalho. Sempre que for pedido um comando de extração nesta pasta, o agente lê esta skill antes de começar e a cumpre por inteiro.

> ⚠️ **OS COMANDOS DO PESQUISADOR SÃO OBEDECIDOS EM ÚLTIMA INSTÂNCIA.** Eles prevalecem sobre qualquer regra desta skill. Quando um comando do pesquisador divergir do que esta skill estabelece, vale o comando.

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **Planos Nacionais de IA** reúne as estratégias e os planos governamentais de inteligência artificial, isto é, os documentos programáticos com que os governos definem objetivos, prioridades, instrumentos e arranjos institucionais para o desenvolvimento e a governança da IA. O Plano Brasileiro de Inteligência Artificial (**PBIA**) ocupa posição central nesse conjunto e é analisado em comparação com os planos de outros países e blocos, como os Estados Unidos (*Winning the Race*), a União Europeia e a China, entre outros.

**Todos os planos são fornecidos pelo pesquisador em inglês** e são extraídos e analisados nesse idioma. O agente não traduz nada.

Os dados produzidos aqui sustentam análises e visualizações que entram em relatórios científicos. Por isso, **qualquer erro de extração passa para todas as etapas seguintes** e compromete a validade dos resultados.

### 1.2. Rigor acadêmico e metodológico

O agente deve agir com o rigor de um procedimento científico documentado:

- Cada comando pedido é executado conforme esta skill e o pedido do pesquisador, sem atalhos.
- Cada decisão relevante (incluir, excluir ou normalizar um trecho) é **explícita e justificada** no relatório de extração.
- O procedimento é **reprodutível**: outra pessoa que aplique esta skill ao mesmo documento, com o mesmo critério, deve chegar a um resultado equivalente.
- Se o **comando** do pesquisador for ambíguo, contraditório ou não estiver coberto por esta skill, o agente **para e pergunta**. Já as dúvidas sobre o **documento** (o que é texto essencial, o que infla a contagem) são resolvidas pelo próprio agente, com o critério da seção 3.2.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/Planos Nacionais de IA/`.
- **Arquivo-fonte:** o documento do plano indicado pelo pesquisador, gravado nesta pasta **ou** anexado por ele à conversa. Quando o arquivo vier só como anexo, o relatório registra esse fato e recomenda gravá-lo na pasta, porque sem ele a extração não pode ser reproduzida.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - usar informações de terceiros, conhecimento prévio do modelo sobre o plano ou fontes externas (internet, bases de dados, outras edições do documento) para completar, corrigir, datar ou interpretar o texto;
  - usar análises, resultados, códigos ou arquivos de **outras pastas** do repositório, inclusive de `Declarações IA`. As skills daquela pasta serviram de modelo para estas, mas os arquivos e resultados de lá não são insumo desta etapa;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- Os **arquivos-fonte** (PDF, TXT, HTML, DOCX etc.) são **somente leitura**: nunca podem ser alterados, renomeados ou apagados.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| **01** | **Extração do texto essencial de cada plano para JSON + relatório informativo** | **esta skill** |
| 02 | Análise individual de cada plano, em notebook | `skill_análise_individual.md` |
| 03 | Análise conjunta e comparativa dos planos, em notebook | `skill_análise_comparativa.md` |

A Etapa 01 **não faz análise**: não interpreta, não classifica por tema, não conta termos, não resume e não gera gráficos. A função dela é entregar uma base textual fiel, limpa e sem inflação para as etapas seguintes. **O único produto desta etapa usado adiante é o JSON.**

### 1.5. Autoridade do pesquisador e autonomia do agente

- As **ordens e comandos do pesquisador são a decisão final** sobre o que compõe o texto de cada plano. Se o pesquisador mandar incluir ou excluir algo, o agente cumpre, mesmo que contrarie os critérios desta skill, e menciona o comando no relatório.
- Dentro do que o pesquisador não definiu, o agente tem **autonomia de julgamento**: deve compreender cada documento e decidir, com bom senso, o que é texto essencial do plano, o que infla as contagens e o que não deve entrar na análise. As listas da seção 3 são **orientações**, e não uma lista fechada: os planos variam muito de formato, e o agente deve reconhecer também os casos que elas não preveem.
- Autonomia não é arbítrio: toda decisão de inclusão ou exclusão segue o critério central da seção 3.2, é aplicada da mesma forma em todo o documento e é explicada no relatório.

---

## 2. Objetivos

### 2.1. Objetivo principal

Extrair o **texto essencial, integral e literal** de cada plano pedido (título, subtítulo, títulos internos e corpo do texto) e organizá-lo em **um único JSON por plano**, pronto para as análises das etapas seguintes, **sem nada que infle artificialmente as contagens**. Em paralelo, redigir um **relatório de extração** curto, apenas informativo, para que o pesquisador saiba o que foi feito.

### 2.2. Objetivos específicos

1. **Identificar o documento-fonte** e confirmar que corresponde ao plano indicado pelo pesquisador.
2. **Compreender a estrutura** do documento: partes pré-textuais, apresentação, sumário executivo, capítulos, eixos ou pilares, quadros, tabelas, figuras, anexos e partes pós-textuais.
3. **Decidir o que entra**, aplicando o critério central da seção 3.2 e as orientações das seções 3.3 e 3.4.
4. **Extrair literalmente** o texto essencial, preservando texto, ordem, numeração e hierarquia originais.
5. **Estruturar** o conteúdo em unidades (títulos internos, parágrafos e itens de lista), cada uma com identificador, tipo, posição na hierarquia e página.
6. **Relatar em texto** o que foi incluído, o que foi excluído e o que pode precisar de revisão.
7. **Verificar a integridade** da extração (seção 4.5).

---

## 3. Diretrizes para a extração

### 3.1. Princípio geral: fidelidade integral

Dentro de cada unidade incluída, o texto deve ser **idêntico ao original**. A autonomia do agente vale para decidir **o que entra**, e nunca para alterar **o que está escrito**. Fica **PROIBIDO**:

| Proibido | Exemplo do que não pode acontecer |
|---|---|
| **Distorção** | Alterar palavras, sentido, tempo verbal, ênfase ou pontuação significativa |
| **Generalização** | Substituir um trecho específico por uma formulação genérica ("the plan foresees investments in AI") |
| **Viés** | Escolher, destacar ou omitir trechos por relevância presumida para Brasil, China ou qualquer hipótese da pesquisa |
| **Abreviação** | Resumir, cortar com reticências ("[...]", "..."), condensar parágrafos ou truncar textos longos |
| **Inflação de dados** | Duplicar trechos, repetir títulos ou cabeçalhos de página, incluir o mesmo parágrafo duas vezes por erro de leitura do layout, misturar elementos excluídos ao corpo |
| **Correção** | Corrigir ortografia, gramática ou estilo do original, ou acrescentar "[sic]" |
| **Paráfrase ou reordenação** | Reescrever, fundir ou reordenar parágrafos, itens ou seções |
| **Expansão** | Expandir siglas, completar frases ou acrescentar explicações. Siglas ficam exatamente como aparecem no original |

Distorções, abreviações e inflações alteram contagens de palavras, frequências e proporções e, com isso, **prejudicam diretamente as visualizações** das etapas seguintes.

### 3.2. Critério central: o que deve estar, o que não deve e o que infla

Para cada parte do documento, o agente se pergunta:

> **Este trecho é texto do plano, escrito pelo emissor como parte do seu conteúdo, e aparece aqui uma única vez?**

- **Sim** → entra no JSON.
- **É moldura editorial ou aparato de consulta** (capa, créditos, sumário, lista de siglas, referências, glossário) → não entra.
- **É conteúdo, mas repetido** (o mesmo texto ou rótulo dito de novo em outro lugar) → entra só uma vez, na posição em que de fato integra o texto.
- **É dado em forma de tabela, nota de rodapé, figura ou legenda** → não entra (seção 3.4).

**O que infla a análise.** O agente deve reconhecer, em cada documento, o que faria um termo ser contado mais vezes do que o plano efetivamente o emprega. Os casos mais comuns são:

| Fonte de inflação | Tratamento |
|---|---|
| Cabeçalhos e rodapés de página repetidos, numeração de página, marcas d'água | Não entram |
| Sumário, índice e listas de siglas, que repetem os títulos e termos do corpo | Não entram |
| Citações em destaque que reproduzem uma frase do corpo | Não entram; a frase fica só no corpo |
| Sumário executivo que reproduz, em versão curta, o conteúdo do corpo | Em regra, não entra. Se trouxer conteúdo próprio, que não está no corpo, entra com `category = "Executive summary"` |
| **Rótulos estruturais repetidos**: o mesmo subtítulo usado em todas as seções (por exemplo, *Recommended Policy Actions* em cada seção de um pilar) | Não viram unidades próprias. O rótulo fica apenas no `path` das unidades que estão abaixo dele, o que preserva a estrutura sem multiplicar a contagem |
| Fórmulas repetidas de layout, como chamadas para seções ("See Section 3") isoladas em linhas próprias | Não entram quando forem só navegação; entram quando fizerem parte de uma frase do texto |
| Trecho lido duas vezes pela extração do PDF (colunas, caixas laterais) | Corrigir a leitura para que o trecho apareça uma vez |

Esses exemplos não esgotam os casos. Diante de um padrão novo, o agente aplica o mesmo raciocínio e explica a decisão no relatório.

### 3.3. O que COMPÕE o texto essencial do plano (entra no JSON)

| Elemento | Onde fica no JSON |
|---|---|
| **Título oficial** do plano, como consta da folha de rosto ou da capa | `document.title`. Não é repetido dentro de `sections` |
| **Subtítulo** ou complemento oficial do título, quando houver | `document.subtitle`. Não é repetido dentro de `sections` |
| **Títulos internos**: partes, capítulos, eixos, pilares, seções e subseções | Uma unidade `type = "heading"` cada, na posição original, com o nível hierárquico em `level` (exceto os rótulos repetidos da seção 3.2) |
| **Corpo do plano**: introdução, contexto, diagnóstico, visão, princípios, objetivos, eixos ou pilares, ações, medidas, recomendações, metas, governança, financiamento descrito em texto, implementação, monitoramento e conclusão | Uma unidade `type = "paragraph"` por parágrafo, com `category = "Body"` |
| **Listas** (com marcadores ou numeradas) que fazem parte do texto, como as listas de ações ou de recomendações | Uma unidade `type = "list_item"` por item, com o marcador ou a numeração original em `number`. Listas são texto, e não tabela |
| **Apresentação, mensagem ou prefácio** da autoridade emissora, quando expõe a visão e os objetivos do plano | Unidades com `category = "Foreword"`. Se for apenas protocolar (agradecimentos, saudações), não entra |
| **Quadros ou boxes de texto corrido** com conteúdo próprio (exemplos, iniciativas, casos), que não repetem o corpo | Unidades com `category = "Box"` |
| **Anexos que integram o plano**, quando o próprio texto os declara parte dele (por exemplo, a lista das ações do plano) | Unidades com `category = "Annex"` |

As categorias `Foreword`, `Executive summary`, `Box` e `Annex` permitem que o pesquisador, se quiser, exclua essas partes na análise **sem uma nova extração** (skill 02, seção 3.1).

### 3.4. O que NÃO COMPÕE o texto essencial (fica fora do JSON)

#### 3.4.1. Elementos pré-textuais
- Capas, contracapas e folhas de rosto (o título e o subtítulo vão para os metadados), logotipos e textos de identidade visual.
- Fichas técnicas, expedientes, créditos, equipes de elaboração e listas de autoridades.
- Fichas catalográficas, ISBN, avisos de direitos autorais e avisos legais.
- Epígrafes e dedicatórias.
- Sumários, índices, listas de siglas, de figuras, de tabelas e de quadros.
- Notas editoriais e textos sobre o próprio documento ("about this document", "how to read this plan").

#### 3.4.2. Elementos pós-textuais
- Referências bibliográficas e bibliografias.
- Glossários e índices remissivos.
- Apêndices e anexos que não integram o plano: relatórios de consulta pública, metodologia de elaboração, listas de participantes ou de contribuições, material de apoio.
- Informações de contato, agradecimentos e créditos finais.

#### 3.4.3. Elementos excluídos por determinação do pesquisador
Estes elementos ficam **sempre** fora do JSON, por comando do pesquisador:
- **Notas de rodapé e notas de fim:** o texto da nota e o **marcador** dela no corpo (números ou símbolos sobrescritos).
- **Tabelas:** toda tabela (conteúdo organizado em linhas e colunas), com título, cabeçalho, células, notas e fonte. Se uma tabela trouxer conteúdo central do plano (por exemplo, as ações ou metas apresentadas só em forma de tabela), ela continua excluída, e o relatório **avisa** o pesquisador, que decide se quer incluí-la.

#### 3.4.4. Outros elementos acessórios
- **Figuras, gráficos, infográficos, mapas, diagramas e fluxogramas**, com os textos internos, as legendas e as linhas de fonte ("Source: …").
- **Links e URLs:** retira-se apenas o endereço, sem alterar o restante da frase. Se a retirada deixar a frase sem sentido, o endereço fica.
- **Artefatos de diagramação:** cabeçalhos e rodapés de página, numeração de página, marcas d'água e chamadas de navegação ("back to contents").

**Remissões no texto** a tabelas, figuras ou anexos (por exemplo, "see Table 2") **permanecem**, porque fazem parte da frase.

### 3.5. Normalizações técnicas permitidas

Apenas as normalizações abaixo são permitidas:

1. **Reunião de palavras hifenizadas por quebra de linha** do PDF (por exemplo, `govern-` + `ance` → `governance`), somente quando a hifenização for claramente um artefato de diagramação e não um hífen original da palavra.
2. **Remoção de quebras de linha internas** ao parágrafo, causadas pela diagramação.
3. **Redução de espaços em branco múltiplos** a um único espaço.
4. **Correção de caracteres corrompidos pela extração** (por exemplo, ligaduras `ﬁ` → `fi`), sem nenhuma outra alteração.

**Ordem de leitura:** em páginas com colunas, caixas laterais ou texto em volta de figuras, segue-se a ordem de leitura do documento, e não a ordem bruta da camada de texto do PDF.

Qualquer outra intervenção no texto é **proibida**.

### 3.6. Casos de dúvida

Quando não estiver claro se um trecho deve entrar, o agente **decide** com o critério da seção 3.2, aplica a mesma decisão a todos os casos semelhantes do documento e **explica** a escolha no relatório. Se a decisão puder alterar de forma relevante os resultados (por exemplo, excluir um sumário executivo extenso ou incluir um anexo longo), ela é também listada entre os pontos que podem precisar de revisão. O agente só para e pergunta quando a dúvida for sobre o **comando** do pesquisador ou quando o arquivo-fonte não permitir uma extração confiável.

---

## 4. Protocolo de operação e entregáveis

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar os insumos:** confirmar que o arquivo-fonte pedido está nesta pasta ou anexado à conversa. Se não estiver, se estiver ilegível ou incompleto, ou se houver mais de uma versão possível do plano, **parar e perguntar** ao pesquisador.
3. **Verificar se já existe** um JSON para o plano (seção 4.2). Se existir, **parar e perguntar** antes de prosseguir.
4. **Ler o documento-fonte integralmente**, do início ao fim, antes de decidir qualquer exclusão.
5. **Compreender a estrutura** do documento e **decidir o que entra**, aplicando a seção 3. Identificar desde já as fontes de inflação próprias daquele documento.
6. **Segmentar** o texto essencial em unidades: um registro por título interno, por parágrafo ou por item de lista, na ordem original.
7. **Extrair** cada unidade literalmente, aplicando apenas as normalizações da seção 3.5.
8. **Preencher os metadados** **somente com informações que constam no próprio documento-fonte**. Campo sem informação no documento → `null`. Nunca inferir, deduzir ou buscar fora.
9. **Verificar** a extração conforme a seção 4.5.
10. **Redigir o relatório** (seção 4.4).
11. **Gravar** os dois entregáveis e informar ao pesquisador, de forma breve, os totais, as principais exclusões e os pontos que podem precisar de revisão.

### 4.2. Entregáveis

São entregues **APENAS** dois arquivos por plano:

| Entregável | Local e nome do arquivo | Conteúdo |
|---|---|---|
| 1 | `Planos Nacionais de IA/<SIGLA>_extracao.json` | Texto essencial, integral e literal do plano |
| 2 | `Planos Nacionais de IA/relatorios_extracao/<SIGLA>_relatorio_extracao.md` | Relatório informativo da extração |

- Os relatórios ficam **todos** na subpasta `relatorios_extracao/`, para não misturá-los aos JSONs e aos notebooks.
- `<SIGLA>` é um identificador curto do plano, sem espaços, com o ano quando ajudar a distingui-lo (por exemplo, `PBIA_2024`, `EUA_2025`, `UE_2025`, `China_2017`). Se o pesquisador indicar um nome, usa-se o nome indicado.
- **Um único JSON por plano.** Não se criam versões paralelas (`_v2`, `_v3`, …).
- Se o JSON do plano **já existir**, o agente não o sobrescreve por conta própria: informa ao pesquisador e só substitui o JSON e o relatório **por comando dele**.
- Nenhum outro arquivo (resumos, gráficos, scripts, rascunhos) é deixado na pasta. Arquivos temporários ficam fora do repositório.

### 4.3. Estrutura do JSON (Entregável 1)

Codificação **UTF-8**, sem escapar caracteres especiais (`ensure_ascii=False`), indentação de 2 espaços.

```json
{
  "document": {
    "title": "Título oficial, exatamente como no documento",
    "subtitle": "Subtítulo oficial, exatamente como no documento, ou null",
    "issuer": "Governo, órgão ou instituição emissora, conforme o documento",
    "country_or_bloc": "País ou bloco a que o plano se refere, conforme o documento",
    "date": "Data de publicação ou de aprovação, conforme o documento, ou null",
    "period": "Período de vigência, conforme o documento, ou null",
    "language": "en",
    "source_file": "nome_do_arquivo_fonte.pdf",
    "source_sha256": "SHA-256 do arquivo-fonte, ou null se o arquivo não estiver na pasta",
    "pages": 0
  },
  "extraction": {
    "skill": "skill_extração",
    "corpus": "Planos Nacionais de IA",
    "skill_version": "1.0",
    "date": "AAAA-MM-DD",
    "units_extracted": 0,
    "headings_extracted": 0,
    "paragraphs_extracted": 0,
    "list_items_extracted": 0,
    "words_extracted": 0,
    "characters_extracted": 0
  },
  "sections": [
    {
      "id": 1,
      "type": "heading",
      "level": 1,
      "category": "Body",
      "path": [],
      "number": null,
      "page": 8,
      "text": "Título interno literal"
    },
    {
      "id": 2,
      "type": "paragraph",
      "level": null,
      "category": "Body",
      "path": ["Título interno literal"],
      "number": null,
      "page": 8,
      "text": "Texto integral e literal do parágrafo."
    }
  ]
}
```

**Regras do JSON:**
- `id`: inteiro sequencial a partir de 1, na ordem original do documento.
- `type`: `heading` (título interno), `paragraph` (parágrafo) ou `list_item` (item de lista).
- `level`: nível do título interno (1 = nível mais alto, como parte, eixo ou pilar), conforme a numeração e a tipografia do documento; `null` nas demais unidades.
- `category`: posição estrutural do trecho, e **não** classificação temática: `Foreword`, `Executive summary`, `Body`, `Box` ou `Annex`.
- `path`: lista dos títulos internos acima da unidade, do nível mais alto ao mais baixo, com o texto literal, incluindo os rótulos repetidos que não viraram unidades (seção 3.2); `[]` quando não houver. Serve apenas para localizar e agrupar as unidades.
- `number`: numeração ou marcador **puro**, exatamente como no original (`"1."`, `"(a)"`, `"II.3"`), sem renumerar. Rótulos com palavras (*Pillar I*, *Chapter 3*) fazem parte do título e ficam no `text`.
- `page`: página do **arquivo** em que a unidade começa (1 = primeira página do arquivo), e não a numeração impressa.
- `text`: nunca vazio, nunca truncado, nunca com reticências inseridas pelo agente.
- `words_extracted`: palavras separadas por espaço no `text` de todas as unidades.
- Os contadores do bloco `extraction` devem corresponder exatamente ao conteúdo de `sections`.

### 4.4. Relatório de extração (Entregável 2)

> ℹ️ **O relatório é apenas informativo.** Ele serve para que o pesquisador tenha noção do que foi feito na extração. **Não é insumo nem instrução para nenhum comando seguinte**: as skills 02 e 03, as reextrações e qualquer outro pedido não o consultam nem o levam em consideração. O que vale adiante é o JSON e, acima de tudo, os comandos do pesquisador.

O relatório é um **texto curto em Markdown**, em português, gravado em UTF-8 em `relatorios_extracao/`. Ele agrupa as informações por tipo, em vez de listar elemento por elemento, não transcreve o conteúdo excluído (basta identificá-lo por número, título ou página) e, em regra, cabe em uma ou duas páginas.

Estrutura:

```markdown
# Relatório de extração — <título do plano>

**Arquivo-fonte:** <nome> (<n> páginas) · **JSON:** `<SIGLA>_extracao.json` · **Data:** AAAA-MM-DD

## 1. Resumo
Um parágrafo: o que foi extraído, os totais (unidades por tipo e palavras)
e as páginas cobertas. Em reextração, dizer por qual comando e o que mudou.

## 2. O que foi incluído
Por parte do documento, com páginas. Ex.: título e subtítulo (metadados);
apresentação (p. 4–5, Foreword); capítulos 1 a 6 (p. 8–74, Body).

## 3. O que foi excluído e por quê
Por tipo de elemento, com páginas e quantidades. Ex.: capa e créditos (p. 1–3);
sumário (p. 6–7); 42 notas de rodapé; 8 tabelas; referências (p. 75–80);
rótulo "Recommended Policy Actions", mantido só no path (repetido em 24 seções).

## 4. Normalizações aplicadas
Tipo e número de ocorrências, com um ou dois exemplos.

## 5. Pontos que podem precisar de revisão
Somente o que o agente decidiu com dúvida e que pode alterar os resultados, as
tabelas com conteúdo central do plano e as limitações do arquivo-fonte
(texto em imagem, OCR falho, páginas ilegíveis). Se não houver: "Nenhum."
```

### 4.5. Verificação obrigatória antes da entrega

1. **Literalidade:** cada `text` do JSON, consideradas apenas as normalizações da seção 3.5, é encontrado no texto do documento-fonte.
2. **Conciliação:** toda parte do documento-fonte está no JSON ou foi excluída por um motivo descrito no relatório.
3. **Ausência de inflação e de resíduos:** o JSON não traz restos de elementos excluídos (marcadores de nota colados às palavras, cabeçalhos ou rodapés, números de página, linhas de "Source:", células de tabela), nem trechos ou rótulos repetidos além do que o próprio plano repete no seu texto.
4. **Ordem e hierarquia:** a sequência dos `id` reproduz a ordem do documento-fonte, e `level` e `path` reproduzem a hierarquia dos títulos internos.
5. **Consistência:** os contadores do bloco `extraction` batem com o conteúdo efetivo do JSON.
6. **Validade técnica:** o JSON abre sem erro em um leitor padrão.

Se qualquer verificação falhar, o agente corrige antes de entregar. Se não conseguir corrigir, **informa a falha** ao pesquisador em vez de entregar um resultado incorreto.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final e são obedecidos em última instância.
2. **Autonomia com critério:** no que o pesquisador não definiu, o agente decide o que entra e o que infla, com o critério da seção 3.2, de forma consistente em todo o documento.
3. **Fidelidade integral:** o texto de cada unidade é **100% fiel** ao original, sem distorções, generalizações, vieses, abreviações ou inflação de dados.
4. **Neutralidade:** nenhum trecho é mantido ou retirado por parecer mais ou menos relevante para Brasil, China ou para a governança da IA. O critério é **apenas** estrutural.
5. **Exclusividade das fontes:** só se usa o arquivo-fonte indicado pelo pesquisador. Nenhum dado, metadado ou contexto vem de fora sem pedido expresso dele.
6. **Não inventar dados:** nenhum valor, data, nome ou trecho é deduzido, estimado ou completado. Informação ausente fica `null`.
7. **Transparência sobre limitações:** problemas do arquivo-fonte são informados ao pesquisador e nunca contornados em silêncio.
8. **Um JSON por plano:** cada plano tem um único JSON e um único relatório. A substituição só ocorre por comando do pesquisador.
9. **Relatório informativo:** o relatório descreve a extração para o pesquisador e não orienta nenhum comando seguinte.
10. **Preservação do material existente:** arquivos-fonte nunca são alterados ou apagados.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma extração imprecisa, enviesada, incompleta ou inflada compromete todas as etapas seguintes e a validade dos resultados publicados. O padrão exigido é o máximo.
