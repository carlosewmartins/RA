numeros = [2,6,18,42,56,8,104,86]
print(numeros)

try:
    numero1 = int(input("Digite a posição de um numero: "))
    numero1 = numeros[numero1 - 1]

    numero2 = int(input("Digite a posição de outro numero: "))
    numero2 = numeros[numero2 - 1]

    print(numero1 + numero2)

except IndexError:
    print("Posição invalida")
