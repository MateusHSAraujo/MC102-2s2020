def temdivisornointervalo(n,começo,fim):
    if começo > fim:
        return False
    else:
        if n%começo == 0:
            return True
        else:
            return temdivisornointervalo(n,começo+1,fim)

def éprimo(n):
    if temdivisornointervalo(n,2,n-1):
        return False
    else:
        return True



    
