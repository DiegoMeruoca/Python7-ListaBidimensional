produto1=["Maçã",10,0.30]#cria as primeiras listas
produto2=["Pêra",5,0.75]
produto3=["Kiwi",5,0.98]
compras=[produto1,produto2,produto3]#cria a lista de listas
total=0
for e in compras:
    print("\nProduto: ",e[0])
    print("Quantidade: ",e[1])
    print("Preço: ",e[2])
    total=total+(e[1]*e[2])
print("\nO total da compra foi R$",total)
