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

**Atenção a expressões compostas e bigramas essenciais:** expressões técnicas de mais de uma palavra (ex.: "inteligência artificial", "aprendizado de máquina", "open source"/"open-source", "decision-making", "human-computer") devem ser tratadas como uma única unidade analítica quando é isso que o termo designa, e não fragmentadas em palavras isoladas — fragmentá-las distorce a contagem de frequência e o significado do termo. Isso vale tanto para bigramas grafados com espaço (ex.: "open source", "large language model") quanto para bigramas grafados com hífen (ex.: "open-source", "decision-making") — a grafia (espaço ou hífen) é uma escolha ortográfica do documento-fonte, não um critério metodológico de tratamento; o que importa é se as duas palavras, juntas, designam um conceito próprio e reconhecível. Um bigrama é "essencial" quando nomeia um conceito, modelo, mecanismo ou categoria com relevância analítica para a pesquisa de Relações Internacionais em curso — por exemplo, "open source"/"open-source" deve ser preservado como unidade sempre que ocorrer, porque o modelo de governança tecnológica baseado em código aberto é, em si, um eixo de comparação relevante entre os países/blocos estudados (o caso chinês, notadamente, adota esse mecanismo de forma distinta de outros modelos nacionais), e não apenas um detalhe técnico incidental.

### 4. Fragmentação por hífen: proibição de regra cega, exigência de análise caso a caso

É um erro metodológico grave tratar todo hífen do texto como separador universal de tokens por padrão (regra cega), assim como seria um erro oposto e igualmente grave tratar todo hífen como união obrigatória (regra cega na direção inversa). **Nenhuma das duas regras cegas é aceitável.** Um erro metodológico não pode ser corrigido pela introdução de outro erro metodológico de sinal oposto.

Em vez disso, todo composto com hífen que ocorra em `texto_completo` deve passar por uma análise individual, explícita e justificada, decidindo entre duas alternativas:

- **(a) Manter unido como token único** — quando o composto denota um conceito técnico, político ou de governança com identidade própria, mais específico do que a soma de suas partes (ex.: "decision-making", "data-driven", "human-computer", "AI-driven", "non-discrimination", "cross-border"), ou quando separá-lo faria uma das partes (ou ambas) colidir, sob a mesma forma solta, com usos de sentido diferente já presentes no texto — o que introduziria polissemia não desambiguada na contagem da palavra solta (ver item 5, abaixo). Esse é o critério que deve prevalecer sempre que houver dúvida razoável, dado o risco documentado de que a fragmentação, historicamente, inflou termos genéricos com ocorrências de sentido não relacionado.
- **(b) Separar em suas palavras componentes** — apenas quando ambas as partes, isoladas, preservam exatamente o mesmo sentido genérico que têm em outros usos já soltos no texto, e a separação não introduz mistura de sentidos nem perda de um conceito próprio nomeado pelo composto. Esse caso deve ser a exceção, não a regra-padrão, e deve ser justificado da mesma forma que qualquer outra decisão de normalização.

Essa decisão deve ser tomada **para cada forma hifenizada relevante identificada no texto** (não apenas para 1-2 casos escolhidos à mão) e registrada de forma auditável, com a frequência de cada forma e a justificativa da escolha (a) ou (b), no registro persistente (item 7, abaixo).

### 5. Desambiguação contextual de termos polissêmicos e homônimos

Antes de fechar a contagem de qualquer termo que entre no corte final (item 6), é obrigatório verificar, a partir do contexto real de cada ocorrência no texto (concordância — a janela de palavras ao redor de cada ocorrência), se esse termo designa mais de um referente distinto. Grafias idênticas ou quase idênticas não implicam necessariamente o mesmo conceito. Exemplos já identificados neste projeto:
- "AI" (tecnologia/campo genérico) vs. "AI+" (nome próprio de uma iniciativa/política específica, quando o documento usar esse rótulo);
- "state"/"states" (unidade subnacional, ex.: "a state's AI regulatory climate") vs. "United States"/"State" enquanto parte do nome do país;
- "generation" enquanto geração de energia/eletricidade (ex.: "power generation", "energy generation") vs. "generation" enquanto geração tecnológica/etária (ex.: "new generation of AI", "next-generation technology") — sentidos que **não podem** ser somados sob um único rótulo;
- "power" enquanto capacidade computacional (ex.: "computing power") vs. poder político/geopolítico vs. energia elétrica — três referentes possíveis sob a mesma grafia.

Sempre que um termo candidato ao corte final apresentar mais de um referente no texto analisado, ele deve ser **desdobrado em rótulos distintos por sentido** (ex.: "generation (energia)" e "generation (tecnológica)"), cada um com sua própria contagem, em vez de manter uma única contagem somada que mistura sentidos incompatíveis — mesmo que isso signifique que nenhum dos sentidos isolados atinja, sozinho, o critério de corte. Somar sentidos distintos sob o mesmo rótulo é o mesmo tipo de erro metodológico da fragmentação indevida de compostos (item 4): em ambos os casos, o número final deixa de corresponder a um conceito único e coerente.

**Princípio geral de não fusão de quase-sinônimos:** da mesma forma, itens lexicais diferentes que pertencem ao mesmo campo semântico mas são palavras distintas (ex.: "smart" e "intelligent"; "security" e "safety") nunca devem ser fundidos sob um rótulo comum, ainda que sejam próximos em sentido — apenas variantes do mesmo lema (flexão, sigla/forma por extenso, maiúscula/minúscula) podem ser agrupadas, conforme já estabelecido no item 3.

### 6. Critério de corte

Definir e declarar explicitamente o critério utilizado para selecionar quais termos entram na visualização final. O critério de corte padrão desta skill é o **Top 50** termos por frequência (podendo o gráfico de Top 25 ser mantido como recorte adicional dentro do mesmo Top 50, mas não como critério de corte único) — um corte maior é necessário para captar as especificidades vocabulares próprias de cada documento, que um corte de apenas 25 termos tende a omitir. O critério deve ser consistente ao longo de uma mesma análise e informado ao usuário junto com o restante da metodologia.

**Cobertura da normalização morfológica sob o corte de Top 50.** Um corte mais profundo (Top 50) só é metodologicamente válido se a normalização morfológica (item 3-b) for aplicada de forma sistemática a todo o universo de candidatos que disputam essas 50 posições — não apenas aos pares que "por acaso" já apareciam nas posições mais altas de um corte de Top 25. Isso significa levantar exaustivamente, entre os termos candidatos (ex.: os 100-150 tokens mais frequentes antes do corte), todas as famílias de variantes morfológicas (singular/plural, conjugações verbais, grafias) e decidir o agrupamento de cada uma, exatamente como já exigido no item 3 — a exigência aqui é de **cobertura proporcional ao tamanho do corte**, não uma regra nova. Deixar de fazer essa varredura ampliada e aplicar ao Top 50 os mesmos agrupamentos, já levantados apenas para o Top 25, é um erro metodológico: abre espaço para que variantes não normalizadas do mesmo lema ocupem posições distintas do ranking apenas por não terem sido conferidas.

### 7. Transparência obrigatória com o usuário

A cada análise de vocabulário realizada, deve-se informar ao usuário, de forma explícita:
- Quais palavras/termos foram retirados e por quê (justificativa linguística/metodológica de cada exclusão);
- Quais variantes foram agrupadas e sob qual termo representativo;
- Quais bigramas/compostos (com ou sem hífen) foram tratados como unidade única, e por quê;
- Quais formas hifenizadas foram identificadas no texto, e para cada uma, se foi mantida unida ou separada, com a justificativa individual (item 4);
- Quais termos foram desdobrados por sentido/referente (desambiguação contextual, item 5), e a contagem de cada sentido separadamente;
- Qual foi o critério de corte utilizado para os termos que entraram no gráfico.

**Salvaguarda contra viés de confirmação:** o critério de remoção ou agrupamento de um termo deve ser sempre linguístico ou metodológico — nunca baseado em o termo favorecer ou contrariar alguma conclusão, narrativa ou expectativa sobre o resultado da análise. Remover um termo porque ele "atrapalha o argumento" em vez de "atrapalha metodologicamente" é uma violação do rigor acadêmico exigido neste trabalho.

### 8. Registro persistente e atualizável por documento

Para cada JSON analisado sob esta skill, deve ser mantido um registro persistente na mesma pasta do país (ex.: `notebooks/Análise Documentos IA/Brasil/`), associado ao documento de origem, contendo:
- Lista de termos removidos e a justificativa de cada remoção;
- Lista de agrupamentos de variantes e o termo representativo de cada grupo;
- Lista de bigramas/compostos (com ou sem hífen) tratados como unidade única, com a justificativa de cada um;
- Auditoria completa das formas hifenizadas identificadas no texto: cada forma, sua frequência, e a decisão (mantida unida ou separada) com justificativa individual (item 4);
- Lista de termos desdobrados por desambiguação contextual (item 5), com os sentidos identificados e a contagem de cada um;
- Critério de corte aplicado (Top 50, com Top 25 como recorte interno);
- Data da última atualização.

Esse registro deve ser **lido antes de qualquer nova visualização de vocabulário** sobre o mesmo documento, para manter consistência metodológica entre gráficos diferentes construídos ao longo do tempo. Sempre que o usuário pedir a remoção de novas palavras, esse registro deve ser **atualizado de forma cumulativa** (mantendo as decisões anteriores, salvo se o usuário pedir para reverter alguma delas), e a descrição apresentada ao usuário deve refletir o estado mais atual da lista.

### 9. Construção do gráfico

Construir a visualização gráfica solicitada pelo usuário com base no vocabulário já tratado (após remoção e normalização), sem tipo de gráfico fixo predefinido — o formato depende exclusivamente do que for demandado.

### 10. Análise final obrigatória

Toda visualização de vocabulário produzida por esta skill deve ser acompanhada de uma análise final contendo:
- A metodologia aplicada (idioma identificado, critério de remoção, critério de agrupamento, tratamento de bigramas/hífens, desambiguação contextual, critério de corte);
- A lista atualizada de palavras retiradas e de variantes agrupadas;
- A lista de compostos/bigramas preservados como unidade e das formas hifenizadas mantidas unidas ou separadas, com justificativa;
- A lista de termos desdobrados por sentido e a contagem de cada sentido;
- O que o gráfico mostra e como interpretá-lo;
- Ajustes possíveis para melhorar a visualização;
- Limitações, imprecisões remanescentes ou fraquezas metodológicas do gráfico, se existirem.

## Resultado esperado

Gráficos de vocabulário fiéis ao conteúdo do documento analisado, construídos com critérios de exclusão e normalização de termos explícitos, justificados, auditáveis e reprodutíveis, livres de vieses narrativos, e sempre acompanhados da metodologia e da interpretação exigidas pela Skill02.
