numeros = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

mais_frequente = 0
maior_contagem = 0

for i in range(len(numeros)):
    contagem = 0
    for j in range(len(numeros)):
        if numeros[j] == numeros[i]:
            contagem += 1

    if contagem > mais_frequente:
        maior_contagem = contagem
        mais_frequente = numeros[i]

print(f"O número que mais se repete é: {mais_frequente}")