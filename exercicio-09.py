# API para obter cotação de moedas


import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda: {moeda} para BRL
        Valor: R$ {float(cotacao['bid']):.2f}
        Máximo: R$ {float(cotacao['high']):.2f}
        Mínimo: R$ {float(cotacao['low']):.2f}
        Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
        """
    except requests.RequestException as e:
        return f"Erro ao obter cotação: {e}"
    except KeyError:
        return "Moeda não encontrada"
    
def main():
        moeda = input("Digite a moeda que deseja conEURsultar ex: USD, EUR, BRL, GBP: ").upper()
        print("\nObtendo cotação...")
        resultado = obter_cotacao(moeda)
        print(resultado)
        
if __name__ == "__main__":
        main()