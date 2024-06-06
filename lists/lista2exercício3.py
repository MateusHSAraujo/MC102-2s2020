m=int(input("Digite o valor de m: "))
n=int(input("Digite o valor de n: "))

while n != 0:
    a= n
    n= m%n
    m= a

print("O MDC dos dois números é: ", m)