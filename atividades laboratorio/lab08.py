###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura de dados
L= int(input())
txt=[ input() for i in range(1,L+1) ]
N=int(input())
plv=[ input() for i in range(1,N+1) ]
# Processamento do texto
txtnv=[]
for a in txt:
    a=a.lower()
    a=a.replace(".","")
    a=a.replace(",","")
    a=a.replace(";","")
    a=a.replace(":","")
    a=a.replace("!","")
    a=a.replace("?","")
    txtnv.append(a)
ocorrencia=0
similares=0
# Saída de dados
for palavra in plv:
    print("Palavra buscada:", palavra)
    palavra=palavra.lower()
    for linha in txtnv:
        llinha=linha.split()
        for plvlinha in llinha:
            if palavra in plvlinha:
                if len(palavra)==len(plvlinha):
                    ocorrencia+=1
                else:
                    similares+=1
    print("Ocorrencia:", ocorrencia)
    print("Palavras similares:", similares)
    ocorrencia=0
    similares=0        







