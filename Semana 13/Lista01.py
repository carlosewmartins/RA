lista_num = [1,2,3,4,5,6]

def soma_elementos(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(soma_elementos(lista_num))
