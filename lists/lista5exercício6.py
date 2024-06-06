def desvioPadrao(v):
    ldi2n=[]
    média=(sum(v)/len(v))

    for i in v:
        di2= (i - média)**2
        ldi2n.append(di2)

    despad= (sum(ldi2n)/(len(v)-1))**(1/2)
    return despad