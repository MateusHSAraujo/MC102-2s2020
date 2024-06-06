'''
def temestrada(M,i,j):
    if M[i][j]==1:
        return True
    if M[i][j] == 0:
        return False


def possiveisdestinos(M,i,listacidades=[]):
    listacidades=[list(range(len(M[0])))]
    if temestrada(M,i,listacidades[0]):
        print("Da cidade {} é possível chegar a cidade {}".format(i,listacidades[0]))
    possiveisdestinos(M,i,listacidades[1:])
    
        
M=[[0, 1, 1, 0],[0, 0, 1, 0],[1, 1, 0, 1],[1, 0, 1, 0]]

def verificamatriz(listabi):
    matriz=True
    for linha in listabi:
        if matriz == False:
            break
        for outralinha in listabi:
            if len(linha)!= len(outralinha):
                matriz=False
                break
    if matriz == True:
        linhas= len(listabi)
        colunas= len(listabi[0])
        return (linhas,colunas)
    else:
        return ()

def transpormatriz(matriz):
    mt=[[0 for i in range(len(matriz))] for j in range(len(matriz[0]))]
    (nlinhas,ncolunas)=verificamatriz(matriz)
    for i in range(nlinhas):
        for j in  range(ncolunas):
            valor = matriz[i][j]
            mt[j][i] = valor   
    return mt


def possiveisdestinos(M,i,j=0):
    listacidades=[list(range(len(M[0])))]
    copiaM=[]
    for linha in M:
        nvl=linha.copy()
        copiamatriz.append(nvl)
    if M[i][j]==1:
        print("Da cidade {} é possível chegar a cidade {}".format(i,j))
        Mtemp= transpormatriz(copiaM)
        Mtemp.pop(listacidades[0])
        novaM=transpormatriz(Mtemp)
        possiveisdestinos(novaM,i,j+1)
    else:
'''



def possiveisdestinos(M,i,j=0):
    if j>=len(M[0]):
        return
    else:
        if M[i][j] ==1:
            M[i][j]==0
            for a in range(len(M)):
                for b in range(len(M[0])):
                    if b == j:
                        M[a][b]==0
            print("Da cidade {} é possível chegar a cidade {}".format(i,j))
            possiveisdestinos(M,i,j+1)
            #possiveisdestinos(M,j)
        else:
            possiveisdestinos(M,i,j+1)



M=[[0, 1, 1, 0],[0, 0, 1, 0],[1, 1, 0, 1],[1, 0, 1, 0]]
possiveisdestinos(M,1)


