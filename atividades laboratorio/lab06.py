###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: Mateus Henrique Silva Araújo   
# RA: 184940
###################################################

# Leitura de dados
n= int(input())
valorações=[float(input()) for i in range(1,n+1)]
k= int(input())
q= float(input())
# Escolha da melhor variação de valores da ação
listalucro=[0]
valorações1= valorações.copy()
valorações2= valorações.copy()
for a in valorações1:
    for b in valorações1:
        if a<=b and valorações1.index(b) - valorações1.index(a) <= k and valorações1.index(a) <= valorações1.index(b) :
            qtec= q//a
            custo= a*qtec
            venda= b*qtec
            lucrodia= venda - custo
            listalucro.append(lucrodia)
    if valorações.count(a)!= 1:
      valorações1.remove(a)


lucro= max(listalucro)
parapeloamordedeus= False
for c in valorações2:
    for d in valorações2:
        if c<=d and 0<= valorações2.index(d) - valorações2.index(c) <= k and valorações2.index(c) <= valorações2.index(d)  :
            qtde= q//c
            custo= c*qtde
            venda= d*qtde
            lucrodia= venda - custo
            if lucrodia == lucro and valorações2.index(c)!=valorações2.index(d):
                dia_compra = valorações2.index(c)+1
                valor_compra = c
                dia_venda = valorações2.index(d)+1
                valor_venda = d
                qtde_acoes = int(qtde)
            elif lucrodia == lucro:
                dia_compra = valorações2.index(c)+1
                valor_compra = c
                dia_venda = valorações2.index(d)+1
                valor_venda = d
                qtde_acoes = int(qtde)
                parapeloamordedeus=True
            if valorações2.count(c)!=1:
                valorações2.remove(c)
                valorações2.insert(0,999999)
    if parapeloamordedeus == True:
        break

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))
