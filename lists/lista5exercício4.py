def teste(a,b,n):
    if (a**2)+(b**2) == (n**2):
        return True
    else:
        return False

def pitagórico(n):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if teste(a,b,n):
                return True
    return False
