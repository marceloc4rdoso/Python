from pegar_cotacao import pegar_cotacao_atual

with open("Coins\\precos.txt", "r") as arquivo:
    lista_precos = arquivo.read().split("\n")

for linha in lista_precos:
    mercadoria, valor, moeda = linha.split(",")
    cotacao = pegar_cotacao_atual(moeda, "BRL")
    print(f"{mercadoria} tá custando R${float(cotacao) * float(valor):,.2f} hoje")