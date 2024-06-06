palavra1=input("Digite a primeira palavra: ")
palavra2=input("Digite a segunda palavra: ")
palavra1=palavra1.lower()
palavra2=palavra2.lower()
p1= palavra1
p2= palavra2



for a in p2:
    if p1.find(a) == -1:
        print(palavra2, "não é um anagrama de", palavra1)
        break
    else:
        pos=p1.find(a)
        lp1= list(p1)
        lp1.pop(pos)
        p1="".join(lp1)

if p1 == "":
    print(palavra2,"é um anagrama de", palavra1)





