n= int(input("digite o número na base decimal que deseja converter para binário: "))
a=n
inteiro=2
lista=["1"]
if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    while inteiro != 1:
        inteiro = n//2
        resto = str(n%2)
        n = inteiro
        lista.insert(1,resto)
    resultado= "".join(lista)
    print(a, "em binário é", resultado)