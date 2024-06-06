n= int(input("Digite o tamanho da lista: "))
ls=[int(input("Digite os valores da lista: ")) for a in range(1,n+1)]
c=int(input("Digite o valor de C: "))
print("Sabendo o valor C, o programa procurará na lista dois valores de posições diferentes que multiplicados resultam C")
resultados=[]
e=0
nexiste=True
while e<n:
    f=0
    while f<n:
        if f==e:
            break
        produto= ls[e]*ls[f]
        if produto == c:
            nexiste=False
            resultados.append(ls[e])
            resultados.append(ls[f])
        f= f+1
    e=e+1
if nexiste == True:
    print("Lista=",ls)
    print("Resultado: não existem tais números")
else:
    print("Lista=",ls)
    print("Resultado:", end=" ")
    k=0
    l=1
    while l<len(resultados):
        print(resultados[k],"e",resultados[l],end=" ")
        k=k+1
        l=l+1
