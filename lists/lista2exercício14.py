
for i in range(1,61):
    for j in range(1,61):
        for k in range(1,61):
            for l in range(1,61):
                for m in range(1,61):
                    for n in range(1,61):
                        condi= i%2 #par
                        condj= j%2 #ímpar
                        condk= k%2 #par
                        condl= l%2 #ímpar
                        condm= m%2 #par
                        condn= n%2 #ímpar
                        if condi == 0 and condj == 1 and condk == 0 and condl == 1 and condm == 0 and condn == 1 and i<j<k<l<m<n:
                            print(i,j,k,l,m,n)

#código complexo demais para meu computadorzinho rodar