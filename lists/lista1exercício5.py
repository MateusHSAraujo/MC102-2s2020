a= float(input("Digite o valor do lado a: "))
b= float(input("Digite o valor do lado b: "))
c= float(input("Digite o valor do lado c: "))

if (a == b == c):
    print("Esse triângulo é equilátero")
elif (a == b) or (b == c) or (a == c):
    print("Esse triângulo é isóceles")
else:
    print("Esse triângulo é escaleno")

s= (a+b+c)*(1/2)
heron=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("Esse triângulo tem área igual a: ", heron)