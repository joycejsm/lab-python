#Desafio

#Criar uma calculadora para realizar operaçoes basicas de matematica

#requisitos

#a operação matematica deve ser relizada entre dois numeros

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação(+ ,- ,* ,/):")

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                resultado = num1 / num2
            else:
                raise ValueError
            print(f"Resultado: {resultado}")
            break 
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitido, tente novamente")

calculadora()