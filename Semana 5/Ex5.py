numeros = []
tamanho = 10
impar = 0
par = 0

while  len(numeros) < 10:
    num = int(input(f"Digite mais {tamanho} numeros: "))
    tamanho -= 1
    numeros.append(num)

for i in numeros:
    if i % 2 == 0:
        print(f"{i} é par")
        par += 1
    else:
        print(f"{i} é impar")
        impar += 1

print(f"{impar} numeros impares e {par} numeros pares")