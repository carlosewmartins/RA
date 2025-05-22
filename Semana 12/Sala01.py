import random

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#Printando normalmente
print(matriz)

#Printando matriz com um for
for row in matriz:
    print(row)

#Printando matriz com dois for
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print()
