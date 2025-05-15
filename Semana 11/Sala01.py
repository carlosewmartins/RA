import random
numerosJogador1 = []
numerosJogador2 = []

for i in range(3):
    numerosJogador1.append(random.randint(1,6))
    numerosJogador2.append(random.randint(1,6))

Jogador1 = sum(numerosJogador1)
Jogador2 = sum(numerosJogador2)

print(f"Jogador 1: {Jogador1}\nJogador 2: {Jogador2}\n")

if Jogador1 > Jogador2:
    print("Jogador 1 ganhou!")
else:
    print("Jogador 2 ganhou!")