n= 0
while n <= 5:
    print(" 1-Pizza de Marguerita \n 2-Pizza de Calabreza \n 3-Pizza de Pepperoni \n 4-Pizza Mussarela  \n 5-Sair")
    n= int(input("Escolha o número correspondente a sua opção: "))
    if n == 1:
        print("Você escolheu a opção: ", n,"-Pizza de Marguerita")
    if n == 2:
        print("Você escolheu a opção: ", n,"-Pizza de Calabreza")
    if n == 3:
        print("Você escolheu a opção: ", n,"-Pizza de Pepperoni")
    if n == 4:
        print("Você escolheu a opção: ", n,"-Pizza de Mussarela")
    if n == 5:
        break
    print("Qual será sua próxima pizza: ")
print("Você escolheu sair \n Fim do Programa")