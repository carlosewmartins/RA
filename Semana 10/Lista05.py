numeros = []
impar = 0
par = 0

for i in range(10):
    numeros.append(int(input('Digite um numero: ')))
    if numeros[i] % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Impares: {impar}")
print(f"Pares: {par}")