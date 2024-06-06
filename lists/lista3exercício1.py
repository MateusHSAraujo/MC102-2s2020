n=int(input("Digite os tamanho da lista de n: "))
ln=[float(input("Digite os valores da lista: ")) for i in range(1,n+1)]
ldi2n=[]
média=(sum(ln)/n)

for i in ln:
    di2= (i - média)**2
    ldi2n.append(di2)

despad= (sum(ldi2n)/(n-1))**(1/2)
print("O valor do desvio padrão dos dados fornecidos é=", despad)

