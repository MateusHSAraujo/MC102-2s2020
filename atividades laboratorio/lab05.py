###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura de dados
n1=int(input())
n3=int(input())
n4=int(input())
n6=int(input())

# Impressão dos quatro números fornecidos como entrada

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

# Processamento e impressão da lista de possíveis apostas
print("Lista de apostas:")
for i in range(1,61):
    for m in range(1,61): 
        if n1%2==0:  #n2 precisa ser ímpar e n5 precisa ser par
            if i%2==1 and m%2==0 and n1<i<n3<n4<m<n6 and (n1+i+n3+n4+m+n6)%7!=0 and (n1+i+n3+n4+m+n6)%13!=0:
                n2=i
                n5=m
                print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))
        else: #n2 precisa ser par e n5 precisa ser ímpar
            if i%2==0 and m%2==1 and n1<i<n3<n4<m<n6 and (n1+i+n3+n4+m+n6)%7!=0 and (n1+i+n3+n4+m+n6)%13!=0:
                n2=i
                n5=m
                print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))















