matriz = []

for i in range(5):
    print(f"Aluno {i+1}:")
    matricula = int(input("Número de matrícula: "))
    media_provas = int(input("Média das provas: "))
    media_trabalhos = int(input("Média dos trabalhos: "))
    nota_final = media_provas + media_trabalhos
    matriz.append([matricula, media_provas, media_trabalhos, nota_final])
    print()

maior_nota = matriz[0][3]
matricula_maior = matriz[0][0]

for aluno in matriz:
    if aluno[3] > maior_nota:
        maior_nota = aluno[3]
        matricula_maior = aluno[0]

print(f"A matrícula do aluno com a maior nota final é: {matricula_maior}")