###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Tabela de Vendas
# Nome: Mateus Henrique Silva Araujo   
# RA: 184940
###################################################
def bubbleSortAlterado(lista):
  n = len(lista)
  for i in range(n - 1, 0, -1):
    aux = True
    for j in range(i):
        if lista[j] > lista[j + 1]:
            aux = False
            (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
    if aux:
      break

def ordenarlinhasporcolunas(matriz,lposprioridade):
    copiamatriz=[]
    for linha in matriz:
        linhacopiamatriz=linha.copy()
        copiamatriz.append(linhacopiamatriz)
    manalise=[]
    for i in range(len(matriz)):
        linhaanalise=[]
        for colunadeprioridade in lposprioridade:
            for j in range(len(matriz[0])):
                if j == colunadeprioridade:
                    linhaanalise.append(matriz[i][j])
        linhaanalise.append(i)
        manalise.append(linhaanalise)

    bubbleSortAlterado(manalise)
    for l in range(len(manalise)):
        copiamatriz[l]= matriz[manalise[l][len(lposprioridade)]]
    
    
    return copiamatriz

# Leitura de dados
N=int(input())
cabeçalho=input()

lcabeçalho=cabeçalho.split(",")

matrizdados=[]
for i in range(N):
        linha= (input()).split(",")
        for i in range(1,len(linha)):
            linha[i]=int(linha[i])
        matrizdados.append(linha)

lprioridade=(input()).split()

lposprioridade=[]
for prioridade in lprioridade:
    posprioridade=lcabeçalho.index(prioridade)
    lposprioridade.append(posprioridade)

# Ordenação dos dados
dados = ordenarlinhasporcolunas(matrizdados,lposprioridade)
dados.insert(0,lcabeçalho)

# Saída dos dados
for linha in dados:
        print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))
