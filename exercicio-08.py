#Desafio
# Criador de senha aleatória

import random
import string

def gerar_senha(tamanho):
    # Combina letras, números e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha com o tamanho especificado
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

# Solicita ao usuário o tamanho da senha
try:
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    if tamanho_senha > 0:
        nova_senha = gerar_senha(tamanho_senha)
        print(f"Sua nova senha é: {nova_senha}")
    else:
        print("O tamanho da senha deve ser maior que zero.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
    
    