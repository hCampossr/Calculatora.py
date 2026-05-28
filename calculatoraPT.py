def somar(x, y):
    soma = x + y
    return soma

def subtrair(x, y):
    reducao = x - y
    return reducao

print(19*"=")
print(" MENU CALCULADORA")
print(19*"=")
print("\n\n Selecione para a operação:\n",
    "1. Somar\n"
    "2. Subtrair\n"
    "3. Multiplicar\n"
    "4. Dividir\n"
    "5. Raiz quadrada\n\n"
    
    "0. Sair\n")

operacao_menu = int(input())
print(operacao_menu)

if operacao_menu == 1:
    num1 = float(input("Digite os numeros da soma: "))
    num2 = float(input())
    result = somar(num1, num2)
    print(num1, "+", num2, "=", result)

if operacao_menu == 2:
    num1 = float(input("Digite os numeros da subtração: "))
    num2 = float(input())
    result = subtrair(num1, num2)
    print(num1, "-", num2, "=", result)