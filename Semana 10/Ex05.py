import random
numeros = []
contador = 0
for i in range(10):
    numeros.append(random.randint(0,999))
print(numeros)

numero_usuario = int(input("Informe um numero: "))

for i in numeros:
    if i == numero_usuario:
        print(f"{numero_usuario} ja está na lista.")
        print(f"Posição {contador}.")
    if numero_usuario not in numeros:
        print(f"{numero_usuario} não esta na lista.")
        break
    contador += 1
