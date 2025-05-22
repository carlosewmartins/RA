tamanho = 10
matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for linha in matriz:
    print(linha)