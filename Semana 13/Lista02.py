numeros = [1,2,3,2,1]
def e_palindromo(lista):
    lista2 = lista.copy()
    lista2.reverse()
    if lista == lista2:
        return True
    else:
        return False

print(e_palindromo(numeros))