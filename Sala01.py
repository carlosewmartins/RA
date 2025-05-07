import random

num = []
pares = []
impares = []

for i in range(1,11):
    num.append(random.randint(0,999))

for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Lista: {num}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")

