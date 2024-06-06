def menor_base_log(n):
    b=2
    k=1
    while b<n:
        valor= b**k
        if valor < n:
            k+=1
        if valor > n:
            b+=1
            k=1
        if valor == n:
            return b
    return b


        