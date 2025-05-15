pares = []
impares = []
numeros = []

for i in range (1,11):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

numeros.extend(pares)
numeros.extend(impares)
numeros.sort()
print(numeros)