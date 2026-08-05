# Skill 02_Análise_Vocab_B – Análise Comparada de Vocabulário e Termos entre Documentos (Complemento à Skill02)

## Relação com a Skill02

Esta skill é um **complemento especializado da Skill02**, aplicável exclusivamente quando a visualização gráfica demandada pelo usuário for baseada em **vocabulário e termos comparados entre múltiplos Planos Nacionais de IA**. Ela não substitui a Skill02, apenas detalha o método a ser seguido quando esse tipo específico de análise comparada for pedido.

Esta skill herda integralmente, sem necessidade de repetição literal, os seguintes elementos já definidos na Skill01/Skill02: o **Princípio de rigor acadêmico**, a **Regra geral de escopo** (atividade restrita a `notebooks/Análise Documentos IA` e suas subpastas) e o **Protocolo de uso do JSON** (uso exclusivo de `titulo`, `pais_ou_bloco` e `texto_completo` de cada documento; exclusão de `elementos_descartados`, `data_extracao`, `data_publicacao` e `fonte`). Tudo o que está definido nesses pontos na Skill02 vale integralmente aqui, aplicado a cada um dos documentos envolvidos na comparação.

## Independência de execução

Assim como as demais skills deste fluxo, esta skill **só é executada quando explicitamente demandada pelo usuário**, especificamente quando a demanda envolver uma análise de vocabulário **conjunta/comparada** entre documentos. Esta skill é independente da **Skill 02_Análise_Vocab_A**: o uso de uma não implica o uso da outra. O usuário determina, a cada prompt, se a análise é individual (aciona a Vocab_A, na respectiva pasta de país) ou conjunta (aciona esta skill, na pasta "Análise Conjunta").

## Escopo desta skill: apenas análise conjunta

Esta skill se aplica **somente à pasta "Análise Conjunta"**, utilizando os JSONs das pastas `Brasil`, `China`, `Estados Unidos`, `Europa` e `Índia`. Ela **não se aplica** às pastas individuais de país — essas seguem a **Skill 02_Análise_Vocab_A** quando for demandada análise de vocabulário de um único documento.

O conjunto de documentos disponíveis para a comparação é, em princípio, os cinco planos nacionais (um por pasta de país). Quais documentos efetivamente entram em cada gráfico, e sob qual recorte, segue sempre a demanda específica indicada pelo usuário em cada prompt — nem toda análise precisa necessariamente comparar os cinco simultaneamente.

## Documento central da comparação

A orientação geral deste projeto de pesquisa é mapear o **PBIA (documento brasileiro)** diante dos demais planos nacionais de IA, verificando a proximidade temática e vocabular entre eles. Ainda assim, **isso não deve ser assumido automaticamente** em toda execução: é necessário sempre verificar, a partir da demanda do usuário, qual documento (o PBIA ou outro) deve ser tratado como peça central/referência da análise, e sob qual eixo de comparação (temático, vocabular, ou outro indicado). Tratar um documento como central sem confirmação explícita, quando o prompt do usuário não deixar isso claro, é uma imprecisão metodológica a ser evitada.

## Objetivo

Construir visualizações gráficas comparadas, fundamentadas na análise do vocabulário e dos termos utilizados em `texto_completo` de múltiplos Planos Nacionais de IA, verificando similaridade textual, similaridade de termos utilizados, e em quais aspectos e temáticas os documentos se aproximam ou se diferenciam — sempre conforme a demanda específica do usuário, com o máximo de precisão terminológica e metodológica.

## Etapas metodológicas

### 1. Identificação do idioma de cada documento

Identificar o idioma predominante de `texto_completo` em **cada um** dos documentos envolvidos na comparação (o idioma original não corresponde necessariamente ao país — ex.: um documento chinês pode estar disponível apenas em inglês). Isso é ainda mais crítico aqui do que na análise individual: comparar a frequência literal de palavras entre documentos escritos em idiomas diferentes é metodologicamente inválido sem uma etapa explícita de equivalência conceitual/tradução.

- Se todos os documentos comparados estiverem no mesmo idioma, a comparação lexical direta (após remoção e normalização, ver etapa 3) é válida.
- Se os documentos comparados estiverem em idiomas diferentes, a comparação **não pode se basear em correspondência literal de strings**. É necessário declarar explicitamente o método usado para tornar os termos comparáveis (ex.: mapeamento de termos equivalentes por conceito, uso de versões oficiais traduzidas quando existirem) e registrar essa etapa como uma limitação metodológica, já que toda tradução introduz imprecisão adicional em relação ao texto original.

### 2. Extração bruta dos termos de cada documento

Extrair todos os termos de `texto_completo` de cada documento envolvido, de forma integral e individual, seguindo o Protocolo de uso do JSON da Skill02, antes de qualquer cruzamento entre documentos.

### 3. Remoção e normalização (por documento, depois entre documentos)

Aplicar, a cada documento individualmente, as mesmas duas operações definidas na Skill 02_Análise_Vocab_A:

**(a) Remoção** de termos que não contribuem para a análise (palavras funcionais do idioma do respectivo documento, números isolados, símbolos, marcadores não semânticos, termos genéricos sem valor analítico para a demanda específica).

**(b) Normalização/agrupamento** de variantes redundantes que designam o mesmo referente (variações morfológicas, siglas e formas por extenso, maiúsculas/minúsculas, expressões compostas tratadas como unidade única).

Após esse tratamento por documento, se a comparação envolver mais de um idioma, realizar como etapa **separada e explicitamente identificada** o alinhamento de termos equivalentes entre idiomas (conforme etapa 1). Essa etapa de alinhamento entre idiomas nunca deve ser confundida com a normalização interna de um único documento — são operações distintas e devem ser relatadas separadamente ao usuário.

Um termo só pode ser agrupado a outro (dentro do mesmo documento ou entre documentos) se designar **exatamente o mesmo referente**. Termos parecidos, mas com significados distintos, nunca devem ser fundidos.

### 4. Normalização pela extensão do documento (comparação relativa)

Cada documento possui um tamanho diferente, e comparar contagens absolutas de termos entre documentos de tamanhos distintos produz distorções — um documento mais longo tenderia a parecer artificialmente "mais rico" em qualquer termo apenas por ser maior. Por isso, toda comparação entre documentos deve ser feita com **medidas relativas** (ex.: frequência relativa do termo em relação ao total de termos do próprio documento, ou outra medida normalizada equivalente), nunca com contagens brutas. O método de normalização utilizado deve ser declarado explicitamente ao usuário.

### 5. Critério de corte

Definir e declarar explicitamente o critério utilizado para selecionar quais termos entram na visualização comparada (ex.: frequência relativa mínima, número fixo de termos mais relevantes por documento, percentil de corte). O mesmo critério deve ser aplicado de forma **uniforme a todos os documentos comparados** — usar critérios de corte diferentes por documento introduziria um viés na comparação.

### 6. Métrica de comparação/similaridade

Não há uma métrica ou tipo de gráfico fixo ao qual esta skill esteja presa. A cada demanda, deve-se ler esta skill e construir a análise de similaridade textual, de termos, ou de temáticas que o usuário pedir (ex.: sobreposição de vocabulário entre documentos, proximidade de frequência relativa em torno de temas específicos, comparação de ranking de termos mais relevantes). Qualquer que seja a métrica escolhida, ela deve ser declarada e justificada explicitamente, nunca aplicada de forma implícita.

### 7. Transparência obrigatória com o usuário

A cada análise comparada realizada, deve-se informar ao usuário, de forma explícita:
- Quais documentos entraram na comparação, e qual foi tratado como central/referência;
- O idioma de cada documento, e o método de equivalência entre idiomas, se aplicável;
- Quais palavras/termos foram retirados em cada documento, e por quê;
- Quais variantes foram agrupadas (dentro de cada documento e, se aplicável, entre documentos) e sob qual termo representativo;
- O método de normalização relativa utilizado para tornar os documentos comparáveis apesar dos tamanhos diferentes;
- O critério de corte utilizado.

**Salvaguarda contra viés de confirmação:** a escolha de quais documentos comparar, qual tratar como central, quais termos remover ou agrupar, e qual métrica de comparação usar deve ser sempre linguística ou metodológica — nunca guiada pelo resultado que se espera ou deseja obter (ex.: aproximar ou afastar o PBIA dos demais planos). Selecionar documentos, termos ou métricas para produzir uma conclusão pré-definida é uma violação do rigor acadêmico exigido neste trabalho.

### 8. Registro persistente e atualizável

Deve ser mantido, na pasta **Análise Conjunta**, um registro persistente associado a cada conjunto de documentos comparado, contendo:
- Documentos incluídos na comparação e qual foi tratado como central;
- Idioma de cada documento e método de equivalência entre idiomas, se aplicável;
- Lista de termos removidos por documento e a justificativa de cada remoção;
- Lista de agrupamentos de variantes (internos e, se houver, entre idiomas) e o termo representativo de cada grupo;
- Método de normalização relativa e critério de corte aplicados;
- Data da última atualização.

Esse registro deve ser **lido antes de qualquer nova visualização comparada** envolvendo os mesmos documentos, para manter consistência metodológica entre gráficos diferentes construídos ao longo do tempo. Sempre que o usuário pedir a remoção de novas palavras ou o ajuste de algum critério, o registro deve ser **atualizado de forma cumulativa** (mantendo decisões anteriores, salvo pedido de reversão), e a descrição apresentada ao usuário deve refletir o estado mais atual.

### 9. Construção do gráfico

Construir a visualização gráfica solicitada pelo usuário com base no vocabulário já tratado e normalizado entre os documentos, sem tipo de gráfico fixo predefinido — o formato depende exclusivamente do que for demandado, desde que represente adequadamente a natureza relativa (e não absoluta) da comparação.

### 10. Análise final obrigatória

Toda visualização comparada produzida por esta skill deve ser acompanhada de uma análise final contendo:
- A metodologia aplicada (idiomas envolvidos, documento central, método de normalização relativa, critério de corte, métrica de comparação);
- A lista atualizada de palavras retiradas e de variantes agrupadas por documento;
- O que o gráfico mostra e como interpretá-lo;
- Em quais aspectos e temáticas os documentos comparados se aproximam e se diferenciam, de acordo estritamente com o que o gráfico permite sustentar — sem generalizações ou simplificações que extrapolem o que os dados efetivamente mostram;
- Ajustes possíveis para melhorar a visualização;
- Limitações, lacunas remanescentes (mantidas ao mínimo possível) ou fraquezas metodológicas do gráfico, se existirem — com atenção especial às limitações inerentes à comparação entre documentos de tamanhos e, eventualmente, idiomas diferentes.

## Resultado esperado

Gráficos comparados de vocabulário e termos, claros, acadêmicos e coerentes, fiéis ao conteúdo dos documentos analisados, construídos com normalização relativa explícita entre documentos de tamanhos diferentes, critérios de exclusão e agrupamento de termos justificados e auditáveis, livres de vieses narrativos, e sempre acompanhados da metodologia e da interpretação exigidas pela Skill02 — mapeando com precisão as aproximações e diferenças entre os Planos Nacionais de IA conforme a demanda do usuário.
