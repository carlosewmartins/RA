numeros = []
contador = 0


while contador < 3:
    numeros.append(int(input("Digite um numero: ")))
    contador += 1

maior = numeros[0]
posicao = 0

for i in range(1,3):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i

print(numeros)
print(f"O maior numero digitado foi {maior}")
print(f"A posicao do numero digitado e {posicao + 1}")