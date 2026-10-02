---
name: skill_análise_comparativa
description: Etapa 03 do fluxo de análise das Declarações sobre IA (IC FAPESP 2026). Orienta a análise CONJUNTA e comparativa de duas ou mais declarações, em notebook Jupyter, a partir dos JSONs produzidos pela skill 01, com comparação relativa (ocorrências por 1.000 tokens) e metodologia explícita.
etapa: 03
versao: 1.0
data: 2026-10-01
---

# Skill de Análise Comparativa — Declarações IA (Etapa 03)

> **Aplicação obrigatória.** Toda análise **conjunta ou comparativa** entre declarações feita dentro da pasta `notebooks/A_IC FAPESP 2026/Declarações IA/` **deve** seguir esta skill. Antes de criar, alterar ou executar um notebook comparativo, o agente deve ler esta skill e cumpri-la por inteiro. Esta skill **amplia** a skill 02 (`skill_análise_individual.md`): todas as regras da skill 02 valem aqui, com os acréscimos e as mudanças descritos abaixo.

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

As **ordens e comandos do pesquisador são a decisão final**. O agente pode propor instrumentos e limiares e apontar riscos, mas não impõe escolhas. Quando uma ordem tiver um risco metodológico, o agente **cumpre a ordem e registra o risco** na seção de fragilidades da visualização afetada.

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

### 3.4. Limites da normalização e salvaguardas obrigatórias

A normalização corrige a diferença de tamanho, mas **não** elimina a instabilidade de frequências baixas. Em um documento curto, uma única ocorrência pode gerar uma taxa alta. Por isso:

1. **Frequência mínima:** comparações termo a termo exigem uma frequência mínima combinada (parâmetro editável). Termos raros não são usados para afirmar diferenças.
2. **Significância e tamanho de efeito juntos:** um termo só é dito **distintivo** quando passa ao mesmo tempo por um teste de significância (log-verossimilhança, G²) e por um limiar de tamanho de efeito (*Log Ratio*). Significância sozinha não basta, e diferença de taxa sozinha também não.
3. **Comparações múltiplas:** como muitos termos são testados ao mesmo tempo, o notebook informa também quantos termos permanecem significativos após a correção de Bonferroni.
4. **Incerteza:** as comparações entre categorias trazem **intervalos de confiança por bootstrap** (reamostragem de parágrafos/itens) para cada documento e para a **diferença** entre eles.
5. **Medidas sensíveis ao tamanho** (número de lemas exclusivos, razão tipo/token) só podem ser apresentadas com a ressalva explícita de que crescem com a extensão do texto.

### 3.5. Medidas comparativas adotadas

| Medida | Definição | Uso |
|---|---|---|
| Taxa por 1.000 tokens | Ver seção 3.3 | Base de todas as comparações |
| G² (log-verossimilhança) | Teste de Dunning (1993), na forma de Rayson & Garside (2000), sobre a tabela 2 × 2 (ocorrências do termo × total de tokens de cada documento) | Significância da diferença |
| *Log Ratio* | log₂ da razão entre as taxas relativas dos dois documentos (Hardie, 2014). Frequência zero recebe correção de 0,5. Valor 1 = duas vezes mais frequente; 2 = quatro vezes | Tamanho de efeito da diferença |
| Diferença entre categorias | Diferença entre as taxas por 1.000 tokens, com IC por bootstrap independente em cada documento | Comparação de enfoques |
| Vocabulário compartilhado/exclusivo | Contagem de lemas de conteúdo presentes em ambos ou em apenas um documento | Descrição, sempre com ressalva de tamanho |

### 3.6. Natureza dos documentos

Declarações diferentes podem pertencer a **gêneros textuais diferentes**: um comunicado de líderes, uma recomendação de organismo internacional, uma declaração de princípios. Diferenças de vocabulário podem refletir o gênero, a extensão ou a função do texto, e não apenas posições substantivas. A interpretação comparativa deve **considerar e declarar** essa possibilidade **com base apenas no que os próprios documentos mostram**, sem recorrer a fontes externas.

### 3.7. Regras para as visualizações

Valem todas as regras da skill 02 (seção 3.6), com os acréscimos:
1. **Toda visualização comparativa usa taxas por 1.000 tokens** (ou medidas derivadas delas), nunca contagens absolutas.
2. Os documentos aparecem sempre na **mesma ordem** e com as **mesmas cores**.
3. Gráficos de dispersão entre documentos **não** usam deslocamento aleatório dos pontos (*jitter*): sobreposições são indicadas por transparência e declaradas.
4. A convenção de sentido das medidas assimétricas (*Log Ratio*, diferenças) é escrita no eixo do gráfico.

### 3.8. Vieses proibidos

Valem todos os da skill 02 (seção 3.5), e mais:
- comparar valores absolutos de documentos de tamanhos diferentes como se fossem comparáveis;
- afirmar que um documento "enfatiza mais" um tema com base em diferenças que não passaram pelos critérios da seção 3.4;
- escolher o documento de referência ou o sentido da comparação para favorecer uma leitura;
- atribuir as diferenças a posições políticas dos atores sem considerar gênero, extensão e função dos textos.

---

## 4. Protocolo de operação e entregáveis

### 4.1. Procedimento passo a passo

1. **Ler esta skill e a skill 02** por inteiro antes de começar.
2. **Verificar os insumos:** os JSONs da skill 01 existem nesta pasta, foram produzidos pela skill 01 e estão no mesmo idioma? Há pendências de revisão humana? Se houver problemas, avisar o pesquisador.
3. **Configurar** os parâmetros na célula de configuração (documentos, pré-processamento, limiares comparativos).
4. **Processar** todos os documentos com o mesmo pipeline.
5. **Expor o perfil comparativo** e a disparidade de tamanho.
6. **Gerar** cada visualização comparativa com sua tabela correspondente.
7. **Redigir**, após a execução, o bloco de texto de cada visualização (seção 4.3).
8. **Registrar** a execução (parâmetros, versões, *hash* de todos os insumos, lista de saídas).
9. **Informar** ao pesquisador, de forma breve, o que foi produzido e quais pontos exigem a atenção dele.

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

### 4.4. Entregáveis

| Entregável | Local |
|---|---|
| Notebook comparativo | `Análise_Comparativa_<SIGLA_A>_<SIGLA_B>.ipynb`, nesta pasta |
| Figuras (PNG 300 dpi + PDF) | `resultados/Comparativa_<SIGLA_A>_<SIGLA_B>/<versão>/` |
| Tabelas completas (CSV, UTF-8 com BOM, `;`, vírgula decimal) | `resultados/Comparativa_<SIGLA_A>_<SIGLA_B>/<versão>/` |
| Registro de execução (`registro_execucao.json`) | `resultados/Comparativa_<SIGLA_A>_<SIGLA_B>/<versão>/` |

As regras de não sobrescrita e de versionamento da skill 02 (seção 4.4) valem integralmente.

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
10. **Primazia do pesquisador:** as ordens e os comandos do pesquisador são a decisão final.

> ⚠️ **RIGOR ACADÊMICO E CIENTÍFICO:** esta pesquisa é financiada pela FAPESP e segue o *Código de Boas Práticas Científicas* da instituição. Uma comparação que ignore a diferença de tamanho entre documentos, que trate ruído estatístico como diferença real ou que esconda escolhas metodológicas compromete a validade dos resultados publicados. O padrão exigido é o máximo.

### Referências metodológicas

- DUNNING, T. Accurate methods for the statistics of surprise and coincidence. *Computational Linguistics*, v. 19, n. 1, p. 61-74, 1993.
- RAYSON, P.; GARSIDE, R. Comparing corpora using frequency profiling. In: *Proceedings of the Workshop on Comparing Corpora*, 38th Annual Meeting of the ACL. Hong Kong, 2000. p. 1-6.
- HARDIE, A. Log Ratio: an informal introduction. *ESRC Centre for Corpus Approaches to Social Science (CASS)*, Lancaster University, 2014.
- GABRIELATOS, C. Keyness analysis: nature, metrics and techniques. In: TAYLOR, C.; MARCHI, A. (org.). *Corpus Approaches to Discourse: A Critical Review*. London: Routledge, 2018. p. 225-258.
- McENERY, T.; HARDIE, A. *Corpus Linguistics: Method, Theory and Practice*. Cambridge: Cambridge University Press, 2012.
- GRIES, S. Th. Dispersions and adjusted frequencies in corpora. *International Journal of Corpus Linguistics*, v. 13, n. 4, p. 403-437, 2008.
- EFRON, B.; TIBSHIRANI, R. J. *An Introduction to the Bootstrap*. New York: Chapman & Hall, 1993.
