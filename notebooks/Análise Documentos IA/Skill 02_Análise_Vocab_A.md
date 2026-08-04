# Skill 02_Análise_Vocab_A – Análise de Vocabulário e Termos (Complemento à Skill02)

## Relação com a Skill02

Esta skill é um **complemento especializado da Skill02**, aplicável exclusivamente quando a visualização gráfica demandada pelo usuário for baseada em **vocabulário e termos** extraídos de um Plano Nacional de IA. Ela não substitui a Skill02, apenas detalha o método a ser seguido quando esse tipo específico de análise for pedido.

Esta skill herda integralmente, sem necessidade de repetição literal, os seguintes elementos já definidos na Skill01/Skill02: o **Princípio de rigor acadêmico**, a **Regra geral de escopo** (atividade restrita a `notebooks/Análise Documentos IA` e suas subpastas) e o **Protocolo de uso do JSON** (uso exclusivo de `titulo`, `pais_ou_bloco` e `texto_completo`; exclusão de `elementos_descartados`, `data_extracao`, `data_publicacao` e `fonte`). Tudo o que está definido nesses pontos na Skill02 vale integralmente aqui.

## Independência de execução

Assim como o Passo 01 e o Passo 02, esta skill **só é executada quando explicitamente demandada pelo usuário**. Ela não é disparada automaticamente sempre que a Skill02 for usada, e a Skill02 não pressupõe o uso desta skill. O usuário determina, a cada prompt, se a análise gráfica solicitada é uma análise de vocabulário (aciona esta skill) ou outro tipo de análise (segue apenas a Skill02).

## Escopo desta skill: apenas análise individual

Esta skill se aplica **somente à análise individual de cada documento**, feita nas pastas `Brasil`, `China`, `Estados Unidos`, `Europa` e `Índia`, sempre com base no único JSON indicado pelo usuário naquela pasta.

Esta skill **não se aplica à pasta "Análise Conjunta"**. Comparar vocabulário entre documentos de tamanhos e idiomas diferentes exige normalização adicional (frequência relativa entre corpora, tradução/alinhamento terminológico entre idiomas) que não está coberta aqui — se o usuário demandar uma análise de vocabulário conjunta entre países, isso deve ser tratado como uma skill própria, não como uma extensão automática desta.

## Objetivo

Construir visualizações gráficas fundamentadas na análise do vocabulário e dos termos utilizados dentro de `texto_completo` de um único Plano Nacional de IA, conforme a demanda específica do usuário, com o máximo de precisão terminológica e metodológica.

## Etapas metodológicas

### 1. Identificação do idioma do documento

Antes de qualquer contagem ou seleção de termos, identificar o idioma predominante em que `texto_completo` está escrito (o idioma original do documento não corresponde necessariamente ao país — ex.: um documento chinês pode estar disponível apenas em inglês). A lista de palavras funcionais a desconsiderar (artigos, preposições, conjunções, pronomes, verbos auxiliares) e as regras de normalização morfológica devem corresponder ao idioma identificado. Aplicar critérios de um idioma a um texto escrito em outro é um erro metodológico grave e deve ser evitado.

### 2. Extração bruta dos termos

Extrair todos os termos de `texto_completo` de forma integral, sem qualquer corte ou seleção prévia de conteúdo — a seleção do que entra ou não na análise ocorre apenas nas etapas seguintes, de forma explícita e justificada.

### 3. Duas operações distintas: remoção e normalização

É necessário distinguir claramente dois procedimentos diferentes, para não confundir exclusão de conteúdo com unificação de conteúdo equivalente:

**(a) Remoção (exclusão) de termos que não contribuem para a análise** — termos que inflam desnecessariamente a contagem e atrapalham metodologicamente o resultado, tais como:
- Palavras funcionais do idioma identificado (artigos, preposições, conjunções, pronomes, verbos auxiliares);
- Números isolados, símbolos, marcadores de lista ou outros resíduos não semânticos;
- Termos genéricos que, no contexto da demanda específica feita pelo usuário, não agregam valor analítico (essa justificativa deve ser feita caso a caso, e não a partir de uma lista fixa e universal de exclusão).

**(b) Normalização/agrupamento de variantes redundantes** — unificação de termos que representam o mesmo conceito, sem descartar nenhum deles do cômputo, apenas consolidando-os sob um único rótulo representativo:
- Variações morfológicas de um mesmo lema (singular/plural, conjugações verbais — ex.: "sistema"/"sistemas");
- Siglas e suas formas por extenso quando designam exatamente o mesmo referente (ex.: "IA" e "Inteligência Artificial"; "AI" e "Artificial Intelligence");
- Variações de maiúsculas/minúsculas do mesmo termo.

Um termo só pode ser agrupado a outro se designar **exatamente o mesmo referente**. Termos com grafias parecidas, mas significados distintos, **nunca** devem ser fundidos — esse é o principal risco de imprecisão nesta etapa e deve ser tratado com o máximo cuidado.

**Atenção a expressões compostas:** expressões técnicas de mais de uma palavra (ex.: "inteligência artificial", "aprendizado de máquina") devem ser tratadas como uma única unidade analítica quando é isso que o termo designa, e não fragmentadas em palavras isoladas — fragmentá-las distorce a contagem de frequência e o significado do termo.

### 4. Critério de corte

Definir e declarar explicitamente o critério utilizado para selecionar quais termos entram na visualização final (ex.: frequência mínima, número fixo de termos mais frequentes, percentil de corte). O critério deve ser consistente ao longo de uma mesma análise e informado ao usuário junto com o restante da metodologia.

### 5. Transparência obrigatória com o usuário

A cada análise de vocabulário realizada, deve-se informar ao usuário, de forma explícita:
- Quais palavras/termos foram retirados e por quê (justificativa linguística/metodológica de cada exclusão);
- Quais variantes foram agrupadas e sob qual termo representativo;
- Qual foi o critério de corte utilizado para os termos que entraram no gráfico.

**Salvaguarda contra viés de confirmação:** o critério de remoção ou agrupamento de um termo deve ser sempre linguístico ou metodológico — nunca baseado em o termo favorecer ou contrariar alguma conclusão, narrativa ou expectativa sobre o resultado da análise. Remover um termo porque ele "atrapalha o argumento" em vez de "atrapalha metodologicamente" é uma violação do rigor acadêmico exigido neste trabalho.

### 6. Registro persistente e atualizável por documento

Para cada JSON analisado sob esta skill, deve ser mantido um registro persistente na mesma pasta do país (ex.: `notebooks/Análise Documentos IA/Brasil/`), associado ao documento de origem, contendo:
- Lista de termos removidos e a justificativa de cada remoção;
- Lista de agrupamentos de variantes e o termo representativo de cada grupo;
- Critério de corte aplicado;
- Data da última atualização.

Esse registro deve ser **lido antes de qualquer nova visualização de vocabulário** sobre o mesmo documento, para manter consistência metodológica entre gráficos diferentes construídos ao longo do tempo. Sempre que o usuário pedir a remoção de novas palavras, esse registro deve ser **atualizado de forma cumulativa** (mantendo as decisões anteriores, salvo se o usuário pedir para reverter alguma delas), e a descrição apresentada ao usuário deve refletir o estado mais atual da lista.

### 7. Construção do gráfico

Construir a visualização gráfica solicitada pelo usuário com base no vocabulário já tratado (após remoção e normalização), sem tipo de gráfico fixo predefinido — o formato depende exclusivamente do que for demandado.

### 8. Análise final obrigatória

Toda visualização de vocabulário produzida por esta skill deve ser acompanhada de uma análise final contendo:
- A metodologia aplicada (idioma identificado, critério de remoção, critério de agrupamento, critério de corte);
- A lista atualizada de palavras retiradas e de variantes agrupadas;
- O que o gráfico mostra e como interpretá-lo;
- Ajustes possíveis para melhorar a visualização;
- Limitações, imprecisões remanescentes ou fraquezas metodológicas do gráfico, se existirem.

## Resultado esperado

Gráficos de vocabulário fiéis ao conteúdo do documento analisado, construídos com critérios de exclusão e normalização de termos explícitos, justificados, auditáveis e reprodutíveis, livres de vieses narrativos, e sempre acompanhados da metodologia e da interpretação exigidas pela Skill02.
