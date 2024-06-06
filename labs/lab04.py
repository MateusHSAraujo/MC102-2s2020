###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Mateus Henrique Silva Araujo  
# RA: 184940
###################################################

# Leitura do hp dos lutadores
hpryu= int(input())
hpken= int(input())
contadorryu=0
contadorken=0
# Leitura da sequência de golpes
while hpryu > 0 and hpken > 0:
    golpe=int(input())
    if golpe > 0:
        hpken = hpken - golpe
        print("RYU APLICOU UM GOLPE:", golpe)
        contadorryu= contadorryu + 1
    else:
        hpryu= hpryu + golpe
        print("KEN APLICOU UM GOLPE:", (-golpe))
        contadorken= contadorken + 1
    if hpryu >= 0:
        print("HP RYU =", hpryu)
    else:
        print("HP RYU = 0")
    if hpken >=0:
        print("HP KEN =", hpken)
    else:
        print("HP KEN = 0")
# Impressão do vencedor e do número de golpes aplicados
if hpryu <=0:
    print("LUTADOR VENCEDOR: KEN")
else:
    print("LUTADOR VENCEDOR: RYU")
print("GOLPES RYU =", contadorryu )
print("GOLPES KEN =", contadorken )












