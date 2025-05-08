idades = []
total_idade = 0
idade = int(input('Digite uma idade: '))
while True:
    if idade > 0:
        idades.append(idade)
        idade = int(input('Digite uma idade (ou digite 0 para parar): '))
    else:
        break

for i in idades:
    total_idade += i

print(idades)
print(f"Média das idades: {total_idade / len(idades)}")