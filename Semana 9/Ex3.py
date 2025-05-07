numeros = []
resultados = []
contador = 0

while contador < 10:
    numeros.append(int(input("Digite um numero: ")))
    contador += 1

for i in numeros:
    i = i ** 2
    resultados.append(i)

print(numeros)
print(resultados)