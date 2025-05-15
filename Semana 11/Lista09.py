import random

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(letras)
print(letras)

resposta_correta = random.choice(letras)
resposta_usuario = int(input(f"Em qual posição (índice) a letra '{resposta_correta}' está? "))

if letras[resposta_usuario] == resposta_correta:
    print("Você acertou!")
else:
    print("Você errou!")
