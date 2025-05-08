texto = input("Digite um texto qualquer: ").lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in texto:
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1

total_vogais = a + e + i + o + u

print(f"Total de vogais no texto: {total_vogais}")
print("Vogais encontradas e suas quantidades:")

if a > 0:
    print(f"a: {a}")
if e > 0:
    print(f"e: {e}")
if i > 0:
    print(f"i: {i}")
if o > 0:
    print(f"o: {o}")
if u > 0:
    print(f"u: {u}")
