numeros = []
lista_pares = []
total_pares = 0
contador = 0

while contador < 3:
    numeros.append(int(input("Digite um numero: ")))
    contador += 1

for i in numeros:
    if i % 2 == 0:
        lista_pares.append(i)
        total_pares += 1

print(f"Numeros pares digitados: {lista_pares} \nTotal de numeros pares: {total_pares}")