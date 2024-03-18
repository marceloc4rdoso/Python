import requests


def pegar_cotacao_atual(moeda_origem, moeda_destino):
    with open("Coins\\codigos_moedas.txt", "r") as arquivo:
        codigos_moedas = arquivo.read().split("\n")
    if moeda_origem not in codigos_moedas:
        print("Moeda de Origem não encontrada")
    if moeda_destino not in codigos_moedas:
        print("Moeda de Destino não encontrada")
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)
    if requisicao:
        cotacao = requisicao.json()[moeda_origem + moeda_destino]["bid"]
        return cotacao
    else:
        print("Combinação não existente na API")
        return ""


if __name__ == "__main__":
    print(pegar_cotacao_atual("EUR", "BRL"))
    print("lira é doidao")