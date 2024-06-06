qtdn= int(input("Digite a quantidade de números que devem ser lidos: "))
i=0
intervalo1=[]
intervalo2=[]
intervalo3=[]
intervalo4=[]
while i < qtdn :
    n= int(input("Digite os componentes n: "))
    if n < 0: 
        a=0
    elif n <= 25:
        intervalo1.append(n)
    elif n <= 50:
        intervalo2.append(n)
    elif n <= 75:
        intervalo3.append(n)
    elif n <= 100:
        intervalo4.append(n)
    i=i+1
print("[0,25]:", len(intervalo1))
print("[26,50]:", len(intervalo2))
print("[51,75]:", len(intervalo3))
print("[76,100]:", len(intervalo4)) 