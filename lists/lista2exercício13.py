n= int(input("Digite o número de linhas e colunas: "))

for i in range(1, n+1):
    print("* "*(i-1),"+ ","* "*(n-i), sep="")