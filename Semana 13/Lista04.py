def contar_caracteres(texto, caractere):
    texto.lower()
    caractere.lower()
    soma = 0
    for i in texto:
        if i == caractere:
            soma += 1

    return soma

print(contar_caracteres("O cachorro correu feliz pelo parque durante a tarde ensolarada", 'a'))


