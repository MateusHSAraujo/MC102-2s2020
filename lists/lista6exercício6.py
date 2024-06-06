def nemfatordois(n):
    if n ==2:
        return 1
    if n%2!=0:
        return -1
    else:
        if nemfatordois(n/2)<1:
            return -1
        else:
            return 1+nemfatordois(n/2)

def pisolog(n):
    if nemfatordois(n)>=1:
        return nemfatordois(n)
    else:
        return pisolog(n-1)


    
