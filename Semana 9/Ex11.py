numeros = [69,55,42,15,75]
menor = min(numeros)
maior = max(numeros)

for i in range(len(numeros)):
    if numeros[i] == menor:
        posicao_menor = i

    if numeros[i] == maior:
        posicao_maior = i

print(f"O maior numero digitado foi {maior}")
print(f"A posicao do maior numero digitado e {posicao_maior}")
print(f"O menor numero digitado foi {menor}")
print(f"A posicao do menor numero digitado e {posicao_menor}")

