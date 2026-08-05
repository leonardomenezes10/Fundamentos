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

**(c) Exclusão de termos idiossincráticos de identificação nacional/institucional — exclusiva desta comparação conjunta, sem equivalente na Skill 02_Análise_Vocab_A.** Diferentemente da análise individual de um único documento — onde nomes de país, siglas de órgãos governamentais e iniciativas nacionais são vocabulário legítimo e informativo sobre aquele documento específico —, a comparação entre documentos exige um filtro adicional: termos que apenas nomeiam a identidade nacional/institucional do próprio documento — e que, por definição, tendem a não ocorrer nos demais documentos por serem exclusivos daquele país/bloco — devem ser excluídos da análise de similaridade. Sem essa exclusão, esses termos inflam artificialmente a "singularidade" estatística de um documento sem refletir nenhuma escolha temática real: um documento não é mais ou menos temático-conceitualmente distinto por nomear a si mesmo.

Essa exclusão exige distinguir, com minúcia e caso a caso — nunca por uma lista fixa e automática —, dois tipos de termos que podem parecer semelhantes à primeira vista, mas são de natureza analítica oposta:

- **Termos técnicos do campo de política de IA/relações internacionais que representam uma especificidade real de abordagem** — mantidos na análise, mesmo que ocorram em um único documento, porque designam um enquadramento, mecanismo ou valor que é, em si, um eixo de comparação legítimo com os demais documentos (ex.: "ally"/"enemy" no documento estadunidense refletem uma moldura de rivalidade geopolítica que os demais documentos não empregam — a ausência desse enquadramento nos outros documentos é, ela mesma, um dado comparativo relevante, não um artefato a descartar).
- **Identificadores de nacionalidade/instituição que apenas nomeiam o próprio documento, sem carregar conteúdo temático-conceitual autônomo** — excluídos da análise de similaridade (ex.: "Brazil"/"Brazilian" no PBIA; "European"/"Europe" nos documentos da União Europeia; siglas de órgãos e agências governamentais específicas de um único país, como "DOC", "DOD", "NIST", "CAISI" nos documentos estadunidenses; nomes de iniciativas ou estruturas nomeadas exclusivas de um único país, como "NIB" no Brasil). A ausência desses termos nos demais documentos não torna o documento de origem tematicamente mais distinto — é apenas o efeito mecânico de que cada documento nomeia a si mesmo, seu governo e suas próprias instituições.

Em caso de dúvida real sobre se um termo é identificador próprio ou especificidade temática genuína, a decisão deve seguir o mesmo padrão de julgamento fundamentado — nunca automático, nunca por lista fixa universal — já exigido pela Skill 02_Análise_Vocab_A para as demais decisões de remoção e normalização, priorizando sempre a permanência de termos temático-conceituais (que descrevem uma abordagem, mecanismo, valor ou estratégia de política de IA) e a exclusão de identificadores que apenas nomeiam o país, bloco, governo ou instituição responsável pelo documento. Cada exclusão desse tipo deve ser registrada com a justificativa individual no registro persistente (item 8, abaixo), com o mesmo rigor exigido para as demais remoções.

Após esse tratamento por documento, se a comparação envolver mais de um idioma, realizar como etapa **separada e explicitamente identificada** o alinhamento de termos equivalentes entre idiomas (conforme etapa 1). Essa etapa de alinhamento entre idiomas nunca deve ser confundida com a normalização interna de um único documento — são operações distintas e devem ser relatadas separadamente ao usuário.

Um termo só pode ser agrupado a outro (dentro do mesmo documento ou entre documentos) se designar **exatamente o mesmo referente**. Termos parecidos, mas com significados distintos, nunca devem ser fundidos — nem mesmo quando pertencem ao mesmo campo semântico (ex.: "smart" e "intelligent" permanecem distintos em todos os documentos comparados, mesma lógica do princípio geral de não fusão de quase-sinônimos da Skill 02_Análise_Vocab_A, item 5).

**Bigramas essenciais e compostos com hífen (herdado da Skill 02_Análise_Vocab_A, itens 3-4, aplicado a cada documento da comparação):** expressões de mais de uma palavra que nomeiam um conceito, modelo ou mecanismo de governança com relevância analítica para a comparação entre países/blocos — grafadas com espaço (ex.: "open source") ou com hífen (ex.: "open-source", "decision-making", "data-driven") — devem ser tratadas como unidade única em **todos** os documentos onde ocorrerem, nunca fragmentadas em palavras soltas. É especialmente importante manter esse tratamento uniforme entre os documentos comparados: se "open-source" for preservado como unidade no documento chinês mas fragmentado em "open"+"source" no documento europeu, a comparação deixa de ser válida, porque estaria comparando grandezas de natureza diferente sob o mesmo rótulo.

Da mesma forma, é proibida qualquer regra cega de tratamento de hífen (nem "hífen sempre separa", nem "hífen sempre une") — cada forma hifenizada identificada em cada documento deve ser avaliada individualmente (mantida unida ou separada, conforme o critério do item 4 da Skill 02_Análise_Vocab_A) e essa decisão deve ser **replicada de forma consistente** sempre que a mesma forma hifenizada ocorrer em mais de um documento da comparação, para não introduzir um viés metodológico artificial entre os países comparados.

**Desambiguação contextual de termos polissêmicos entre documentos (herdado da Skill 02_Análise_Vocab_A, item 5):** antes de comparar a frequência de qualquer termo entre documentos, verificar se ele apresenta mais de um referente em cada um dos textos (ex.: "AI" vs. "AI+"; "state(s)" vs. "United States"; "generation" como geração de energia vs. geração tecnológica; "power" como capacidade computacional vs. poder político vs. energia). Termos com mais de um referente devem ser desdobrados em rótulos por sentido **antes** de qualquer comparação entre países — comparar a contagem bruta e não desambiguada de um termo polissêmico entre documentos é metodologicamente inválido, pois pode atribuir a um país uma ênfase temática que na verdade decorre de um sentido do termo irrelevante à comparação em curso.

### 4. Normalização pela extensão do documento (comparação relativa)

Cada documento possui um tamanho diferente, e comparar contagens absolutas de termos entre documentos de tamanhos distintos produz distorções — um documento mais longo tenderia a parecer artificialmente "mais rico" em qualquer termo apenas por ser maior. Por isso, toda comparação entre documentos deve ser feita com **medidas relativas** (ex.: frequência relativa do termo em relação ao total de termos do próprio documento, ou outra medida normalizada equivalente), nunca com contagens brutas. O método de normalização utilizado deve ser declarado explicitamente ao usuário.

### 5. Critério de corte

Definir e declarar explicitamente o critério utilizado para selecionar quais termos entram na visualização comparada. O critério de corte padrão desta skill, herdado da Skill 02_Análise_Vocab_A, é o **Top 50** termos por documento (podendo um recorte de Top 25 ser mantido como visão adicional dentro do mesmo Top 50). O mesmo critério deve ser aplicado de forma **uniforme a todos os documentos comparados** — usar critérios de corte diferentes por documento introduziria um viés na comparação. Assim como na análise individual, o corte de Top 50 só é válido se acompanhado da varredura ampliada de normalização morfológica exigida na Skill 02_Análise_Vocab_A (item 6) em cada um dos documentos comparados.

### 6. Métrica de comparação/similaridade

**Método padrão de mensuração de similaridade entre documentos.** A similaridade de vocabulário entre dois ou mais documentos é medida a partir do vocabulário normalizado (após as etapas de remoção, normalização e exclusão de identificadores próprios da etapa 3) representado como um **vetor de frequência relativa** — a proporção de cada termo em relação ao total de tokens de conteúdo do próprio documento, nunca a contagem absoluta (consistente com a exigência de normalização relativa do item 4 desta skill). Cada documento é assim representado por um vetor no mesmo espaço de termos — a união dos vocabulários normalizados de todos os documentos incluídos na comparação —, e a similaridade entre um par de documentos é calculada sobre esses vetores (ex.: similaridade de cosseno), produzindo um valor único e comparável para cada par. Esse é o método de referência sempre que a demanda do usuário for "similaridade entre documentos" em termos gerais, e deve ser declarado explicitamente como tal sempre que utilizado.

Isso não substitui outras formas de análise de vocabulário/temática que o usuário venha a solicitar de modo complementar ou alternativo (ex.: sobreposição de conjuntos de termos mais frequentes, comparação de ranking, proximidade de frequência relativa em torno de um tema específico) — não há um tipo de gráfico fixo ao qual esta skill esteja presa. Qualquer que seja a métrica efetivamente utilizada em uma visualização, ela deve ser declarada e justificada explicitamente, nunca aplicada de forma implícita.

### 6.1. Sequência estruturada da comparação

A comparação entre os documentos deve seguir uma sequência estruturada, do mais específico para o mais amplo, em vez de comparar todos os pares de documentos de forma desordenada:

1. **Coerência interna por bloco/país.** Primeiro, verificar a similaridade entre os documentos do mesmo país/bloco quando houver mais de um (China: `ai_plus.json` vs. `new_generation_ai_development_plan.json`; União Europeia: `ai_continent_action_plan.json` vs. `apply_ai_strategy.json`) — estabelecendo se os documentos de um mesmo país/bloco falam a mesma "língua" de política de IA entre si ou se divergem internamente. Essa coerência interna nunca deve ser presumida a priori; se a análise revelar divergência interna, isso deve ser reportado como achado, não ocultado.
2. **Comparação entre blocos/países.** Em seguida, comparar as abordagens entre União Europeia, China e Estados Unidos entre si (tratando cada bloco/país como unidade agregada, ou comparando seus documentos individualmente, conforme a demanda do usuário) — verificando se essas três abordagens internacionais estão próximas ou distantes entre si, e em que aspectos.
3. **Posicionamento do PBIA.** Por último, posicionar o PBIA em relação ao conjunto já mapeado nos passos 1-2, verificando o grau de proximidade ou distância do documento brasileiro em relação a cada bloco/país e ao conjunto como um todo.

Essa sequência não impede a construção de uma matriz de similaridade completa entre todos os documentos incluídos na comparação de uma só vez (que continua sendo o instrumento de base, ver item 6) — ela define a **ordem de leitura e apresentação** dos resultados ao usuário, para que a interpretação avance do particular (coerência interna de cada bloco) para o geral (posicionamento do PBIA no conjunto), e não o contrário. Essa sequência deve ser seguida sempre que a demanda do usuário for uma análise de similaridade abrangendo o conjunto dos documentos, salvo indicação explícita em contrário.

### 7. Transparência obrigatória com o usuário

A cada análise comparada realizada, deve-se informar ao usuário, de forma explícita:
- Quais documentos entraram na comparação, e qual foi tratado como central/referência;
- O idioma de cada documento, e o método de equivalência entre idiomas, se aplicável;
- Quais palavras/termos foram retirados em cada documento, e por quê;
- Quais variantes foram agrupadas (dentro de cada documento e, se aplicável, entre documentos) e sob qual termo representativo;
- Quais bigramas/compostos (com ou sem hífen) foram tratados como unidade única em cada documento, e a confirmação de que o mesmo composto recebeu o mesmo tratamento em todos os documentos onde ocorre;
- Quais formas hifenizadas foram identificadas em cada documento e a decisão (unida ou separada) tomada para cada uma, com justificativa;
- Quais termos foram desdobrados por desambiguação contextual em cada documento, com a contagem de cada sentido separadamente;
- Quais termos foram excluídos por serem identificadores idiossincráticos de nacionalidade/instituição (item 3-c) — ex.: gentílicos do próprio país, siglas de órgãos governamentais nacionais, nomes de iniciativas exclusivas de um único país/bloco —, com a justificativa de cada exclusão e a distinção explícita em relação aos termos técnicos mantidos por representarem especificidade real de abordagem;
- O método de normalização relativa utilizado para tornar os documentos comparáveis apesar dos tamanhos diferentes;
- A métrica de similaridade utilizada (item 6 — vetor de frequência relativa e método de cálculo, ex. similaridade de cosseno) e a sequência de comparação seguida (item 6.1), quando a demanda envolver mensuração de similaridade entre os documentos;
- O critério de corte utilizado.

**Salvaguarda contra viés de confirmação:** a escolha de quais documentos comparar, qual tratar como central, quais termos remover ou agrupar, e qual métrica de comparação usar deve ser sempre linguística ou metodológica — nunca guiada pelo resultado que se espera ou deseja obter (ex.: aproximar ou afastar o PBIA dos demais planos). Selecionar documentos, termos ou métricas para produzir uma conclusão pré-definida é uma violação do rigor acadêmico exigido neste trabalho.

### 8. Registro persistente e atualizável

Deve ser mantido, na pasta **Análise Conjunta**, um registro persistente associado a cada conjunto de documentos comparado, contendo:
- Documentos incluídos na comparação e qual foi tratado como central;
- Idioma de cada documento e método de equivalência entre idiomas, se aplicável;
- Lista de termos removidos por documento e a justificativa de cada remoção;
- Lista de agrupamentos de variantes (internos e, se houver, entre idiomas) e o termo representativo de cada grupo;
- Lista de bigramas/compostos tratados como unidade única, por documento, com verificação de consistência entre documentos;
- Auditoria das formas hifenizadas por documento (mantidas unidas ou separadas, com justificativa);
- Lista de termos desdobrados por desambiguação contextual, por documento, com a contagem de cada sentido;
- Lista de termos excluídos por identificação idiossincrática nacional/institucional (item 3-c), por documento, com a justificativa individual de cada exclusão;
- Método de mensuração de similaridade utilizado (item 6 — vetor de frequência relativa) e, quando aplicável, os resultados organizados segundo a sequência estruturada de comparação (item 6.1: coerência interna por bloco, comparação entre blocos, posicionamento do PBIA);
- Método de normalização relativa e critério de corte aplicados;
- Data da última atualização.

Esse registro deve ser **lido antes de qualquer nova visualização comparada** envolvendo os mesmos documentos, para manter consistência metodológica entre gráficos diferentes construídos ao longo do tempo. Sempre que o usuário pedir a remoção de novas palavras ou o ajuste de algum critério, o registro deve ser **atualizado de forma cumulativa** (mantendo decisões anteriores, salvo pedido de reversão), e a descrição apresentada ao usuário deve refletir o estado mais atual.

### 9. Construção do gráfico

Construir a visualização gráfica solicitada pelo usuário com base no vocabulário já tratado e normalizado entre os documentos, sem tipo de gráfico fixo predefinido — o formato depende exclusivamente do que for demandado, desde que represente adequadamente a natureza relativa (e não absoluta) da comparação.

### 10. Análise final obrigatória

Toda visualização comparada produzida por esta skill deve ser acompanhada de uma análise final contendo:
- A metodologia aplicada (idiomas envolvidos, documento central, tratamento de bigramas/hífens, desambiguação contextual, exclusão de identificadores idiossincráticos nacionais/institucionais, método de normalização relativa, critério de corte, métrica de comparação e, quando aplicável, a sequência estruturada de comparação seguida — item 6.1);
- A lista atualizada de palavras retiradas e de variantes agrupadas por documento, incluindo compostos/bigramas preservados e termos desdobrados por sentido;
- O que o gráfico mostra e como interpretá-lo;
- Em quais aspectos e temáticas os documentos comparados se aproximam e se diferenciam, de acordo estritamente com o que o gráfico permite sustentar — sem generalizações ou simplificações que extrapolem o que os dados efetivamente mostram;
- Ajustes possíveis para melhorar a visualização;
- Limitações, lacunas remanescentes (mantidas ao mínimo possível) ou fraquezas metodológicas do gráfico, se existirem — com atenção especial às limitações inerentes à comparação entre documentos de tamanhos e, eventualmente, idiomas diferentes.

## Resultado esperado

Gráficos comparados de vocabulário e termos, claros, acadêmicos e coerentes, fiéis ao conteúdo dos documentos analisados, construídos com normalização relativa explícita entre documentos de tamanhos diferentes, critérios de exclusão e agrupamento de termos justificados e auditáveis, livres de vieses narrativos, e sempre acompanhados da metodologia e da interpretação exigidas pela Skill02 — mapeando com precisão as aproximações e diferenças entre os Planos Nacionais de IA conforme a demanda do usuário.
