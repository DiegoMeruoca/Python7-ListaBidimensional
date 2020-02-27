L=[7,4,3,12,8]
fim=5
while fim>1:#Inicia um Laço de repitição enquanto a variavel fim for maior que 1
    trocou=False#Carrega o controle de troca como falso
    x=0#
    while x<(fim-1):
        if L[x]>L[x+1]:#Testa se O Número(L[x] é maior que o proximo (L[x+1])
            trocou=True#Marca que houve troca
            temp=L[x]#Armazena O número maior no temp (Temporário)
            L[x]=L[x+1]#Armazena o número menor(L[x+1]) no lugar do número maior(L[x])
            L[x+1]=temp#Armazena o número maior que estava reservado na variavel temp na posição do número menor L[x+1]
        x+=1#Adiciona mais um contador no x para poder comparar os proximos dois números da lista
    if not trocou:#Testa se não trocou, caso não tenha trocado nada é pq a lsita ja esta ordenada
        break#Encerra o laço de repetição, pois a lista já está ordenada
    fim-=1#Subtrai um da variavel fim para ir fazendo uma "Contagem regreciva"
for e in L:#Imprime a nova lista
    print(e)

