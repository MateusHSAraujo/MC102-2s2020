palavra1=input("Digite a primeira palavra: ")
palavra2=input("Digite a segunda palavra: ")

for i in palavra1:
    for j in palavra2:
        if i == j:
            palavra2= palavra2.replace(i,"")
print("Seu resultado é: ", palavra2)