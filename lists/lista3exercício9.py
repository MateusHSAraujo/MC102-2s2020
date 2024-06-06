n= int(input("Digite o tamanho da sequência de números reais:"))
v=[]
ce= True
aviso= False
#Recebendo os números dentro da condição necessária:
while ce == True:
    for i in range(1,n+1):
        compv=int(input("Digite a sequência de números inteiros, maiores que 1: "))
        if compv>1:
            v.append(compv)
            ce= False
        else:
            aviso=True
            ce=True
            break
    if aviso== True:
        print("Você digitou um número menor ou igual a um. O programa reiniciará a leitura dos valores.")
        aviso= False
para=False
dva=[]
dvb=[]
listacoprimitividade=[]
for a in v:
    for b in v:
        
        #Definindo os divisores de cada dois componentes de v:
        for e in range(1,a+1):
            if a%e==0:
                dva.append(e)        
        for f in range(1,b+1):
            if b%f==0:
                dvb.append(f)   
        #Analisando se esses componentes de v apresentam divisores iguais e diferentes de 1:
        for compdva in dva:
            for compdvb in dvb:
                if compdva == compdvb != 1:
                    coprimo= False
                    para=True
                    break
                else:
                    coprimo= True
            if para == True:
                para=False
                break           
       
        if coprimo == True:
            listacoprimitividade.append(1)
        else:
            listacoprimitividade.append(0)
        dva=[]
        dvb=[]
    print(listacoprimitividade)
    listacoprimitividade=[]





        
