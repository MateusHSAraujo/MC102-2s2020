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


def solucao(mat):
    matt=transpormatriz(mat)
    for linhat in matt:
        linhatanalise= linhat.copy()
        linhatanalise.sort()
        if linhatanalise != list(range(1,10)):
            return False
    for linha in mat:
        linhaanalise= linha.copy()
        linhaanalise.sort()
        if linhaanalise != list(range(1,10)):
            return False
    for linhat in matt:
        for elemento in linhat:
            if linhat.count(elemento) > 1:
                return False
    for linha in mat:
        for elemento in linha:
            if linha.count(elemento) > 1:
                return False
    return True     