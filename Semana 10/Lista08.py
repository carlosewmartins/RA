numeros = []

for i in range(10):
    num = int(input(f"Digite um numero número: "))
    numeros.append(num)

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Números em ordem crescente:")
for numero in numeros:
    print(numero)
