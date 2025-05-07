import random

negativos = []
positivos = []
numeros = []
soma_positivos = 0

for i in range(10):
    numeros.append(random.randint(-255,255))

for i in numeros:
    if i >= 0:
        positivos.append(i)
        soma_positivos += i
    else:
        negativos.append(i)
print(numeros)

print(f"Quantidade de numeros negativos: {len(negativos)}")
print(f"Soma de numeros positivos: {soma_positivos}")