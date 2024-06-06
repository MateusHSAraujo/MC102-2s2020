def divisorespróprios(x):
    ldivisores=[]
    for i in range(1,x):
        if x%i==0:
            ldivisores.append(i)
    return ldivisores

def amigos(a,b):
    somadivisoresprópriosdea= sum(divisorespróprios(a))
    somadivisoresprópriosdeb= sum(divisorespróprios(b))
    if somadivisoresprópriosdea == b and somadivisoresprópriosdeb == a:
        return True
    else:
        return False
