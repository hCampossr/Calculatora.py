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

operacao_menu = 5
while operacao_menu != 0:
    print(19*"=")
    print(" MENU CALCULADORA")
    print(19*"=")
    print("\n\n Selecione para a operação:\n",
        "1. Somar\n"
        "2. Subtrair\n"
        "3. Multiplicar\n"
        "4. Dividir\n\n"
        
        "0. Sair\n")

    operacao_menu = int(input())
    print(operacao_menu)

    if operacao_menu == 1:
        num1 = float(input("Digite os numeros da soma: "))
        num2 = float(input())
        result = somar(num1, num2)
        print(num1, "+", num2, "=", result)

    elif operacao_menu == 2:
        num1 = float(input("Digite os numeros da subtração: "))
        num2 = float(input())
        result = subtrair(num1, num2)
        print(num1, "-", num2, "=", result)

    elif operacao_menu == 3:
        num1 = float(input("Digite os numeros da multiplicar: "))
        num2 = float(input())
        result = multiplicar(num1, num2)
        print(num1, "x", num2, "=", result)

    elif operacao_menu == 4:
        num1 = float(input("Digite os numeros da dividir: "))
        num2 = float(input())
        result = dividir(num1, num2)
        print(num1, "/", num2, "=", result)
