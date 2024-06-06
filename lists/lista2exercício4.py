n= int(input("Digite o valor se n: "))
lista1=[]
listamenorprimo=[]
condição= False
númeroescolhido= n
if n==1:
    print("O maior número primo antes 1 é 1 \nO menor número primo depois de 1 é 1")
else:
    for m in range(1, n+1):
        for i in range(1,m+1):
            if m%i == 0:
                lista1.append(i)
        if lista1==[1,m]:
            listamenorprimo.append(m)
        lista1=[]
    maiormenorprimo= max(listamenorprimo)
    print("O maior número primo antes de", n,"é o número", maiormenorprimo)
    while condição != True:
        for a in range(1,n+1):
            if n%a == 0:
                lista1.append(a)
        if lista1==[1,n]:
            break
        lista1=[]
        n= n+1
    print("O menor número primo depois de", númeroescolhido ,"é o número", n)