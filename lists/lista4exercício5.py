palavra1=input("Digite a primeira palavra: ")
palavra2=input("Digite a segunda palavra: ")
palavra1=palavra1.lower()
palavra2=palavra2.lower()

lpalavra1= list(palavra1)
lpalavra2= list(palavra2)
lanalise=[]
lpalavra1intacta=lpalavra1.copy()
i=0
j=0
while i<len(lpalavra1):
    if lpalavra2[j] == lpalavra1[i]:
        objlp1= lpalavra1[i]
        lanalise.append(objlp1)
        i=i+1
        j=j+1
    else:
         j=j+1
    if j>=len(lpalavra2):
        break

if lanalise == lpalavra1intacta:
    print(palavra1,"é subsequente de",palavra2)
else:
    print(palavra1,"não é subsequente de",palavra2)
           
