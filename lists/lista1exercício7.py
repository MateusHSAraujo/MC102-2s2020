seletor= input("Digite F para selecionar Fahrenheit ou C para selecionar Celsius: ")
if seletor == "C":
    temp= int(input("Digite a temperatura que deseja converter de celsius pra fahrenheit: "))
    ntemp = 1.8*temp + 32
    print(temp, " celsius é igual a ", ntemp, " fahrenheit")
if seletor == "F":
    temp= int(input("Digite a temperatura que deseja converter de fahrenheit para celsius: "))
    ntemp= (temp - 32)*(1/1.8)
    print(temp, " fahrenheit é igual a ", ntemp, " celsius")
