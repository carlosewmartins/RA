numeros = []
contador = 0

while contador < 10:
    numeros.append(int(input("Digite um numero: ")))
    contador += 1

numeros.sort()
print(f"Menor numero: {numeros[0]} \nMaior numero: {numeros[9]}")