def sanduiche_primo(n):
    lista1=[]
    listamenorprimo=[]
    condição= False
    númeroescolhido= n
    if n==1:
        return ()
    else:
        for m in range(1, n):
            for i in range(1,m+1):
                if m%i == 0:
                    lista1.append(i)
            if lista1==[1,m]:
                listamenorprimo.append(m)
            lista1=[]
        maiormenorprimo= max(listamenorprimo)
        while condição != True:
            for a in range(1,n+1):
                if n%a == 0:
                    lista1.append(a)
            if lista1==[1,n]:
                if n != númeroescolhido:
                    break
            lista1=[]
            n= n+1
        return (maiormenorprimo,n)    