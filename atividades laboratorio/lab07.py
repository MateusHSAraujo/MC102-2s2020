###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura de dados
n=int(input())
lnotas=[float(input()) for a in range(1,n+1)]
lpesos=[float(input()) for b in range(1,n+1)]



# Cálculo da média ponderada dos laboratórios
c=0
d=0
e=0
lcompmedia=[]
while c<n:
    notaxpeso= lnotas[d]*lpesos[e]
    lcompmedia.append(notaxpeso)
    d=d+1
    e=e+1
    c=c+1
media= sum(lcompmedia)/sum(lpesos)

print("Media laboratorios:", format(media, ".1f").replace(".", ","))
# Verificação da situação do aluno
# Caso o aluno tenha sido aprovado por nota
if media >= 5:
    print("Situacao: Aprovado por nota")
# Caso o aluno tenha sido reprovado por nota
if media < 2.5 :
   print("Situacao: Reprovado por nota")

nota_final=media
# Cálculo da nota do exame, caso o aluno tenha ido para o exame

if 2.5<media<5:
   m=int(input())
   llabexame=[int(input()) for f in range(1,m+1) ]
   lnotasexame=[float(input()) for g in range(1,m+1)]
   h=0
   j=0
   k=0
   lcompmediaexame=[]
   lpesosusados=[]
   while h<m:
       pesosusados=lpesos[llabexame[h]-1]
       lpesosusados.append(pesosusados)
       h=h+1

   while j<m:
       notaxpeso2= lnotasexame[j]*lpesosusados[k]
       lcompmediaexame.append(notaxpeso2)
       j=j+1
       k=k+1
   mediaexame=sum(lcompmediaexame)/sum(lpesosusados)
   nota_final=min(5,(media+mediaexame)/2)

   
   if nota_final>=5:
        # Caso o aluno tenha sido aprovado no exame
        print("Situacao: Aprovado no exame")
   
   if nota_final<5:
        # Caso o aluno tenha sido repravado no exame
        print("Situacao: Reprovado no exame")






# Saída de dados

print("Nota final:", format(nota_final, ".1f").replace(".", ","))
