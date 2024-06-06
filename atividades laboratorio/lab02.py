###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# Leitura de dados
x=int(input())
t=int(input())
v_1=float(input())
v_2=float(input())

# Cálculo dos tempos de viagem
th= t/60
T1= (x-(v_1*th))/v_1
T2= x/v_2


# Impressão da resposta
if T2>T1 :
    print(True)
else:
    print(False)
