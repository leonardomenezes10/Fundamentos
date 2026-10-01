---
name: skill_extração
description: Etapa 01 do fluxo de análise das Declarações sobre IA (IC FAPESP 2026). Extrai o conteúdo integral e literal das declarações para JSON e registra em CSV tudo o que foi retirado, com o motivo, para verificação humana.
etapa: 01
versao: 1.0
data: 2026-10-01
---

# Skill de Extração — Declarações IA (Etapa 01)

> **Aplicação obrigatória.** Toda declaração a ser extraída dentro da pasta `notebooks/A_IC FAPESP 2026/Declarações IA/` **deve** passar por esta skill. Nenhuma extração pode ser feita fora deste protocolo, de forma parcial ou por atalho. Sempre que for pedido um comando de extração nesta pasta, o agente deve ler esta skill antes de começar e cumpri-la por inteiro.

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **Declarações IA** reúne documentos declaratórios sobre inteligência artificial, como declarações conjuntas, comunicados de cúpulas e compromissos internacionais. Nesses documentos, os Estados manifestam princípios, entendimentos comuns e intenções sobre o desenvolvimento, o uso e a governança da IA. A análise desses textos serve para mapear convergências e divergências entre os atores internacionais e identificar o posicionamento de Brasil e China.

Os dados produzidos aqui vão sustentar análises e visualizações que entram em relatórios científicos. Por isso, **qualquer erro de extração passa para todas as etapas seguintes** e compromete a validade dos resultados.

### 1.2. Rigor acadêmico e metodológico

O agente deve agir com o rigor de um procedimento científico documentado:

- Cada comando pedido deve ser executado **exatamente** conforme as instruções desta skill e do pedido do pesquisador, sem acrescentar etapas, atalhos ou interpretações próprias.
- Cada decisão tomada (manter, retirar ou normalizar um trecho) precisa ser **explícita, justificada e rastreável** no relatório CSV.
- O procedimento precisa ser **reprodutível**: outra pessoa que aplique esta skill ao mesmo documento deve chegar ao mesmo resultado.
- Se as instruções do pedido forem ambíguas, contraditórias ou não cobertas por esta skill, o agente **para e pergunta** ao pesquisador. Não deve presumir.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/Declarações IA/`.
- **Todos** os insumos, decisões e conteúdos usados devem vir **desta pasta**.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - usar informações de terceiros, conhecimento prévio do modelo ou fontes externas (internet, bases de dados, outras versões do documento) para completar, corrigir, datar ou interpretar o texto;
  - usar análises, resultados, códigos ou arquivos de **outras pastas** do repositório;
  - tomar como contexto qualquer outra página, documento ou conversa;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- Os **arquivos-fonte** (PDF, TXT, HTML, DOCX etc.) são **somente leitura**: nunca podem ser alterados, renomeados ou apagados.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| **01** | **Extração do conteúdo integral das declarações para JSON + relatório de retiradas (CSV)** | **esta skill** |
| 02 em diante | Análises textuais e construção de gráficos a partir do JSON da Etapa 01 | skills próprias de cada etapa |

A Etapa 01 **não faz análise**: não interpreta, não classifica tematicamente, não conta termos, não resume e não gera gráficos. A função dela é entregar uma base textual fiel, limpa e auditável para as etapas seguintes.

---

## 2. Objetivos

### 2.1. Objetivo principal

Extrair, da melhor forma possível, o **conteúdo integral e literal** das declarações pedidas e organizá-lo em **JSON estruturado**, pronto para análise e visualização nas etapas seguintes. Em paralelo, documentar em **CSV** tudo o que foi retirado e o motivo, para permitir verificação humana.

### 2.2. Objetivos específicos

1. **Identificar o documento-fonte** pedido dentro da pasta e confirmar que corresponde à declaração indicada pelo pesquisador.
2. **Delimitar o corpo da declaração**, separando o texto declaratório (o que de fato é a declaração) dos elementos pré-textuais, pós-textuais e acessórios.
3. **Extrair literalmente** o corpo da declaração, preservando texto, idioma, ordem, numeração e estrutura originais.
4. **Estruturar** o conteúdo em unidades (parágrafos ou itens numerados), cada uma com identificador, localização e posição na hierarquia do documento.
5. **Registrar em CSV** cada elemento retirado ou normalizado, com o conteúdo exato, a localização, o critério aplicado, a justificativa e a indicação de revisão humana.
6. **Verificar a integridade** da extração: todo trecho do documento-fonte deve estar no JSON **ou** no CSV. Nenhuma omissão pode ficar sem registro.

---

## 3. Diretrizes para a análise

### 3.1. Princípio geral: fidelidade integral

O texto extraído deve ser **idêntico ao original**. Fica **PROIBIDO**:

| Proibido | Exemplo do que não pode acontecer |
|---|---|
| **Distorção** | Alterar palavras, sentido, tempo verbal, ênfase ou pontuação significativa |
| **Generalização** | Substituir um trecho específico por uma formulação genérica ("os países se comprometem com a IA segura") |
| **Viés** | Escolher, destacar ou omitir trechos por relevância presumida para Brasil, China ou qualquer hipótese da pesquisa |
| **Abreviação** | Resumir, cortar com reticências ("[...]", "..."), condensar parágrafos ou truncar textos longos |
| **Inflação de dados** | Duplicar trechos, repetir títulos ou cabeçalhos de página, incluir o mesmo parágrafo duas vezes por erro de leitura do layout, misturar elementos acessórios ao corpo |
| **Tradução** | Traduzir o texto. O idioma original é mantido |
| **Correção** | Corrigir ortografia, gramática ou estilo do original, ou acrescentar "[sic]" |
| **Paráfrase ou reordenação** | Reescrever, fundir ou reordenar parágrafos, itens ou seções |
| **Expansão** | Expandir siglas, completar frases ou acrescentar explicações. Siglas ficam exatamente como aparecem no original |

Distorções, abreviações e inflações alteram contagens de palavras, frequências e proporções, e com isso **prejudicam diretamente as visualizações** das etapas seguintes.

### 3.2. O que COMPÕE a declaração (deve ser mantido no JSON)

- **Título oficial** da declaração, registrado nos metadados e não repetido dentro do texto das seções.
- **Preâmbulo**: parágrafos introdutórios do próprio texto declaratório (por exemplo, *"Recognizing…"*, *"Affirming…"*, *"Nós, os Chefes de Estado…"*). O preâmbulo **faz parte da declaração** e não deve ser confundido com elementos pré-textuais.
- **Corpo dispositivo**: princípios, compromissos, entendimentos, recomendações, ações e parágrafos numerados ou não.
- **Títulos e subtítulos internos** da declaração, registrados no campo `subtitle` da seção correspondente e não misturados ao `text`.
- **Anexos que integram formalmente a declaração**, ou seja, quando o próprio texto os declara parte integrante (por exemplo, "Anexo I – Princípios"). Devem ser sinalizados no CSV com `acao = Mantido com ressalva` para confirmação humana.

### 3.3. O que NÃO COMPÕE a parte essencial de análise (deve ser retirado e registrado no CSV)

#### 3.3.1. Elementos pré-textuais
- Capas, folhas de rosto, logotipos e textos de identidade visual.
- Sumários, índices, listas de siglas, listas de figuras e tabelas.
- Informações prévias e descrições sobre o documento: notas editoriais, "sobre este documento", apresentações institucionais, prefácios ou mensagens de terceiros que não fazem parte do texto declaratório, avisos de direitos autorais, ISBN, ficha catalográfica, créditos de edição.

#### 3.3.2. Elementos pós-textuais
- Referências bibliográficas e bibliografias.
- Glossários, apêndices e anexos que **não** são parte integrante da declaração (material de apoio, relatórios técnicos, documentos de referência).
- Informações de contato, créditos finais, agradecimentos e expedientes.

#### 3.3.3. Elementos acessórios inseridos no texto
- **Notas de rodapé e notas de fim**: o texto da nota e o **marcador** dela no corpo (números ou símbolos sobrescritos).
- **Links e URLs**: endereços eletrônicos, hiperlinks e referências do tipo "disponível em: …". Retira-se apenas o endereço, sem alterar o restante da frase. Se a retirada deixar a frase sem sentido, **não retirar**: manter e sinalizar para revisão.
- **Artefatos de diagramação**: cabeçalhos e rodapés de página repetidos, numeração de página, marcas d'água, legendas de imagens decorativas.

#### 3.3.4. Lista de signatários
A lista de países ou autoridades signatárias **não entra no texto das seções**, para não inflar as contagens. Ela é transcrita **literalmente** no campo `document.signatories` dos metadados, porque é informação relevante para a pesquisa (posicionamento de Brasil e China), e registrada no CSV com `acao = Realocado para metadados`.

### 3.4. Normalizações técnicas permitidas

Apenas as normalizações abaixo são permitidas. **Todas** devem ser registradas no CSV, uma linha por tipo de ocorrência e por página, com exemplos literais:

1. **Reunião de palavras hifenizadas por quebra de linha** do PDF (por exemplo, `govern-` + `ance` → `governance`), somente quando a hifenização for claramente um artefato de diagramação e não um hífen original da palavra.
2. **Remoção de quebras de linha internas** ao parágrafo, causadas pela diagramação.
3. **Redução de espaços em branco múltiplos** a um único espaço.
4. **Correção de caracteres corrompidos pela extração** (por exemplo, ligaduras `ﬁ` → `fi`), sem nenhuma outra alteração.

Qualquer outra intervenção no texto é **proibida**.

### 3.5. Regra para casos de dúvida

Se não houver certeza de que um elemento compõe ou não a declaração:

- **MANTER** o elemento no JSON (preservar o conteúdo original é a opção conservadora);
- **REGISTRAR** no CSV com `acao = Mantido com ressalva`, `revisao_humana = Sim` e a justificativa da dúvida;
- a decisão final cabe ao pesquisador.

---

## 4. Protocolo de operação e entregáveis

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar os insumos:** confirmar que o arquivo-fonte pedido existe **dentro desta pasta**. Se não existir, estiver ilegível, incompleto ou houver mais de uma versão possível (idiomas ou edições diferentes), **parar e perguntar** ao pesquisador.
3. **Ler o documento-fonte integralmente**, do início ao fim, antes de decidir qualquer retirada.
4. **Delimitar** onde começa e onde termina o corpo da declaração, aplicando as seções 3.2 e 3.3.
5. **Segmentar** o corpo em unidades: um registro por parágrafo ou por item numerado, na ordem original.
6. **Extrair** cada unidade literalmente, aplicando apenas as normalizações da seção 3.4.
7. **Preencher os metadados** do documento **somente com informações que constam no próprio documento-fonte**. Campo sem informação no documento → `null`. Nunca inferir, deduzir ou buscar fora.
8. **Registrar no CSV** cada retirada, normalização, realocação e manutenção com ressalva.
9. **Verificar** a extração conforme a seção 4.5.
10. **Gravar** os dois entregáveis nesta pasta e informar ao pesquisador, de forma breve, os totais e os pontos marcados para revisão humana.

### 4.2. Entregáveis

São entregues **APENAS** dois arquivos, ambos gravados em `notebooks/A_IC FAPESP 2026/Declarações IA/`:

| Entregável | Nome do arquivo | Conteúdo |
|---|---|---|
| 1 | `<SIGLA>_extracao.json` | Conteúdo integral e literal da declaração |
| 2 | `<SIGLA>_relatorio_extracao.csv` | Registro de tudo o que foi retirado, normalizado, realocado ou mantido com ressalva |

- `<SIGLA>` é um identificador curto da declaração, sem espaços (por exemplo, `Bletchley_2023`). Se o pesquisador indicar um nome, usa-se o nome indicado.
- **Não sobrescrever** arquivos existentes. Se já existir um arquivo com o mesmo nome, gravar uma nova versão com sufixo (`_v2`, `_v3`, …) e avisar o pesquisador.
- Nenhum outro arquivo (resumos, gráficos, scripts, rascunhos) deve ser deixado na pasta. Arquivos temporários usados durante o trabalho devem ficar fora do repositório.

### 4.3. Estrutura do JSON (Entregável 1)

Codificação **UTF-8**, sem escapar caracteres acentuados (`ensure_ascii=False`), indentação de 2 espaços.

```json
{
  "document": {
    "title": "Título oficial, exatamente como no documento",
    "source_file": "nome_do_arquivo_fonte.pdf",
    "issuer": "Órgão, cúpula ou conjunto de Estados emissor, conforme o documento",
    "event": "Cúpula ou reunião em que foi adotada, conforme o documento, ou null",
    "place": "Local, conforme o documento, ou null",
    "date": "Data, conforme o documento, ou null",
    "language": "Código do idioma do texto extraído (ex.: en, pt, zh)",
    "pages": 0,
    "signatories": ["Lista literal de signatários, na ordem do documento, ou null"]
  },
  "extraction": {
    "skill": "skill_extração",
    "skill_version": "1.0",
    "date": "AAAA-MM-DD",
    "units_extracted": 0,
    "words_extracted": 0,
    "characters_extracted": 0,
    "items_removed_or_normalized": 0,
    "items_flagged_for_review": 0,
    "report_file": "<SIGLA>_relatorio_extracao.csv"
  },
  "sections": [
    {
      "id": 1,
      "category": "Preamble",
      "subtitle": "Subtítulo interno original, ou null",
      "number": "Numeração original do parágrafo/item, ou null",
      "page": 1,
      "text": "Texto integral e literal do parágrafo ou item."
    }
  ]
}
```

**Regras do JSON:**
- `id`: inteiro sequencial a partir de 1, na ordem original do documento.
- `category`: posição estrutural do trecho, e **não** classificação temática. Valores: `Preamble`, `Body`, `Annex`. Classificações temáticas são feitas nas etapas seguintes.
- `number`: numeração **exatamente** como no original (`"1"`, `"(a)"`, `"II.3"`), sem renumerar.
- `text`: nunca vazio, nunca truncado, nunca com reticências inseridas pelo agente.
- Os contadores do bloco `extraction` devem corresponder exatamente ao conteúdo de `sections` e às linhas do CSV.

### 4.4. Estrutura do relatório CSV (Entregável 2)

Codificação **UTF-8 com BOM** (`utf-8-sig`), delimitador **ponto e vírgula (`;`)**, todos os campos de texto entre aspas duplas, para abrir corretamente no Excel em português. Uma linha por elemento.

| Coluna | Descrição |
|---|---|
| `id_registro` | Identificador sequencial da linha (R001, R002, …) |
| `arquivo_fonte` | Nome do arquivo-fonte |
| `pagina` | Página (ou intervalo) em que o elemento aparece |
| `localizacao` | Posição no documento (ex.: "antes do preâmbulo", "após §12", "rodapé da p. 4") |
| `tipo_elemento` | Capa, Sumário, Descrição do documento, Nota de rodapé, Marcador de nota, Link/URL, Referência bibliográfica, Cabeçalho/rodapé de página, Numeração de página, Lista de signatários, Anexo, Hifenização, Quebra de linha, Caractere corrompido, Outro (especificar) |
| `conteudo_original` | Conteúdo **literal e completo** do elemento retirado ou alterado. Para normalizações repetitivas, exemplos literais e o número de ocorrências |
| `acao` | `Removido`, `Normalizado`, `Realocado para metadados` ou `Mantido com ressalva` |
| `criterio_aplicado` | Seção desta skill que fundamenta a decisão (ex.: "3.3.3 – notas de rodapé") |
| `justificativa` | Explicação clara e específica do motivo, sem fórmulas genéricas |
| `confianca` | Grau de certeza do agente na decisão: `Alta`, `Média` ou `Baixa` |
| `revisao_humana` | `Sim` ou `Não`. Obrigatoriamente `Sim` quando `confianca` for `Média` ou `Baixa` e quando `acao` for `Mantido com ressalva` |
| `decisao_pesquisador` | **Deixar em branco**: preenchido pelo pesquisador (Manter / Retirar / Corrigir) |
| `comentario_pesquisador` | **Deixar em branco**: preenchido pelo pesquisador |

O CSV existe para **favorecer a verificação humana**. Por meio dele, o pesquisador julga o que deve ou não ser mantido e avalia se a extração foi eficiente. Por isso, nenhuma retirada pode aparecer só de forma agregada ou vaga ("várias notas removidas"). Cada elemento substantivo retirado tem sua própria linha com o conteúdo literal.

### 4.5. Verificação obrigatória antes da entrega

1. **Literalidade:** cada `text` do JSON, considerando apenas as normalizações da seção 3.4, deve ser encontrado no texto do documento-fonte.
2. **Conciliação (nenhuma omissão silenciosa):** todo trecho do documento-fonte deve estar no JSON **ou** registrado no CSV.
3. **Ausência de duplicação:** nenhum trecho pode aparecer duas vezes no JSON, a menos que esteja repetido no próprio original. Nesse caso, registrar no CSV como `Mantido com ressalva`.
4. **Ordem:** a sequência dos `id` reproduz a ordem do documento-fonte.
5. **Consistência:** os contadores do bloco `extraction` batem com o conteúdo efetivo dos arquivos.
6. **Validade técnica:** o JSON abre sem erro em um leitor padrão e o CSV abre com as colunas corretas.

Se qualquer verificação falhar, o agente corrige antes de entregar. Se não conseguir corrigir, **informa a falha** ao pesquisador em vez de entregar um resultado incorreto.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Fidelidade integral:** o texto extraído é a base de todas as análises. Ele deve ser **100% fiel** ao original, sem distorções, generalizações, vieses, abreviações ou inflação de dados.
2. **Neutralidade:** a extração é indiferente às hipóteses da pesquisa. Nenhum trecho é mantido ou retirado por parecer mais ou menos relevante para Brasil, China ou para a governança da IA. O critério é **apenas** estrutural (seções 3.2 e 3.3).
3. **Exclusividade das fontes:** só se usa o que está nesta pasta. Nenhum dado, metadado ou contexto pode vir de fora sem pedido expresso do pesquisador.
4. **Não inventar dados:** nenhum valor, data, nome, signatário ou trecho pode ser deduzido, estimado ou completado. Informação ausente fica `null` e, se relevante, é sinalizada no CSV.
5. **Rastreabilidade total:** toda decisão que afaste o JSON do texto bruto do documento-fonte está registrada no CSV com critério e justificativa.
6. **Transparência sobre limitações:** problemas do arquivo-fonte (páginas ilegíveis, OCR falho, texto em imagem, trechos cortados) devem ser **informados explicitamente** ao pesquisador e registrados no CSV, e nunca contornados em silêncio.
7. **Primazia da verificação humana:** o agente propõe e o pesquisador decide. Os campos `decisao_pesquisador` e `comentario_pesquisador` existem para isso e nunca são preenchidos pelo agente.
8. **Preservação do material existente:** arquivos-fonte e entregáveis anteriores nunca são alterados ou apagados. Novas extrações geram novas versões.
9. **Cumprimento estrito do pedido:** o agente faz o que foi pedido, conforme esta skill. Na dúvida, pergunta.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma extração imprecisa, enviesada, incompleta ou inflada compromete todas as etapas seguintes e a validade dos resultados publicados. O padrão exigido é o máximo.
