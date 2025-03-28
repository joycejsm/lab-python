# Desafio

# Criar um programa para calcular o valor da gorjeta no valor total da conta e da porcetagem desejada.

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

total_conta = 100.00
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"O valor da gorjeta é R$ {total_conta:.2f}, a gorjeta de {porcentagem}% é R$ {gorjeta:.2f}")