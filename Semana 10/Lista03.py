num = int(input("Digite um numero de 1 a 10: "))

if num > 10:
    print(f"{num} é maior que 10")
elif num < 1:
    print(f"{num} é menor que 1")
else:
    for i in range(1, 11):
        print(i * num)