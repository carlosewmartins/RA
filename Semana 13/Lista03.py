lista_num = [1,2,3,4,5,6,20,8,9]

def maior_elemento(lista):
    maior = 0
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

print(maior_elemento(lista_num))