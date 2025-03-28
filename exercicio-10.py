import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Corrigido erro de sintaxe
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"  # Corrigida a sintaxe dos "\n"
    except requests.RequestException as e:  # Corrigida a exceção
        return f"Erro ao obter usuário: {e}"

def main():
    print("Gerenciando um usuário aleatório...")
    usuario = obter_usuario_aleatorio()
    print(usuario)  # Adicionado para exibir o usuário retornado

if __name__ == "__main__":  # Corrigida a comparação
    main()
