###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Líquido
# Nome: Mateus Henrique Silva Araújo    
# RA: 184940
###################################################

# Leitura de dados
salario_bruto= float(input())
# Desconto de INSS
if salario_bruto <= 1045 :
    INSS= salario_bruto * 0.075
elif salario_bruto < 2089.60 :
    INSS= salario_bruto * 0.09
elif salario_bruto < 3134.40:
    INSS= salario_bruto * 0.12
elif salario_bruto < 6101.06:
    INSS= salario_bruto * 0.14
else:
    INSS= 6101.06*0.14
sbi= salario_bruto - INSS
# Desconto de IR
if sbi <= 1903.98:
    IR=0.00
elif sbi < 2826.65:
    IR= sbi*0.075 - 142.80
elif sbi < 3751.05:
    IR= sbi*0.15 - 354.80
elif sbi <= 4664.68:
    IR= sbi*0.225 - 636.13
else:
    IR= sbi*0.275 - 869.36

salario_liquido= salario_bruto - INSS - IR
# Saída de dados

print("Bruto: R$", format(salario_bruto, ".2f").replace(".", ","))
print("INSS: R$", format(INSS, ".2f").replace(".", ","))
print("IR: R$", format(IR, ".2f").replace(".", ","))
print("Liquido: R$", format(salario_liquido, ".2f").replace(".", ","))
