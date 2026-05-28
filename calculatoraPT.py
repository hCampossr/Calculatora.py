import os

def somar(x, y):
    soma = x + y
    return soma

def subtrair(x, y):
    reducao = x - y
    return reducao

def multiplicar(x, y):
    produto = x * y
    return produto

def dividir(x, y):
    quociente = x / y
    return quociente

def voltar():
    input("\nPressione [ENTER] para voltar ao menu")

operacao_menu = 5

while operacao_menu != 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(19*"=")
    print(" MENU CALCULADORA")
    print(19*"=")
    print("\n\n Selecione para a operação:\n"
        "1. Somar\n"
        "2. Subtrair\n"
        "3. Multiplicar\n"
        "4. Dividir\n\n"
        
        "0. Sair\n")

    operacao_menu = int(input())
    print(operacao_menu)

    if operacao_menu == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        num1 = float(input("Digite os numeros da soma: \n\n"))
        num2 = float(input())
        result = somar(num1, num2)
        print(num1, "+", num2, "=", result)
        voltar()

    elif operacao_menu == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        num1 = float(input("Digite os numeros da subtração: \n\n"))
        num2 = float(input())
        result = subtrair(num1, num2)
        print(num1, "-", num2, "=", result)
        voltar()

    elif operacao_menu == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        num1 = float(input("Digite os numeros da multiplicar: \n\n"))
        num2 = float(input())
        result = multiplicar(num1, num2)
        print(num1, "x", num2, "=", result)
        voltar()

    elif operacao_menu == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        num1 = float(input("Digite os numeros da dividir: \n\n"))
        num2 = float(input())
        if num2 != 0:
            result = dividir(num1, num2)
            print(num1, "/", num2, "=", result)
        else:
            print("Divisao invalida. Denominador igual a 0\n")
        voltar()
