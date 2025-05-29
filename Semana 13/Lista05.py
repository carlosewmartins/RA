def menu():
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - SAIR")

    opcao = int(input("Que função deseja utilizar: "))
    match opcao:
        case 1:
            num1 = float(input("Digite o 1° numero: "))
            num2 = float(input("Digite o 2° numero: "))
            print(f"{num1} + {num2} = {somar(num1,num2)}")
        case 2:
            num1 = float(input("Digite o 1° numero: "))
            num2 = float(input("Digite o 2° numero: "))
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        case 3:
            num1 = float(input("Digite o 1° numero: "))
            num2 = float(input("Digite o 2° numero: "))
            print(f"{num1} x {num2} = {multiplicar(num1, num2)}")
        case 4:
            num1 = float(input("Digite o 1° numero: "))
            num2 = float(input("Digite o 2° numero: "))
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        case 5:
            print("Saindo do programa...")
        case _:
            print("Opção inválida")

def somar(a,b):
     return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

if __name__ == "__main__":
    menu()