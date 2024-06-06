n= float(input("Digite o primeiro número: "))
m= float(input("Digite o segundo número: "))
operador= input("Digite '+', '-', '*' ou '/' para selecionar a operação que deseja realizar entre os dois números: ")
if operador == "+":
    result= n+m
elif operador == "-":
    result= n-m
elif operador == "*":
    result= n*m
else:
    result= n/m

print("O resultador é: ", result)
print("Fim do Programa")