---
name: skill_análise_individual
description: Etapa 02 do fluxo de análise das Declarações sobre IA (IC FAPESP 2026). Orienta a análise de UMA declaração por vez, em notebook Jupyter, a partir do JSON produzido pela skill 01. Produz visualizações e interpretações com metodologia explícita, escolhas registradas e fragilidades apontadas.
etapa: 02
versao: 1.0
data: 2026-10-01
---

# Skill de Análise Individual — Declarações IA (Etapa 02)

> **Aplicação obrigatória.** Toda análise de uma declaração **isolada** (não comparada) feita dentro da pasta `notebooks/A_IC FAPESP 2026/Declarações IA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook de análise individual, o agente deve ler esta skill e cumpri-la por inteiro. Esta skill **não** cobre análises conjuntas ou comparativas: essas são regidas pela skill 03 (`skill_análise_comparativa.md`).

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A pasta **Declarações IA** reúne documentos declaratórios sobre inteligência artificial (declarações conjuntas, comunicados de cúpulas, recomendações e compromissos internacionais). A análise desses textos serve para mapear o vocabulário, os enfoques e as ênfases de cada documento, como base para a comparação entre atores e para a identificação do posicionamento de Brasil e China.

As visualizações e interpretações produzidas aqui podem ser incorporadas a relatórios científicos. Por isso, **cada gráfico precisa ser metodologicamente defensável, reprodutível e acompanhado da explicação de como foi construído**.

### 1.2. Rigor acadêmico e transparência metodológica

- Cada comando pedido deve ser executado **exatamente** conforme as instruções desta skill e do pedido do pesquisador.
- **Toda** escolha metodológica (pré-processamento, listas de palavras, recortes, limiares, parâmetros, tipo de gráfico) precisa estar **visível no código** e **descrita em texto** no próprio notebook, logo após a visualização que ela afeta.
- O procedimento precisa ser **reprodutível**: o mesmo JSON, com os mesmos parâmetros, deve gerar os mesmos números e as mesmas figuras. Procedimentos aleatórios (como o bootstrap) usam semente fixa e registrada.
- Se as instruções forem ambíguas, contraditórias ou não cobertas por esta skill, o agente **para e pergunta** ao pesquisador. Não deve presumir.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/Declarações IA/`.
- **Insumos permitidos:** (a) o JSON da declaração produzido pela **skill 01** (`<SIGLA>_extracao.json`); (b) o codebook de categorias desta pasta (`codebook_declaracoes.json`); (c) as instruções do pesquisador.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - investigar outras páginas, pastas ou notebooks do repositório para buscar padrões de resposta, resultados anteriores ou modelos de análise;
  - se espelhar em outras resoluções, análises ou interpretações sobre o mesmo documento ou o mesmo caso, sejam do repositório, da internet ou do conhecimento prévio do modelo;
  - usar informações externas para completar, contextualizar ou interpretar o texto;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O JSON da skill 01 é **somente leitura**: o notebook nunca o modifica.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| 01 | Extração do conteúdo integral das declarações para JSON + relatório de retiradas (CSV) | `skill_extração.md` |
| **02** | **Análise individual de cada declaração, em notebook, com visualizações e interpretações** | **esta skill** |
| 03 | Análise comparativa entre declarações, com normalização relativa | `skill_análise_comparativa.md` |

A Etapa 02 parte **exclusivamente** do resultado da Etapa 01. Se o JSON da declaração não existir, o agente não faz a análise: informa ao pesquisador que a skill 01 precisa ser executada antes.

### 1.5. Autoridade do pesquisador

As **ordens e comandos do pesquisador são a decisão final** sobre o que analisar, como analisar e o que manter. O agente pode **propor** instrumentos (listas de termos, categorias, limiares) e **apontar** riscos metodológicos, mas não pode impor escolhas, alterar decisões do pesquisador por conta própria nem omitir uma ordem recebida. Quando uma ordem do pesquisador tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.

---

## 2. Objetivos

### 2.1. Objetivo principal

Analisar, em notebook Jupyter (`.ipynb`), o conteúdo extraído de **uma** declaração e produzir **visualizações gráficas e interpretações** que permitam conhecer os termos mais comuns, o enfoque dado pelo texto, as proporções entre temas e as ênfases do documento. A metodologia adotada, as escolhas feitas e as fragilidades identificadas devem ficar explícitas.

### 2.2. Objetivos específicos

1. **Verificar o insumo:** confirmar que o JSON vem da skill 01, está íntegro e corresponde à declaração pedida.
2. **Descrever o documento:** extensão, número de unidades (parágrafos/itens), tokens e vocabulário.
3. **Identificar os termos mais frequentes** (lemas), com frequência absoluta, frequência por 1.000 tokens e grau de dispersão ao longo do texto.
4. **Identificar expressões recorrentes** de duas palavras (bigramas).
5. **Mapear o enfoque temático** por meio de um codebook de categorias, com proporções, intervalos de confiança e teste de robustez.
6. **Localizar** onde, ao longo do documento, os termos e as categorias aparecem.
7. **Caracterizar a ênfase normativa** do texto por meio dos verbos modais (*shall*, *must*, *should*, *will*, *may*, etc.).
8. **Interpretar** cada visualização com base nos valores obtidos, apontando método, escolhas e fragilidades.
9. **Registrar** parâmetros, versões e saídas para garantir a reprodutibilidade.

---

## 3. Diretrizes para a análise

### 3.1. Insumo: o que entra e o que não entra

Do JSON da skill 01 são usados **apenas**:

| Campo | Uso |
|---|---|
| `document.title` | Identificação do documento nas tabelas, figuras e textos. Por padrão, **não** entra nas contagens. Incluí-lo é uma escolha do pesquisador e deve ser registrada |
| `sections[].text` | **Único conteúdo analisado**: o texto integral e literal de cada parágrafo ou item |
| `sections[].id` | Apenas como **índice de posição** da unidade no documento (para gráficos de distribuição), nunca como conteúdo |
| `extraction` | Apenas para **verificação** de integridade e de pendências de revisão |

**Todo conteúdo periférico fica fora da análise:** subtítulos internos (`subtitle`), numeração (`number`), categoria estrutural (`category`), página (`page`), signatários (`signatories`) e os demais metadados. Se o pesquisador quiser incluir algum desses campos, a inclusão deve ser pedida expressamente e registrada.

### 3.2. Análise integral do conteúdo

- A análise cobre **todo** o texto das unidades. É proibido amostrar, cortar, resumir ou analisar apenas parte do documento.
- Recortes do tipo "os *N* mais frequentes" servem **apenas à visualização**. A tabela completa, com todos os termos, deve ser **exportada** para verificação.
- Quando houver **empate no ponto de corte** de um recorte, o notebook deve informar quantos e quais termos empatados ficaram de fora e qual critério de desempate foi usado.
- É proibido abreviar, truncar ou parafrasear trechos citados do documento. Citações são literais.

### 3.3. Pré-processamento padrão

O pré-processamento é o mesmo para todas as declarações, para que os resultados sejam comparáveis na skill 03. Qualquer alteração deve ser feita nos parâmetros do notebook e registrada.

| Passo | Procedimento | Justificativa |
|---|---|---|
| 1 | Processamento de cada unidade com spaCy (modelo do idioma do documento; em inglês, `en_core_web_sm`) | Tokenização, lematização e classes gramaticais com ferramenta aberta e documentada |
| 2 | Reunião de palavras compostas com hífen (*multi-stakeholder*, *human-centric*) em um só token | Evita que o composto seja contado como palavras soltas, o que distorce frequências |
| 3 | **Token** = sequência de letras (com hífen interno ou sigla com pontos). Números, pontuação e símbolos não são tokens | Define com precisão o denominador das taxas |
| 4 | Lematização e conversão para minúsculas (ex.: *risks* → *risk*) | Agrupa flexões de uma mesma palavra |
| 5 | Correções explícitas de lematização, listadas no código (ex.: *datum* → *data*) | Corrige erros conhecidos do modelo sem intervenção oculta |
| 6 | **Tokens de conteúdo** = substantivos, nomes próprios, verbos, adjetivos e advérbios, fora da lista de *stopwords* do spaCy (verificada pelo lema) e com pelo menos 2 caracteres | Concentra a análise em palavras com carga semântica |

- Listas de *stopwords* adicionais ou de palavras a manter são **decisões do pesquisador**: ficam em listas editáveis no código, vazias por padrão.
- **Nunca** se removem palavras para "limpar" um resultado indesejado sem registro e justificativa.

### 3.4. Medidas adotadas

| Medida | Definição |
|---|---|
| Frequência absoluta | Número de ocorrências do lema no documento |
| Frequência por 1.000 tokens | (frequência ÷ total de tokens do documento) × 1.000. O denominador é o total de tokens (palavras), **incluindo** *stopwords* |
| Alcance | Número e percentual de unidades (parágrafos/itens) em que o lema aparece |
| Dispersão (DP normalizado) | Medida de Gries (2008), normalizada (Lijffijt & Gries, 2012): 0 = distribuição proporcional ao tamanho das unidades; 1 = concentração máxima. Distingue termos espalhados pelo texto de termos concentrados em poucos trechos |
| Bigramas | Pares de tokens de conteúdo **adjacentes no texto original**, na mesma frase, sem pontuação entre eles. Não se formam pares artificiais pela remoção de *stopwords* |
| Categorias temáticas | Ocorrências dos termos do codebook, por 1.000 tokens e em percentual do total de ocorrências do codebook |
| Intervalo de confiança | Bootstrap por reamostragem de **unidades** (parágrafos/itens), com semente fixa. A reamostragem por unidade respeita a dependência entre palavras do mesmo parágrafo |
| Modais | Verbos modais identificados pela etiqueta gramatical (`MD`), por 1.000 tokens |

Medidas que dependem fortemente da extensão do texto (como a razão tipo/token) **não** devem ser usadas como indicador de riqueza vocabular sem a devida ressalva.

### 3.5. Codebook de categorias temáticas

- O codebook é um **instrumento analítico do pesquisador**. Fica em arquivo único da pasta (`codebook_declaracoes.json`), compartilhado por todos os notebooks, para que todas as declarações sejam medidas com o mesmo instrumento.
- Uma versão proposta pelo agente deve vir marcada como **proposta**, até ser validada pelo pesquisador.
- As categorias são **mutuamente exclusivas**: um termo pertence a uma só categoria.
- O notebook deve sempre mostrar: (a) o codebook completo; (b) a **cobertura** (percentual dos tokens do documento captado pelo codebook); (c) os termos com **zero ocorrências**; (d) a contribuição de cada termo para sua categoria; (e) um **teste de robustez**: quanto a categoria depende do seu termo mais frequente.
- Alterar o codebook depois de ver os resultados é permitido apenas por decisão do pesquisador e deve ser registrado (nova versão do codebook).

### 3.6. Regras para as visualizações

1. **Um único eixo de valores por gráfico.** É vedado o uso de dois eixos verticais com escalas diferentes.
2. **Barras começam em zero.** Eixos não podem ser truncados para exagerar diferenças.
3. **Cores fixas por documento** em todos os notebooks (a mesma cor representa sempre a mesma declaração), com paleta segura para daltonismo.
4. **Legibilidade acadêmica:** fonte de no mínimo 9 pt, rótulos em português, separador decimal com vírgula, exportação em PNG (300 dpi) e PDF.
5. **Formas de leitura imprecisa** (nuvens de palavras, gráficos de pizza, gráficos 3D) **não** podem ser usadas como evidência principal.
6. Toda figura tem uma **tabela correspondente** com os valores exatos, exibida no notebook e exportada.
7. Ordens fixas (por exemplo, a ordem das categorias do codebook) são mantidas entre figuras e entre documentos.

### 3.7. Vieses proibidos

- Escolher termos, categorias, recortes ou parâmetros para **confirmar uma hipótese** da pesquisa.
- Destacar apenas os resultados convenientes ou omitir os inconvenientes.
- Ajustar limiares ou listas depois de ver os resultados sem registrar a alteração e o motivo.
- Atribuir intenções, motivações ou posições políticas aos autores do documento que não estejam no texto.
- Tratar frequência como importância política sem a devida mediação interpretativa.

---

## 4. Protocolo de operação e entregáveis

### 4.1. Procedimento passo a passo

1. **Ler esta skill por inteiro** antes de começar.
2. **Verificar o insumo:** o JSON da skill 01 existe nesta pasta? Foi produzido pela skill 01 (campo `extraction.skill`)? Há itens pendentes de revisão humana no CSV da skill 01? Se houver pendências, avisar o pesquisador.
3. **Configurar** os parâmetros na célula de configuração do notebook. Nenhum parâmetro pode ficar espalhado pelo código.
4. **Executar** o pré-processamento e exibir o perfil do documento.
5. **Gerar** cada visualização com sua tabela correspondente.
6. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
7. **Registrar** a execução (parâmetros, versões, *hash* dos insumos, lista de saídas).
8. **Informar** ao pesquisador, de forma breve, o que foi produzido e quais pontos exigem a atenção dele.

### 4.2. Estrutura obrigatória do notebook

1. **Apresentação:** do que se trata, finalidade, insumo usado (skill 01), recorte do conteúdo (apenas título e texto integral das unidades), método, transparência das escolhas e vínculo com esta skill.
2. **Configuração:** todos os parâmetros editáveis, comentados, em uma única célula.
3. **Ambiente e funções:** restrição de pasta, estilo das figuras e funções do pipeline, comentadas.
4. **Carregamento e verificação** do JSON.
5. **Pré-processamento** e **perfil** do documento.
6. **Análises e visualizações**, cada uma seguida do bloco de texto da seção 4.3.
7. **Registro de execução** e **síntese** final.

### 4.3. Bloco de texto após cada visualização

Logo após cada visualização, o notebook deve conter:

| Item | Conteúdo |
|---|---|
| **Método e escolhas** | O que foi medido, como, com quais parâmetros, e quais escolhas foram feitas (inclusive as do pesquisador) |
| **Como ler** | Instrução objetiva de leitura do gráfico |
| **Interpretação** | Texto breve que interpreta o gráfico **com base nos valores efetivamente obtidos** |
| **Fragilidades e ajustes possíveis** | Limitações do método ou dos dados e ajustes que poderiam ser considerados, **quando necessário** |

**Regras da interpretação:**
- É redigida **somente depois da execução**, a partir dos números exibidos. Antes da execução, o campo fica marcado como pendente. Nunca se escreve interpretação antecipada ou "esperada".
- Cita os valores que a sustentam (frequências, taxas, intervalos).
- Separa **observação** (o que os números mostram) de **inferência** (o que eles podem sugerir), e marca a inferência como tal.
- Não extrapola para além do documento analisado e não faz comparações com outros documentos (isso é tarefa da skill 03).

### 4.4. Entregáveis

| Entregável | Local |
|---|---|
| Notebook de análise | `Análise_<SIGLA>.ipynb`, nesta pasta |
| Figuras (PNG 300 dpi + PDF) | `resultados/<SIGLA>/<versão>/` |
| Tabelas completas (CSV, UTF-8 com BOM, `;`, vírgula decimal) | `resultados/<SIGLA>/<versão>/` |
| Registro de execução (`registro_execucao.json`) | `resultados/<SIGLA>/<versão>/` |

- **Não sobrescrever** resultados existentes. Uma nova execução com mudanças gera uma nova versão (`v2`, `v3`, …). O notebook deve interromper a execução se a pasta de saída já tiver arquivos e a substituição não tiver sido autorizada.
- Alterações pedidas em gráficos já existentes são **acrescentadas** como novas versões (novas células ao final do notebook e novos arquivos), sem apagar as anteriores, salvo ordem expressa do pesquisador.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Fidelidade ao insumo:** analisa-se apenas o texto integral e literal das unidades do JSON da skill 01, sem cortes, abreviações ou acréscimos.
2. **Transparência total:** todo método e toda escolha estão no código **e** na descrição em texto que acompanha a visualização.
3. **Reprodutibilidade:** parâmetros centralizados, semente fixa, versões registradas, *hash* dos insumos registrado.
4. **Neutralidade:** nenhum instrumento ou parâmetro é escolhido para produzir um resultado desejado.
5. **Não inventar dados:** nenhum valor é estimado, ajustado ou arredondado para "melhorar" um gráfico. Divergências inesperadas são explicadas, não corrigidas à força.
6. **Exclusividade das fontes:** só se usa o que está nesta pasta. Nada vem de outras páginas, pastas ou resoluções anteriores sem pedido expresso do pesquisador.
7. **Fragilidades declaradas:** limitações conhecidas (erros de lematização, ambiguidade de termos, documentos curtos, cobertura do codebook) são sempre declaradas.
8. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final.
9. **Escopo individual:** esta skill não compara documentos. Toda comparação segue a skill 03.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma visualização sem método explícito, com escolhas ocultas ou com interpretação não sustentada pelos dados compromete a validade dos resultados publicados. O padrão exigido é o máximo.

### Referências metodológicas

- GRIES, S. Th. Dispersions and adjusted frequencies in corpora. *International Journal of Corpus Linguistics*, v. 13, n. 4, p. 403-437, 2008.
- LIJFFIJT, J.; GRIES, S. Th. Correction to Stefan Th. Gries' "Dispersions and adjusted frequencies in corpora". *International Journal of Corpus Linguistics*, v. 17, n. 1, p. 147-149, 2012.
- EFRON, B.; TIBSHIRANI, R. J. *An Introduction to the Bootstrap*. New York: Chapman & Hall, 1993.
- KRIPPENDORFF, K. *Content Analysis: An Introduction to Its Methodology*. 4. ed. Thousand Oaks: SAGE, 2019.
