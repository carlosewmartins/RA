numeros = []

while True:
    num = int(input("Digite um número:"))
    if num > -1:
        numeros.append(num)
    else:
        if numeros:
            media = sum(numeros) / len(numeros)
            print(f"Média: {media}")

        else:
            print("Nenhum número foi inserido.")
        break

print(numeros)

