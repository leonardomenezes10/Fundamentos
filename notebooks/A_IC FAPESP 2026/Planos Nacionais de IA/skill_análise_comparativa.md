---
name: skill_análise_comparativa
description: Etapa 03 do fluxo de análise dos Planos Nacionais de IA (IC FAPESP 2026). Orienta a análise CONJUNTA e comparativa de dois ou mais planos (PBIA, Winning the Race, UE, China etc.), em notebook Jupyter, a partir dos JSONs produzidos pela skill 01, com comparação relativa (ocorrências por 1.000 tokens) e metodologia explícita.
etapa: 03
versao: 1.0
data: 2026-10-04
---

# Skill de Análise Comparativa — Planos Nacionais de IA (Etapa 03)

> **Aplicação obrigatória.** Toda análise **conjunta ou comparativa** entre planos feita na pasta `notebooks/A_IC FAPESP 2026/Planos Nacionais de IA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook comparativo, o agente lê esta skill e a cumpre por inteiro. Esta skill **amplia** a skill 02 (`skill_análise_individual.md`): todas as regras da skill 02 valem aqui, com os acréscimos e as mudanças descritos abaixo.

> ⚠️ **OS COMANDOS DO PESQUISADOR SÃO OBEDECIDOS EM ÚLTIMA INSTÂNCIA.** Eles prevalecem sobre qualquer regra desta skill. Visualizações, relatórios e outras saídas **só vão para a pasta `resultados/` por comando do pesquisador** (seção 4.4).

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A comparação entre os planos nacionais de IA, como o **PBIA**, o plano dos Estados Unidos (*Winning the Race*), o da União Europeia e o da China, permite identificar **semelhanças, distinções, enfoques e ênfases** de vocabulário, de prioridades e de concepções de governança. Com isso, a política brasileira pode ser situada em relação às demais, em especial à chinesa.

Todos os planos estão **em inglês**, e a comparação é feita nesse idioma.

Os resultados comparativos podem ser incorporados a relatórios científicos. Uma comparação mal construída, por exemplo entre valores absolutos de documentos de tamanhos diferentes, produz **conclusões falsas**. Por isso, esta skill exige comparação **relativa** e procedimento **idêntico** para todos os planos.

### 1.2. Rigor acadêmico e transparência metodológica

Valem integralmente as regras da skill 02 (seção 1.2):
- cada comando pedido é executado conforme esta skill e o pedido do pesquisador;
- toda escolha metodológica está visível no código **e** descrita em texto logo após a visualização que ela afeta;
- o procedimento é reprodutível, com semente fixa e parâmetros registrados;
- se o **comando** do pesquisador for ambíguo, o agente para e pergunta.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/Planos Nacionais de IA/`.
- **Insumos permitidos:** (a) os JSONs dos planos produzidos pela **skill 01** (`<SIGLA>_extracao.json`, um único por plano); (b) as instruções do pesquisador.
- Os **relatórios de extração** (`relatorios_extracao/`) **não são insumo** desta etapa: são apenas informativos para o pesquisador e não são consultados nem levados em consideração.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - investigar outras páginas, pastas ou notebooks do repositório para buscar padrões de resposta, resultados anteriores ou modelos de análise;
  - se espelhar em outras resoluções, análises ou interpretações sobre os mesmos planos;
  - usar informações externas para contextualizar ou interpretar as diferenças encontradas;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O notebook comparativo **reprocessa** os JSONs da skill 01 com o mesmo pipeline. Ele **não** usa números copiados dos notebooks individuais. Assim, todos os planos são tratados no mesmo processamento e com os mesmos parâmetros.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| 01 | Extração do texto essencial de cada plano para JSON + relatório informativo | `skill_extração.md` |
| 02 | Análise individual de cada plano | `skill_análise_individual.md` |
| **03** | **Análise conjunta e comparativa dos planos, com normalização relativa** | **esta skill** |

### 1.5. Autoridade do pesquisador e autonomia do agente

- As **ordens e comandos do pesquisador são a decisão final e são obedecidos em última instância**: quais planos comparar, em que ordem, com quais recortes e limiares. O agente pode propor instrumentos e apontar riscos, mas não impõe escolhas. Quando uma ordem tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.
- Dentro do que o pesquisador não definiu, o agente tem **autonomia** para reconhecer o que infla ou desequilibra a comparação e para tratá-lo, conforme a seção 3.6, sempre de forma visível no código e explicada no texto.

---

## 2. Objetivos

### 2.1. Objetivo principal

Comparar, em notebook Jupyter (`.ipynb`), o conteúdo extraído de dois ou mais planos e produzir **visualizações gráficas e interpretações comparativas**. A comparação é feita sempre em **termos relativos (ocorrências por 1.000 tokens)**, e não absolutos, para permitir verificar semelhanças, distinções, diferentes enfoques, diferentes ênfases, termos mais comuns e termos mais distintivos de cada plano.

### 2.2. Objetivos específicos

1. **Verificar os insumos:** confirmar que todos os JSONs vêm da skill 01 e estão íntegros.
2. **Expor a disparidade de tamanho** entre os planos, que justifica a normalização relativa.
3. **Comparar os termos mais frequentes** de cada plano, em ocorrências por 1.000 tokens.
4. **Identificar semelhanças:** termos com peso relativo parecido nos planos.
5. **Identificar distinções:** termos significativamente mais característicos de um plano do que de outro (análise de *keyness*).
6. **Comparar o vocabulário** compartilhado e exclusivo, com as ressalvas de tamanho.
7. **Comparar os enfoques temáticos**, quando o pesquisador definir as categorias, com intervalos de confiança para cada plano e para a diferença entre eles.
8. **Comparar a ênfase normativa** (verbos modais), quando pedido.
9. **Interpretar** cada visualização com base nos valores obtidos, apontando método, escolhas e fragilidades.
10. **Registrar** parâmetros, versões e saídas para garantir a reprodutibilidade.

---

## 3. Diretrizes para a análise

### 3.1. Insumo: o que entra e o que não entra

Igual à skill 02 (seção 3.1). De cada JSON são usados o título e o subtítulo (identificação e, por padrão, contagem), o texto integral e literal de cada unidade (`sections[].text`) e, apenas como filtros, índice de posição ou agrupador, os campos `type`, `category`, `id` e `path`. **Os mesmos filtros valem para todos os planos.**

### 3.2. Identidade de procedimento

- **Mesmo pipeline e mesmos parâmetros** para todos os planos comparados. O pré-processamento é o da skill 02 (seção 3.3).
- **Mesmo idioma:** todos os JSONs devem estar em inglês (`document.language = "en"`). O carregamento confere isso e interrompe a execução se algum divergir.
- **Simetria.** Nenhum plano é tratado como referência privilegiada, **inclusive o PBIA**: a posição central do PBIA está na pergunta de pesquisa, e não no procedimento. A convenção de sentido das medidas (por exemplo, valores positivos = mais característico do plano A) é declarada e mantida em todas as figuras.
- **Ordem e cores fixas.** Os planos aparecem sempre na ordem definida em `DOCUMENTOS` e com as cores de `COR_DOCUMENTO`, as mesmas dos notebooks individuais.

### 3.3. Comparação relativa: ocorrências por 1.000 tokens

Os planos têm **tamanhos diferentes**. Comparar frequências absolutas favoreceria o plano mais longo e produziria distorções. Por isso, **toda comparação entre planos é feita em ocorrências por 1.000 tokens**:

> **taxa por 1.000 tokens = (ocorrências do termo no plano ÷ total de tokens do plano) × 1.000**

- **Token** é definido como na skill 02: palavra (sequência de letras, com hífen interno ou sigla com pontos), sem números e pontuação.
- **O denominador é o total de tokens do plano, incluindo *stopwords*.** É a mesma base para todos os termos e para todas as categorias.
- Com essa normalização, os termos ficam em **pé de igualdade**: uma taxa de 5 por 1.000 tem o mesmo significado em um plano de 5.000 tokens e em um de 50.000.
- Valores **absolutos** aparecem apenas na tabela de perfil, para **expor a disparidade de tamanho**, e como informação auxiliar nas tabelas. Eles **nunca** são usados para afirmar que um plano enfatiza algo mais do que outro.

### 3.4. Comparação entre mais de dois planos

- As medidas descritivas (taxas por 1.000 tokens, termos mais comuns, vocabulário) são apresentadas para **todos os planos lado a lado**.
- Os gráficos de dois eixos (dispersão de semelhanças, convergência e divergência) comparam **dois planos por vez**. Com mais planos, faz-se um gráfico por par pedido pelo pesquisador ou um painel com os pares.
- A *keyness* segue um de dois modos, definido na configuração **antes** de ver os resultados (`MODO_KEYNESS`):
  - `"pares"` (padrão): cada par de planos é comparado diretamente;
  - `"um_contra_os_demais"`: cada plano é comparado ao conjunto formado pela soma dos demais. Nesse modo, os planos mais longos pesam mais na referência, e isso é declarado nas fragilidades.
- A escolha do modo é do pesquisador. O agente pode propor e justificar uma opção.
- A correção para comparações múltiplas (Bonferroni) considera o total de testes de todas as comparações feitas.

### 3.5. Critérios para afirmar uma diferença

| Comparação | Critério |
|---|---|
| Termo a termo (*keyness*) | Frequência combinada mínima `FREQ_MINIMA_COMPARACAO = 5`; **G²** de log-verossimilhança (Dunning, 1993; Rayson & Garside, 2000) ≥ `LIMIAR_G2 = 6,63` (p < 0,01; 1 grau de liberdade) **e** \|*Log Ratio*\| (Hardie, 2014) ≥ `LIMIAR_LOG_RATIO = 1` (ao menos o dobro da frequência relativa). Os dois critérios são exigidos juntos |
| Comparações múltiplas | Informa-se quantos termos distintivos resistem à correção de Bonferroni (`ALFA_BONFERRONI = 0,01`) |
| Frequência zero | Correção de 0,5 apenas no cálculo do *Log Ratio*; o termo é marcado como *exclusivo* |
| Categorias temáticas | Diferença afirmada apenas quando o intervalo de confiança da diferença (bootstrap por unidades, semente fixa) **não inclui zero** |
| Zonas descritivas | Zonas de convergência e divergência por razão entre taxas (`RAZAO_ZONA_NEUTRA = 2`) são **descritivas** e não são teste de significância. A tabela informa quais termos passam nos critérios de *keyness* |

Os limiares são parâmetros editáveis e são fixados **antes** da interpretação.

### 3.6. Autonomia na comparação: o que infla e o que desequilibra

Vale a seção 3.5 da skill 02 (**inflação é artefato; frequência real é resultado**), com um cuidado a mais: na comparação, o problema não é só a inflação de um plano, mas a **assimetria** entre os planos.

- O agente verifica se os planos receberam **tratamento equivalente**. Se um rótulo repetido, um bloco duplicado ou outro artefato foi tratado em um plano, artefatos do mesmo tipo são tratados da mesma forma nos demais.
- O agente avalia se diferenças de **estrutura** entre os planos distorcem a comparação (por exemplo, um plano com sumário executivo ou apresentação extensa e outro sem). Quando distorcerem, ele aplica os filtros da seção 3.1 de forma simétrica, explica a escolha e mostra o efeito, ou leva a questão ao pesquisador quando a escolha mudar o objeto da comparação.
- Toda decisão desse tipo fica na configuração, é explicada no texto e pode ser revertida pelo pesquisador.

### 3.7. Regras para as visualizações

Valem todas as regras da skill 02 (seção 3.7), com os acréscimos:
1. **Toda visualização comparativa usa taxas por 1.000 tokens** (ou medidas derivadas delas), nunca contagens absolutas.
2. Os planos aparecem sempre na **mesma ordem** e com as **mesmas cores**, e cada um é identificado também por rótulo direto ou marcador.
3. O sentido de toda medida assimétrica (*Log Ratio*, eixos X e Y) é escrito no próprio gráfico.
4. Com muitos planos, prefere-se gráficos de pontos com um marcador por plano ou painéis pequenos lado a lado a gráficos sobrecarregados.

### 3.8. Vieses proibidos

Valem todos os da skill 02 (seção 3.6), e mais:
- comparar valores absolutos de planos de tamanhos diferentes como se fossem comparáveis;
- afirmar que um plano "enfatiza mais" um tema com base em diferenças que não passaram pelos critérios da seção 3.5;
- escolher o plano de referência, o modo de *keyness* ou o sentido da comparação para favorecer uma leitura;
- tratar o PBIA, ou qualquer outro plano, com procedimento diferente dos demais;
- atribuir as diferenças a posições políticas dos governos sem considerar o gênero, a extensão, a função e a data de cada plano.

---

## 4. Protocolo de operação

### 4.1. Procedimento passo a passo

1. **Ler esta skill e a skill 02** por inteiro antes de começar.
2. **Configurar** os parâmetros na célula de configuração (planos, pré-processamento, modo de *keyness*, limiares comparativos).
3. **Processar** todos os planos com o mesmo pipeline.
4. **Verificar** a equivalência de tratamento entre os planos (seção 3.6).
5. **Expor o perfil comparativo** e a disparidade de tamanho.
6. **Gerar** cada visualização comparativa com a sua tabela correspondente.
7. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
8. **Registrar** a execução (parâmetros, versões, *hash* de todos os insumos, lista de saídas).
9. **Informar** ao pesquisador, de forma breve, o que foi produzido, os tratamentos aplicados e os pontos que exigem a atenção dele.

### 4.2. Estrutura obrigatória do notebook

Nome do arquivo: `Análise_Comparativa_<SIGLA_1>_<SIGLA_2>[_<SIGLA_n>].ipynb`, gravado nesta pasta, com as siglas na ordem de `DOCUMENTOS`.

1. **Apresentação** (primeira célula, em Markdown): título, projeto, etapa, insumos e o aviso de que as visualizações são prévias e de que nada vai para `resultados/` sem comando do pesquisador. Em seguida: **1. Do que se trata**; **2. Finalidade**; **3. Insumos e recorte do conteúdo**; **4. Por que a comparação é relativa**; **5. Método** (visão geral, em tabela); **6. Transparência das escolhas**; **7. Princípios** (vínculo com esta skill e simetria entre os planos).
2. **Configuração:** todos os parâmetros editáveis em uma única célula: `DOCUMENTOS` (sigla → JSON, na ordem das figuras), os mesmos parâmetros de pré-processamento e de recorte dos notebooks individuais e os parâmetros comparativos (`MODO_KEYNESS`, `TOP_N_COMPARACAO`, `FREQ_MINIMA_COMPARACAO`, `LIMIAR_G2`, `LIMIAR_LOG_RATIO`, `TOP_N_KEYNESS`, `ALFA_BONFERRONI`, `N_ROTULOS_DISPERSAO`, `N_BOOTSTRAP`, `NIVEL_CONFIANCA`, `SEMENTE`), com `SALVAR_SAIDAS = False`.
3. **Ambiente, estilo e funções:** restrição de pasta, estilo, funções do pipeline (**idênticas** às da skill 02) e funções comparativas.
4. **Carregamento e verificação** de todos os JSONs, com as verificações da skill 02 e a conferência do idioma.
5. **Pré-processamento** e **perfil comparativo**, com a disparidade de tamanho e os filtros aplicados a cada plano.
6. **Análises e visualizações comparativas**, cada uma seguida do bloco de texto da seção 4.3. Conjunto-padrão: termos mais comuns, lado a lado; semelhanças (termos compartilhados); distinções (*keyness*); vocabulário compartilhado e exclusivo. Outras análises (por exemplo, convergência e divergência de unigramas e bigramas, enfoques temáticos, modais) entram **por comando do pesquisador**.
7. **Registro de execução** e **síntese** final.

### 4.3. Bloco de texto após cada visualização

Igual à skill 02 (seção 4.3): **Método e escolhas**, **Como ler**, **Interpretação** (redigida só depois da execução, a partir dos valores obtidos, separando observação de inferência) e **Fragilidades e ajustes possíveis** (quando necessário). Na interpretação comparativa, toda afirmação de diferença indica o critério da seção 3.5 que a sustenta.

### 4.4. Pasta `resultados`

- Visualizações, tabelas, relatórios e quaisquer outras saídas **só vão para a pasta `resultados/` quando o pesquisador der o comando**, e da forma que ele exigir.
- **Nenhuma** visualização é adicionada automaticamente a `resultados/`. Sem o comando, o notebook apenas exibe as visualizações e as tabelas, sem gravá-las (`SALVAR_SAIDAS = False`).
- Quando houver gravação, as saídas vão para `resultados/Comparativa_<SIGLAS>/<VERSAO_SAIDA>/`. Resultados anteriores nunca são sobrescritos.
- Versões interativas (site) só são feitas por comando do pesquisador, com os mesmos dados do notebook, e o link é registrado no próprio notebook.

---

## 5. Regras de qualidade e rigor acadêmico

1. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final e são obedecidos em última instância.
2. **Comparação relativa obrigatória:** nenhuma conclusão comparativa se apoia em valores absolutos.
3. **Identidade de procedimento:** mesmo pipeline, mesmos parâmetros e mesmos filtros para todos os planos.
4. **Significância com tamanho de efeito:** diferenças termo a termo só são afirmadas quando passam pelos dois critérios. Diferenças entre categorias só são afirmadas quando o intervalo de confiança da diferença não inclui zero.
5. **Autonomia com simetria:** o agente trata o que infla ou desequilibra a comparação, sempre da mesma forma em todos os planos e de modo visível.
6. **Fidelidade ao insumo:** analisa-se apenas o texto das unidades dos JSONs da skill 01.
7. **Transparência total:** todo método e toda escolha estão no código **e** na descrição em texto.
8. **Reprodutibilidade:** parâmetros centralizados, semente fixa, versões e *hashes* registrados.
9. **Neutralidade e simetria:** nenhum plano é privilegiado e nenhum parâmetro é escolhido para produzir um resultado desejado.
10. **Exclusividade das fontes:** só se usam os JSONs dos planos. Os relatórios de extração e os materiais de outras pastas não são consultados.
11. **Fragilidades declaradas:** instabilidade de frequências baixas, diferenças de gênero, extensão e data dos planos e erros de lematização são sempre declarados.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma comparação que ignore a diferença de tamanho entre os planos, que trate ruído estatístico como diferença real ou que esconda escolhas metodológicas compromete a validade dos resultados publicados. O padrão exigido é o máximo.
