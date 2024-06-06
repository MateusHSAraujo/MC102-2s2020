n= int(input("Digite o tamanho de sua lista de números: "))
i=0
co=0
while i<n:
    nw = co    
    co= float(input("Digite os números componetes de sua lista: "))
    if nw <= co:
        status = True
    else:
        negativo = False
    i=i+1
if negativo == False :
    print("A lista não está em ordem crescente")
else:
    print("A lista está em ordem crescente")