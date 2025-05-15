lista_usuario = []

for i in range(5):
     lista_usuario.append(int(input("Digite o valor a adicionar na lista: ")))

lista_ordenada = sorted(lista_usuario)
lista_inversa = sorted(lista_usuario, reverse=True)

print(f"Lista digitada: {lista_usuario}")
print(f"Lista crescente: {lista_ordenada}")
print(f"Lista decrescente: {lista_inversa}\n")

print(f"Maior numero: {max(lista_usuario)}")
print(f"Menor numero: {min(lista_usuario)}")
print(f"Soma dos valores: {sum(lista_usuario)}")
print(f"Tamanho da lista: {len(lista_usuario)}")