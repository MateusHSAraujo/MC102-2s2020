c= int(input("Digite o valor de C: "))
for x1 in range(0,c+1):
    for x2 in range(0,c+1):
        for x3 in range(0,c+1):
            if x1+x2+x3 == c:
                print("x1=", x1,"x2=", x2, "x3=", x3,"é uma solução para x1+x2+x3=",c)