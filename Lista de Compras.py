compras=[]
print("Digite a lista de compras, digite fim para sair.")
while True:
    produto=input("Produto:")
    if produto=="fim" or produto=="FIM":
        break
    quantidade=int(input("Quantidade:"))
    preco=float(input("Preço:"))
    compras.append([produto,quantidade,preco])#Adiciona uma lista dentro da outra lista
soma=0.0
for e in compras:
    print("%20s x%d R$%6.2f --> Total: R$%6.2f."%(e[0],e[1],e[2],(e[1]*e[2])))
    soma=soma+e[1]*e[2]
print(">>>Total da compra: %7.2f.<<<"%soma)
