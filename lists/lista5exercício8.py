def frequencias(v):
    dicv={}
    lfrequencia=[]
    for elemento in v:
        dicv[v.count(elemento)]= elemento
    for frequencia in dicv.keys():
        lfrequencia.append(frequencia)
    maiorfrequencia= max(lfrequencia)
    menorfrequencia= min(lfrequencia)
    f2= dicv.get(maiorfrequencia)
    f1=dicv.get(menorfrequencia)
    return (f1,f2)
