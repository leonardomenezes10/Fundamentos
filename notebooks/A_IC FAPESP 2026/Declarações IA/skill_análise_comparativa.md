---
name: skill_análise_comparativa
description: Etapa 03 do fluxo de análise das Declarações sobre IA (IC FAPESP 2026). Orienta a análise CONJUNTA e comparativa de duas ou mais declarações, em notebook Jupyter, a partir dos JSONs produzidos pela skill 01, com comparação relativa (ocorrências por 1.000 tokens) e metodologia explícita.
etapa: 03
versao: 1.0
data: 2026-10-01
---

# Skill de Análise Comparativa — Declarações IA (Etapa 03)

> **Aplicação obrigatória.** Toda análise **conjunta ou comparativa** entre declarações feita dentro da pasta `notebooks/A_IC FAPESP 2026/Declarações IA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook comparativo, o agente deve ler esta skill e cumpri-la por inteiro. Esta skill **amplia** a skill 02 (`skill_análise_individual.md`): todas as regras da skill 02 valem aqui, com os acréscimos e as mudanças descritos abaixo.

> ⚠️ **OS COMANDOS DO PESQUISADOR SÃO OBEDECIDOS EM ÚLTIMA INSTÂNCIA.** Eles prevalecem sobre qualquer regra desta skill. Visualizações, relatórios e outras saídas **só vão para a pasta `resultados/` por comando do pesquisador** (seção 4.4).

---

## 1. Contexto

### 1.1. A pesquisa

Esta skill integra o projeto de Iniciação Científica *"As Relações Brasil-China e a Política de Governança Brasileira sobre Inteligência Artificial"* (FAPESP, Processo nº 2026/04597-1). A comparação entre declarações sobre IA permite identificar **semelhanças, distinções, enfoques e ênfases** entre os atores internacionais no debate sobre a governança da IA. Com isso, o posicionamento de Brasil e China pode ser situado em relação aos demais.

Os resultados comparativos podem ser incorporados a relatórios científicos. Uma comparação mal construída, por exemplo entre valores absolutos de documentos de tamanhos diferentes, produz **conclusões falsas**. Por isso, esta skill exige comparação **relativa** e procedimento **idêntico** para todos os documentos.

### 1.2. Rigor acadêmico e transparência metodológica

Valem integralmente as regras da skill 02 (seção 1.2):
- cada comando pedido é executado exatamente conforme as instruções desta skill e do pedido do pesquisador;
- toda escolha metodológica está visível no código **e** descrita em texto logo após a visualização que ela afeta;
- o procedimento é reprodutível, com semente fixa e parâmetros registrados;
- na dúvida, o agente para e pergunta ao pesquisador.

### 1.3. Restrição de ambiente e de fontes

- **Pasta de atuação exclusiva:** `notebooks/A_IC FAPESP 2026/Declarações IA/`.
- **Insumos permitidos:** (a) os JSONs das declarações produzidos pela **skill 01** (`<SIGLA>_extracao.json`); (b) as instruções do pesquisador.
- **É PROIBIDO**, salvo pedido expresso do pesquisador:
  - investigar outras páginas, pastas ou notebooks do repositório para buscar padrões de resposta, resultados anteriores ou modelos de análise;
  - se espelhar em outras resoluções, análises ou interpretações sobre os mesmos documentos ou o mesmo caso;
  - usar informações externas para contextualizar ou interpretar as diferenças encontradas;
  - ler, criar, alterar ou apagar arquivos fora desta pasta.
- O notebook comparativo **reprocessa** os JSONs da skill 01 com o mesmo pipeline. Ele **não** usa números copiados dos notebooks individuais. Assim, os dois documentos são tratados no mesmo processamento e com os mesmos parâmetros.

### 1.4. Posição desta skill no fluxo de trabalho

| Etapa | Função | Skill |
|---|---|---|
| 01 | Extração do conteúdo integral das declarações para JSON + relatório de retiradas (CSV) | `skill_extração.md` |
| 02 | Análise individual de cada declaração | `skill_análise_individual.md` |
| **03** | **Análise comparativa entre declarações, com normalização relativa** | **esta skill** |

### 1.5. Autoridade do pesquisador

As **ordens e comandos do pesquisador são a decisão final e são obedecidos em última instância**. O agente pode propor instrumentos e limiares e apontar riscos, mas não impõe escolhas. Quando uma ordem tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.

---

## 2. Objetivos

### 2.1. Objetivo principal

Comparar, em notebook Jupyter (`.ipynb`), o conteúdo extraído de duas ou mais declarações e produzir **visualizações gráficas e interpretações comparativas**. A comparação é feita sempre em **termos relativos (ocorrências por 1.000 tokens)**, e não absolutos, para permitir verificar semelhanças, distinções, diferentes enfoques, diferentes ênfases, termos mais comuns e termos mais distintivos de cada documento.

### 2.2. Objetivos específicos

1. **Verificar os insumos:** confirmar que todos os JSONs vêm da skill 01, estão íntegros e estão no mesmo idioma.
2. **Expor a disparidade de tamanho** entre os documentos, que justifica a normalização relativa.
3. **Comparar os termos mais frequentes** de cada documento, em ocorrências por 1.000 tokens.
4. **Identificar semelhanças:** termos com peso relativo parecido nos documentos.
5. **Identificar distinções:** termos significativamente mais característicos de um documento do que do outro (análise de *keyness*).
6. **Comparar o vocabulário** compartilhado e exclusivo, com as ressalvas de tamanho.
7. **Comparar os enfoques temáticos**, com intervalos de confiança para cada documento e para a diferença entre eles.
8. **Comparar a ênfase normativa** (verbos modais).
9. **Interpretar** cada visualização com base nos valores obtidos, apontando método, escolhas e fragilidades.
10. **Registrar** parâmetros, versões e saídas para garantir a reprodutibilidade.

---

## 3. Diretrizes para a análise

### 3.1. Insumo: o que entra e o que não entra

Igual à skill 02 (seção 3.1). De cada JSON são usados **apenas** o título (`document.title`, para identificação) e o texto integral e literal de cada parágrafo ou item (`sections[].text`). O `id` serve apenas como índice de posição. **Todo conteúdo periférico fica fora da análise.**

### 3.2. Identidade de procedimento

- **Mesmo pipeline e mesmos parâmetros** para todos os documentos comparados. O pré-processamento é o da skill 02 (seção 3.3).
- **Mesmo idioma.** Documentos em idiomas diferentes não são comparados lexicalmente. Se os idiomas divergirem, o agente para e informa o pesquisador.
- **Simetria.** Nenhum documento é tratado como referência privilegiada. A convenção de sentido das medidas (por exemplo, valores positivos = mais característico do documento A) é declarada e mantida em todas as figuras.
- **Cores fixas por documento**, as mesmas usadas nos notebooks individuais.

### 3.3. Comparação relativa: ocorrências por 1.000 tokens

Os documentos têm **tamanhos diferentes**. Comparar frequências absolutas favoreceria o documento mais longo e produziria distorções. Por isso, **toda comparação entre documentos é feita em ocorrências por 1.000 tokens**:

> **taxa por 1.000 tokens = (ocorrências do termo no documento ÷ total de tokens do documento) × 1.000**

- **Token** é definido como na skill 02: palavra (sequência de letras, com hífen interno ou sigla com pontos), sem números e pontuação.
- **O denominador é o total de tokens do documento, incluindo *stopwords*.** É a mesma base para todos os termos e para todas as categorias.
- Com essa normalização, os termos analisados ficam em **pé de igualdade**: uma taxa de 5 por 1.000 tem o mesmo significado em um documento de 1.500 tokens e em um de 15.000.
- Valores **absolutos** aparecem apenas na tabela de perfil, para **expor a disparidade de tamanho**, e como informação auxiliar nas tabelas. Eles **nunca** são usados para afirmar que um documento enfatiza algo mais do que outro.

### 3.4. Regras para as visualizações

Valem todas as regras da skill 02 (seção 3.6), com os acréscimos:
1. **Toda visualização comparativa usa taxas por 1.000 tokens** (ou medidas derivadas delas), nunca contagens absolutas.
2. Os documentos aparecem sempre na **mesma ordem** e com as **mesmas cores**.

### 3.5. Vieses proibidos

Valem todos os da skill 02 (seção 3.5), e mais:
- comparar valores absolutos de documentos de tamanhos diferentes como se fossem comparáveis;
- afirmar que um documento "enfatiza mais" um tema com base em diferenças que não passaram pelos critérios da seção 3.4;
- escolher o documento de referência ou o sentido da comparação para favorecer uma leitura;
- atribuir as diferenças a posições políticas dos atores sem considerar gênero, extensão e função dos textos.

---

## 4. Protocolo de operação

### 4.1. Procedimento passo a passo

1. **Ler esta skill e a skill 02** por inteiro antes de começar.
2. **Configurar** os parâmetros na célula de configuração (documentos, pré-processamento, limiares comparativos).
3. **Processar** todos os documentos com o mesmo pipeline.
4. **Expor o perfil comparativo** e a disparidade de tamanho.
5. **Gerar** cada visualização comparativa com sua tabela correspondente.
6. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
7. **Registrar** a execução (parâmetros, versões, *hash* de todos os insumos, lista de saídas).
8. **Informar** ao pesquisador, de forma breve, o que foi produzido e quais pontos exigem a atenção dele.

### 4.2. Estrutura obrigatória do notebook

1. **Apresentação:** do que se trata, finalidade, insumos (skill 01), recorte do conteúdo, método, justificativa da comparação relativa, transparência das escolhas e vínculo com esta skill.
2. **Configuração:** todos os parâmetros editáveis em uma única célula.
3. **Ambiente e funções:** restrição de pasta, estilo e funções do pipeline (idênticas às da skill 02) e funções comparativas.
4. **Carregamento e verificação** de todos os JSONs.
5. **Pré-processamento** e **perfil comparativo** (com a disparidade de tamanho).
6. **Análises e visualizações comparativas**, cada uma seguida do bloco de texto da seção 4.3.
7. **Registro de execução** e **síntese** final.

### 4.3. Bloco de texto após cada visualização

Igual à skill 02 (seção 4.3): **Método e escolhas**, **Como ler**, **Interpretação** (redigida só depois da execução, a partir dos valores obtidos, separando observação de inferência) e **Fragilidades e ajustes possíveis** (quando necessário). Na interpretação comparativa, toda afirmação de diferença deve indicar o critério que a sustenta (G² e *Log Ratio*, ou intervalo de confiança da diferença).

### 4.4. Pasta `resultados`

- Visualizações, tabelas, relatórios e quaisquer outras saídas **só vão para a pasta `resultados/` quando o pesquisador der o comando**, e da forma que ele exigir.
- **Nenhuma** visualização é adicionada automaticamente a `resultados/`. Sem o comando, o notebook apenas exibe as visualizações e as tabelas, sem gravá-las (`SALVAR_SAIDAS = False` na célula de configuração).

---

## 5. Regras de qualidade e rigor acadêmico

1. **Comparação relativa obrigatória:** nenhuma conclusão comparativa se apoia em valores absolutos.
2. **Identidade de procedimento:** mesmo pipeline, mesmos parâmetros e mesmo idioma para todos os documentos.
3. **Significância com tamanho de efeito:** diferenças termo a termo só são afirmadas quando passam pelos dois critérios. Diferenças entre categorias só são afirmadas quando o intervalo de confiança da diferença não inclui zero.
4. **Fidelidade ao insumo:** analisa-se apenas o texto integral e literal das unidades dos JSONs da skill 01.
5. **Transparência total:** todo método e toda escolha estão no código **e** na descrição em texto.
6. **Reprodutibilidade:** parâmetros centralizados, semente fixa, versões e *hashes* registrados.
7. **Neutralidade e simetria:** nenhum documento é privilegiado e nenhum parâmetro é escolhido para produzir um resultado desejado.
8. **Exclusividade das fontes:** só se usa o que está nesta pasta.
9. **Fragilidades declaradas:** instabilidade de frequências baixas, diferença de gênero textual e erros de lematização são sempre declarados.
10. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final e são obedecidos em última instância.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma comparação que ignore a diferença de tamanho entre documentos, que trate ruído estatístico como diferença real ou que esconda escolhas metodológicas compromete a validade dos resultados publicados. O padrão exigido é o máximo.
