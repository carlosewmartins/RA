notas = [61,87,53,89,100,56,32,77,43,85,70,60,43,69,0]

soma_notas = 0

for nota in notas:
    soma_notas += nota
media = soma_notas / len(notas)

print(f"A media da turma foi: {media:.2f}")
