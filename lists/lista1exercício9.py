print("Esse programa lerá seu sexo, sua idade e seu tempo de contribuição para calcular se você pode se aposentar ou não")
seletor= input("Escolha M se você é do sexo masculino ou F se você é do sexo feminino: ")
id= int(input("Digite sua idade: "))
tc= int(input("Digite seu tempo de contribuição em anos: "))

if seletor == "M":
    if id >= 65:
        if tc >= 10:
            print("Aposentável")
        else:
            print("Não Aposentável")
    elif id >= 63:
        if tc >= 15:
            print("Aposentável")
        else:
            print("Não Aposentável")
    else:
        print("Não Aposentável")
    
if seletor == "F":
    if id >= 63:
        if tc >= 10:
            print("Aposentável")
        else:
            print("Não Aposentável")
    elif id >= 60:
        if tc >= 15:
            print("Aposentável")
        else:
            print("Não Aposentável")
    else:
        print("Não Aposentável")
print("Fim do Programa")