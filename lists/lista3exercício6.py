n= int(input("Digite o tamanho da primeiro sequência: "))
m= int(input("Digite o tamanho da segundo sequência: "))
l1=[int(input("Digite os valores da primeiro sequência: ")) for a in range(1,n+1)]
l2=[int(input("Digite os valores da segundo sequência: ")) for b in range(1,m+1)]
print("Primeiro sequência:", l1)
print("Segundo sequência:", l2)
luniao= l1+l2
lfinal=[]
numerodeanalises= m+n
while numerodeanalises > 0:
    numerodeanalises= numerodeanalises-1
    for e in luniao:
        if e == min(luniao):
            lfinal.append(e)
            luniao.remove(e)
print("Resultado:",lfinal)