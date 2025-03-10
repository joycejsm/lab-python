# print("Hello World!")

fruta = "banana"

print(fruta)

def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao}
    lista.append(pessoa)

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")

    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissao: {pessoa['profissao']}")

pessoas = []

adicionar_pessoa(pessoas, "Ana", 25, "Engenheira")
adicionar_pessoa(pessoas, "Joyce", 28, "Desenvolvedora Web")
adicionar_pessoa(pessoas, "Heitor", 33, "Músico")

exibir_pessoas(pessoas)