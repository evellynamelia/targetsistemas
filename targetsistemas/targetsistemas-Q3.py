import json

# A empresa foi dada com um faturamento de R$1 bilhão por mês, o json foi construido a partir desses dados! A construção foi feita por IA e coloquei que não tivesse faturamento nos finais de semana.

# Função para calcular os dados do faturamento
def calculofat(dados):
    # Filtro de dias com faturamento maior que 0
    fat = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

    # Calculo de menor e maior faturamento
    menorfat = min(fat)
    maiorfat = max(fat)

    # Calculo de média do faturamento
    mediafat = sum(fat) / len(fat)

    # Dias com faturamento superior à média
    media_dia = len([dia for dia in fat if dia > mediafat])

    return menorfat, maiorfat, media_dia

try:
    with open('faturamento.json', 'r', encoding='utf-8') as file:
        dadosfat = json.load(file)

    menor, maior, media_dia = calculofat(dadosfat)

    # Resultados
    print(f"Menor faturamento: R${menor:}")
    print(f"Maior faturamento: R${maior:}")
    print(f"Número de dias com faturamento acima da média: {media_dia}")

except FileNotFoundError:
    print("O arquivo 'faturamento.json' não foi encontrado. Verifique o caminho e tente novamente.")
except json.JSONDecodeError:
    print("Erro ao ler o arquivo JSON. Verifique a formatação do arquivo.")
