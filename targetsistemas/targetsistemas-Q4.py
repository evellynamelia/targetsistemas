estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

totalfat = sum(estado.values())
print(f"Faturamento total: R${totalfat:.2f}\n")

for estado, valor in estado.items():
    percentual = (valor / totalfat) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")
