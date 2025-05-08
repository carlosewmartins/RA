numeros = []
multiplos = 0
nao_multiplos = 0

for i in range(2):
    numeros.append(int(input('Digite um numero: ')))
    if numeros[i] % 10 == 0:
        multiplos += 1
    else:
        nao_multiplos += 1

print(f"Multiplos de 10: {multiplos}")
print(f"Outros numeros: {nao_multiplos}")