ce=False
while ce==False:
    n= int(input("Digite a quantidade de números da primeira sequência: "))
    print("Lembre-se que a primeira sequência não pode ser maior que a segunda")
    m= int(input("Digite a quantidade de números da segunda sequência: "))
    if n<=m:
        ce=True
l1=[int(input("Digite os valores da primeira sequência: ")) for a in range(1,n+1)]
l2=[int(input("Digite os valores da segunda sequência: ")) for b in range(1,m+1)]
print("Primeira sequência:",l1)
print("Segunda sequência:",l2)
numerodeanalises= (m-n)+1
contador=0
listadeverificaçao=[]
if n == m:
    if l1 == l2:
        print("Resultado: 1")
else:
    while numerodeanalises != 0:
        numerodeanalises = numerodeanalises - 1
        for c in l2[:n]:
            listadeverificaçao.append(c)
        if listadeverificaçao == l1:
            contador= contador+1
        listadeverificaçao=[]
        l2.pop(0)
print("Resultado: ", contador)
