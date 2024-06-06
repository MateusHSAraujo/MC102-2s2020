###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada em todas as direções (norte, sul, leste, oeste,
nordeste, sudeste, noroeste e sudoeste) a partir da posição inicial.

Caso a palavra seja encontrada a partir da posição inicial a função
deve retornar o valor True. Caso contrário, a função de retornar o
valor False.
"""
def busca_palavra(matriz,palavra,i,j):
    if i<0 or j<0 or i>=len(matriz) or j>=len(matriz[0]):
        return False
    else:
        if matriz[i][j] == palavra[0]:
            if len(palavra)==1:
                return True
            else:
                if busca_palavra(matriz,palavra[1:],i-1,j-1) or busca_palavra(matriz,palavra[1:],i-1,j) or busca_palavra(matriz,palavra[1:],i-1,j+1) or busca_palavra(matriz,palavra[1:],i,j-1) or busca_palavra(matriz,palavra[1:],i,j+1) or busca_palavra(matriz,palavra[1:],i+1,j-1) or busca_palavra(matriz,palavra[1:],i+1,j) or busca_palavra(matriz,palavra[1:],i+1,j+1):
                    return True
                else:
                    return False
        else:
            return False




# Leitura da matriz

matriz=[]
ce= True

while ce:
  linha = input()
  if linha.isdigit():
      n=int(linha)
      break
  linhamatriz= linha.split()
  matriz.append(linhamatriz)


# Leitura das palavras

lpalavras=[input() for i in range(n)]
lpalavras.sort()



# Processamento da busca na matriz e impressão, por palavra,
# das posições iniciais (linha e coluna)

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")


for palavra in lpalavras:
    posições=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if busca_palavra(matriz,palavra,i,j):
                posições.append((i+1,j+1))
    print("Palavra:", palavra)
    print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posições])).strip())
    print(40 * "-")













