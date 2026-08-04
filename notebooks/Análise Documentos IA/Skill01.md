# Skill01 – Extração Integral de Texto de Documentos

## Objetivo

Esta skill constitui o **Passo 01** do fluxo de trabalho de análise de documentos sobre inteligência artificial. Sua função é, mediante comando de extração de texto, localizar o documento ou site indicado, extrair a totalidade do seu conteúdo textual relevante e registrar essa extração em formato JSON, dentro da subpasta correspondente ao país ou bloco de origem do documento.

## Princípio de rigor acadêmico

Este trabalho integra uma pesquisa acadêmica séria e deve ser conduzido com o mais alto grau de rigor e perfeccionismo metodológico. Não são aceitáveis:

- Generalizações de qualquer tipo sobre o conteúdo do documento;
- Erros metodológicos graves, sejam eles de extração, classificação ou organização dos dados;
- Simplificações do texto original, sob qualquer justificativa de concisão ou clareza;
- Omissão de trechos por julgamento de relevância pessoal — a decisão sobre o que é substância do texto e o que é material acessório segue apenas os critérios objetivos descritos abaixo, nunca a impressão subjetiva de quem executa a extração;
- Adição de conteúdo, interpretação, resumo ou complemento que não exista literalmente no documento original.

A fidelidade integral ao texto-fonte é o critério inegociável de qualidade desta etapa.

## Regra geral de escopo

Toda atividade realizada no âmbito desta skill deve se restringir **exclusivamente** ao conteúdo da pasta `notebooks/Análise Documentos IA` e de suas subpastas (`Brasil`, `China`, `Estados Unidos`, `Europa`, `Índia`, `Análise Conjunta`).

- Não utilizar como referência, exemplo, padrão ou fonte de dados qualquer material, script, notebook ou documento localizado fora dessa pasta.
- Cada execução desta skill deve considerar apenas os documentos e arquivos já existentes dentro de "Análise Documentos IA".
- Essa restrição vale tanto para leitura de contexto quanto para gravação de resultados: nada deve ser lido de, nem escrito em, pastas fora de "Análise Documentos IA" durante a execução desta skill.

## Gatilho

Esta skill é executada sempre que o usuário emitir um comando de extração de texto de um documento (PDF, DOCX, HTML, etc.) ou de um site indicado, no contexto da pasta "Análise Documentos IA".

## Processo de execução

1. **Localizar o documento ou site indicado** pelo usuário.

2. **Identificar o país ou bloco de origem** do documento, entre as cinco categorias já estruturadas na pasta:
   - Brasil
   - China
   - Estados Unidos
   - Europa
   - Índia

   A identificação deve ser feita com base em critérios objetivos e verificáveis: instituição emissora, órgão governamental responsável, idioma original, domínio/URL de publicação, ou indicação explícita no próprio documento. Em caso de dúvida real sobre a origem, perguntar ao usuário antes de prosseguir — nunca assumir.

3. **Extrair a totalidade do corpo do texto**, de forma integral, literal e fiel ao original, sem paráfrase. Isso inclui todo o conteúdo textual que constitui a substância argumentativa, descritiva, normativa ou analítica do documento: título, subtítulos, corpo de todos os capítulos/seções, tabelas com conteúdo textual relevante, listas e anexos com conteúdo substantivo.

4. **Descartar exclusivamente os elementos que não contribuem para a análise acadêmica do conteúdo**, especificamente:
   - Notas de rodapé;
   - Referências bibliográficas ao final do documento, de cada capítulo ou de cada página;
   - Páginas iniciais que não tratam do conteúdo do texto (capa, folha de rosto, ficha catalográfica, sumário/índice, lista de figuras/tabelas, agradecimentos, prefácios puramente protocolares);
   - Cabeçalhos e rodapés repetitivos de paginação (numeração de página, nome do documento repetido em cada página);
   - Elementos de navegação de páginas web (menus, banners, links de compartilhamento, propaganda, avisos de cookies) quando o documento for extraído de um site.

   Nenhum outro tipo de conteúdo deve ser descartado. Em caso de dúvida sobre se um trecho é substância do texto ou material acessório, o trecho deve ser **mantido**, nunca descartado — o critério é sempre conservador, em favor da integralidade.

5. **Registrar a extração em um arquivo JSON**, salvo dentro da subpasta correspondente ao país/bloco identificado (ex.: `notebooks/Análise Documentos IA/Brasil/`), com nome descritivo do documento de origem.

## Estrutura do JSON de saída

Cada extração deve gerar um arquivo JSON contendo, no mínimo, os seguintes campos:

```json
{
  "titulo": "Título exato do documento, como consta na fonte",
  "pais_ou_bloco": "Brasil | China | Estados Unidos | Europa | Índia",
  "fonte": "URL ou caminho do arquivo original",
  "data_publicacao": "Data de publicação do documento, se disponível, ou null",
  "data_extracao": "Data em que a extração foi realizada (AAAA-MM-DD)",
  "elementos_descartados": [
    "Lista descritiva de tudo o que foi removido e por quê, ex.: 'notas de rodapé (12 ocorrências)', 'sumário (p.1-2)', 'referências bibliográficas finais'"
  ],
  "texto_completo": "Transcrição integral, literal e original de todo o corpo do texto mantido, preservando a ordem e a estrutura (títulos, seções, parágrafos) do documento original"
}
```

- O campo `texto_completo` deve conter o texto integral, sem resumos, sem paráfrases, sem correções de estilo e sem tradução (salvo se o próprio comando de extração solicitar tradução de forma explícita).
- O campo `elementos_descartados` existe para garantir rastreabilidade e auditabilidade da extração: todo descarte deve ser justificável e registrado, nunca silencioso.

## Regras absolutas

- Não generalizar o conteúdo do documento.
- Não ocultar nenhuma parte do corpo do texto sem registro correspondente em `elementos_descartados`.
- Não simplificar o texto original.
- Não adicionar conteúdo, interpretação, análise ou complemento que não exista literalmente no documento.
- Não complementar o texto com informações externas ao documento, ainda que verdadeiras ou relevantes.
- Não tomar como referência arquivos, scripts ou dados de fora da pasta "Análise Documentos IA".

## Resultado esperado

Um arquivo JSON, salvo na subpasta correta de "Análise Documentos IA", contendo a extração integral, fiel e original do conteúdo do documento solicitado — pronto para servir de insumo às etapas seguintes de análise acadêmica.
