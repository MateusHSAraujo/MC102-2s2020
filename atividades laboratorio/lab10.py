###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na horizontal (da esquerda para direita) a partir da
posição inicial.  Caso a palavra seja encontrada a partir da posição
inicial a função deve transformar todas as letras da palavra em
maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.
"""
def horizontal(matriz, linha, coluna, palavra):
  palavraemlista=list(palavra)
  j=coluna
  for letra in palavraemlista:
    if j > len(matriz[0])-1:
      return False
    if matriz[linha][j] != letra and matriz[linha][j] != "*" and matriz[linha][j] != letra.upper():
      return False
    j+=1
  for a in palavraemlista:
    matriz[linha][coluna]=matriz[linha][coluna].upper()
    coluna+=1
  return True


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na vertical (de cima para baixo) a partir da posição
inicial.  Caso a palavra seja encontrada a partir da posição inicial a
função deve transformar todas as letras da palavra em maiúsculas e
retornar o valor True. Caso contrário, a função de retornar o valor
False.
"""
def vertical(matriz, linha, coluna, palavra):
  palavraemlista=list(palavra)
  i=linha
  for letra in palavraemlista:
    if i > len(matriz)-1:
      return False
    if matriz[i][coluna] != letra and matriz[i][coluna] != "*" and matriz[i][coluna] != letra.upper():
      return False
    i+=1
  for a in palavraemlista:
    matriz[linha][coluna]=matriz[linha][coluna].upper()
    linha+=1
  return True


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na diagonal (no sentido inferior direito) a partir da
posição inicial.  Caso a palavra seja encontrada a partir da posição
inicial a função deve transformar todas as letras da palavra em
maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.
"""
def diagonal1(matriz, linha, coluna, palavra):
  palavraemlista=list(palavra)
  i=linha
  j=coluna
  for letra in palavraemlista:
    if i > len(matriz)-1:
      return False
    if j > len(matriz[0])-1:
      return False
    if matriz[i][j] != letra and matriz[i][j] != "*" and matriz[i][j] != letra.upper():
      return False
    i-=1
    j+=1
  for a in palavraemlista:
    matriz[linha][coluna]=matriz[linha][coluna].upper()
    linha-=1
    coluna+=1
  return True



"""
Esta função recebe como parâmetro uma matriz, uma posição inicial
na matriz determinada pelos parâmetros linha e coluna e uma palavra
que deve ser buscada na diagonal (sentido superior direito) a partir
da posição inicial.  Caso a palavra seja encontrada a partir da
posição inicial a função deve transformar todas as letras da palavra
em maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.

"""
def diagonal2(matriz, linha, coluna, palavra):
  palavraemlista=list(palavra)
  i=linha
  j=coluna
  for letra in palavraemlista:
    if i > len(matriz)-1:
      return False
    if j > len(matriz[0])-1:
      return False
    if matriz[i][j] != letra and matriz[i][j] != "*" and matriz[i][j] != letra.upper():
      return False
    i+=1
    j+=1
  for a in palavraemlista:
    matriz[linha][coluna]=matriz[linha][coluna].upper()
    linha+=1
    coluna+=1
  return True


# Leitura da matriz

matriz = []
ce= True

while ce:
  linha = input()
  if linha.isdigit():
      n=int(linha)
      break
  linhamatriz= linha.split()
  matriz.append(linhamatriz)

# Dica: use linha.isdigit(), linha.split() e matriz.append()
# para processar a entrada e armazenar a matriz de caracteeres

# Leitura e processamento das palavras
lpalavras=[input() for i in range(n)]

print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

ocorrencias=0
for palavra in lpalavras:
  
  print("Palavra:", palavra)
  for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
      if horizontal(matriz,linha,coluna,palavra):
        ocorrencias+=1
      if vertical(matriz,linha,coluna,palavra):
        ocorrencias+=1
      if diagonal1(matriz,linha,coluna,palavra):
        ocorrencias+=1
      if diagonal2(matriz,linha,coluna,palavra):
        ocorrencias+=1
  print("Ocorrencias:", ocorrencias)
  print("-" * 40)
  ocorrencias=0

# Impressão da matriz

for linha in matriz:
  print(" ".join(linha))
