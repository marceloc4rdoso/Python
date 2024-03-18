produtos = {}
produto = input("Insira um produto: ").title()
while True:
    for produto in produtos:
        produto += 1
        print(type(produtos))  
        produtos['nome']= produto
        print(f"{produto} inserido com sucesso!")
    print(produtos)