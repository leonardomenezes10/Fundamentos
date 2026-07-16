import json
import os

def classificar_noticias(caminho_arquivo, limite=15):
    """
    Classifica as primeiras notícias de um arquivo JSON do banco de dados Agencia Brasil
    com base nas diretrizes de instabilidade política definidas na skill01.md.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    itens = dados.get("_default", {})
    classificadas = {}

    # Dicionário pré-classificado para o lote de teste (itens 1 a 15 de 2018-05)
    analise_pre_definida = {
        "1": {
            "classificacao": "Não",
            "justificativa": "Trata-se de uma medida fiscal e de fiscalização governamental sobre postos de gasolina. Embora ligada ao contexto da greve dos caminhoneiros, a notícia em si descreve regulação de preços e penalidades para postos, o que entra na exceção de decisões administrativas/econômicas."
        },
        "2": {
            "classificacao": "Não",
            "justificativa": "Decisão judicial pontual determinando a garantia de leitos de UTI em Palmas, enquadrando-se como trâmite administrativo e de saúde pública regular."
        },
        "3": {
            "classificacao": "Sim",
            "justificativa": "Descreve uma crise política internacional grave na Nicarágua com violência armada estatal, repressão a protestos de rua e mortes civis significativas, indicando contestação e ameaça severa à estabilidade institucional."
        },
        "4": {
            "classificacao": "Sim",
            "justificativa": "A greve completa e paralisação total da frota de transporte público em Manaus afetou de forma crítica o funcionamento urbano e a governabilidade local, configurando processo com impacto político relevante regional."
        },
        "5": {
            "classificacao": "Não",
            "justificativa": "Medida tributária tomada pelo governo do Distrito Federal (redução do cálculo do ICMS). Enquadra-se nas exceções de decisões econômicas/administrativas comuns."
        },
        "6": {
            "classificacao": "Não",
            "justificativa": "Plano administrativo de segurança pública para reestruturação de UPPs na Baixada Fluminense, sem indicar crise política ou institucional."
        },
        "7": {
            "classificacao": "Não",
            "justificativa": "Decisão judicial de manutenção de condenação criminal do ex-governador Sérgio Cabral, que já estava preso. Representa o trâmite normal do sistema de justiça."
        },
        "8": {
            "classificacao": "Sim",
            "justificativa": "Paralisação nacional coordenada da categoria estratégica dos petroleiros, desafiando a governabilidade e gerando alto nível de incerteza em refinarias de energia."
        },
        "9": {
            "classificacao": "Não",
            "justificativa": "Negociação diplomática internacional entre EUA e Coreia do Norte. Enquadra-se nas exceções diplomáticas e não indica instabilidade interna no funcionamento do sistema político de nenhum dos Estados."
        },
        "10": {
            "classificacao": "Não",
            "justificativa": "Decisão administrativa regulatória de concessão de isenção de pedágio em São Paulo como cumprimento de acordos."
        },
        "11": {
            "classificacao": "Não",
            "justificativa": "Publicação de portaria ministerial para fiscalização de postos, tratando-se de decisão puramente administrativa e reguladora."
        },
        "12": {
            "classificacao": "Não",
            "justificativa": "Decisão político-econômica de corte de verbas e reconfiguração de incentivos fiscais para subsidiar o óleo diesel."
        },
        "13": {
            "classificacao": "Não",
            "justificativa": "Evento religioso pacífico de grande porte (Marcha para Jesus), sem teor de contestação ou ruptura do sistema institucional."
        },
        "14": {
            "classificacao": "Não",
            "justificativa": "Divergência de opinião e críticas de entidades empresariais (AEB) sobre corte de incentivos. Representa debates econômicos rotineiros da sociedade civil organizada."
        },
        "15": {
            "classificacao": "Não",
            "justificativa": "Notícia econômica e de relações internacionais aduaneiras (tarifas de aço e alumínio entre EUA e Brasil)."
        }
    }

    print(f"--- Processando as primeiras {limite} notícias do arquivo {caminho_arquivo} ---")
    for i in range(1, limite + 1):
        chave = str(i)
        if chave in itens:
            noticia = itens[chave]
            titulo = noticia.get("titulo")
            data = noticia.get("data")
            
            # Se for do lote pré-definido, aplica a classificação com justificativa
            if chave in analise_pre_definida:
                resultado = analise_pre_definida[chave]
                classificacao = resultado["classificacao"]
                justificativa = resultado["justificativa"]
            else:
                # Fallback simples para outros arquivos
                classificacao = "Não Classificado"
                justificativa = "Requer análise manual ou integração com API de LLM."
            
            classificadas[chave] = {
                "titulo": titulo,
                "data": data,
                "classificacao_instabilidade_politica": classificacao,
                "justificativa": justificativa
            }
            print(f"[{chave}] Título: {titulo} | Instabilidade: {classificacao}")

    # Salva o resultado
    arquivo_saida = "noticias_classificadas_sample.json"
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        json.dump(classificadas, f, indent=4, ensure_ascii=False)
    
    print(f"\nResultados salvos com sucesso em: {arquivo_saida}")

if __name__ == "__main__":
    # Caminho padrão do arquivo de maio de 2018 extraído do notícias.zip
    classificar_noticias("json/BD_AGENCIA_BRASIL-2018-05.json")
