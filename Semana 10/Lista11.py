tamanho = int(input("Digite o tamanho do vetor: "))
vetorA = []
vetorB = []
vetorC = []
for i in range(tamanho):
    vetorA.append(int(input(f"Digite o valor a adicionar no vetor A: ")))
    vetorB.append(int(input(f"Digite o valor a adicionar no vetor B: ")))

for i in range(tamanho):
    vetorC.append(vetorA[i] + vetorB[i])

print(f"Vetor A: {vetorA}\nVetor B: {vetorB}\nVetor C: {vetorC}")