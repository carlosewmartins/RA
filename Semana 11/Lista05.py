palavras = ["banana", "maca", "uva", "mamao"]

palavra_longa = max(palavras, key=len)
palavra_curta = min(palavras, key=len)

print(f"A palavra mais longa é: {palavra_longa}")
print(f"A palavra mais curta é: {palavra_curta}")