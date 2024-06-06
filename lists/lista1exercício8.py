ano= int(input("Digite o valor de um ano: "))

if ano%400 == 0:
    print(ano, "é bissexto")
elif ano%4 == 0:
    if ano%100 != 0:
        print(ano, "é bissexto")
    else:
       print(ano, "não é bissexto") 
else:
    print(ano, "não é bissexto")