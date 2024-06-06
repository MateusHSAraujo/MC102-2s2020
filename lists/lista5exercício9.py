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


def verificaestradaschegamasnaosai(mat):
    matt=transpormatriz(mat)
    temestradaschegando=[]
    naotemestradasaindo=[]
    for linhat in matt:
        if sum(linhat) != 0:
            temestradaschegando.append(1)
        else:
            temestradaschegando.append(0)
    for linha in mat:
        if sum(linha) != 0:
            naotemestradasaindo.append(0)
        else:
            naotemestradasaindo.append(1)
    resposta=[]
    for a in range(len(mat)):
        for b in range(len(mat)):
            if a==b:
                if temestradaschegando[a] + naotemestradasaindo[a]==2:
                    resposta.append(True)
                else:
                    resposta.append(False)
    return resposta

def verificaestradassaimasnaochega(mat):
    matt=transpormatriz(mat)
    naotemestradaschegando=[]
    temestradasaindo=[]
    for linhat in matt:
        if sum(linhat) != 0:
            naotemestradaschegando.append(0)
        else:
            naotemestradaschegando.append(1)
    for linha in mat:
        if sum(linha) != 0:
            temestradasaindo.append(1)
        else:
            temestradasaindo.append(0)
    resposta=[]
    for a in range(len(mat)):
        for b in range(len(mat)):
            if a==b:
                if naotemestradaschegando[a] + temestradasaindo[a]==2:
                    resposta.append(True)
                else:
                    resposta.append(False)
    return resposta   

def verificacidadeisolada(mat):
    matt=transpormatriz(mat)
    naotemestradaschegando=[]
    naotemestradasaindo=[]
    for linhat in matt:
        if sum(linhat) != 0:
            naotemestradaschegando.append(0)
        else:
            naotemestradaschegando.append(1)
    for linha in mat:
        if sum(linha) != 0:
            naotemestradasaindo.append(0)
        else:
            naotemestradasaindo.append(1)
    resposta=[]
    for a in range(len(mat)):
        for b in range(len(mat)):
            if a==b:
                if naotemestradaschegando[a] + naotemestradasaindo[a]==2:
                    resposta.append(True)
                else:
                    resposta.append(False)
    return resposta   
