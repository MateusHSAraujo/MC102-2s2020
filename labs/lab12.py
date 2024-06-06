###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Filtros de Imagens
# Nome: Mateus Henrique Silva Araujo   
# RA: 184940
###################################################


'''
Função que recebe uma imagem e imprime essa imagem no formato PGM
'''
def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))

'''
Função que retorna a mediana de uma lista. Se o tamanho da lista
for par, a função retorna a parte inteira da média entre os elementos
centrais
'''
def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        #retorna a parte inteira da média entre os elementos centrais
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

''' 
Função que recebe a matriz que representa a imagem original e
retorna a imagem resultante da aplicação do filtro negativo 
'''
def filtro_negativo(imagem):
    linha= len(imagem)
    coluna= len(imagem[0])
    for x in range(linha):
        for y in range(coluna):
            imagem[x][y] = 255 - imagem[x][y]

    return imagem

'''
Função que recebe a matriz que representa a imagem original e 
retorna a imagem resultante da aplicação do filtro da mediana
'''
def filtro_mediana(imagem):
    linha= len(imagem)
    coluna= len(imagem[0])
    imagemresultado=[]
    for i in imagem:
        linhaimagemresultado= i.copy()
        imagemresultado.append(linhaimagemresultado)

    
    for x in range(linha):
        for y in range(coluna):
            listaparamediana=[]
            if (x-1)>= 0:
                if (y-1)>=0:
                    listaparamediana.append(imagem[x-1][y-1])
                if y>=0:
                    listaparamediana.append(imagem[x-1][y])
                if (y+1) < coluna:
                    listaparamediana.append(imagem[x-1][y+1])
            if x >= 0:
                if (y-1)>=0:
                    listaparamediana.append(imagem[x][y-1])
                if y>=0:
                    listaparamediana.append(imagem[x][y])
                if (y+1) < coluna:
                    listaparamediana.append(imagem[x][y+1])           
            if (x+1)< linha:
                if (y-1)>=0:
                    listaparamediana.append(imagem[x+1][y-1])
                if y>=0:
                    listaparamediana.append(imagem[x+1][y])
                if (y+1) < coluna:
                    listaparamediana.append(imagem[x+1][y+1])           
            medianadalista= mediana(listaparamediana)
            imagemresultado[x][y] = medianadalista

    return imagemresultado

'''
Função que recebe três parâmetros: 

imagem: matriz que representa a imagem original
M: matriz núcleo
D: divisor

Essa função retorna a imagem resultante da aplicação de um filtro 
que usa convolução
'''
def convolucao(imagem, M, D):
    linha= len(imagem)
    coluna= len(imagem[0])
    imagemresultado=[ [0 for j in range(coluna-2)] for i in range(linha-2)]

    for x in range(1,linha-1):
        for y in range(1,coluna-1):
            l1= (M[0][0]*imagem[x-1][y-1]) + (M[0][1]*imagem[x-1][y]) + (M[0][2]*imagem[x-1][y+1])
            l2= (M[1][0]*imagem[x][y-1]) + (M[1][1]*imagem[x][y]) + (M[1][2]*imagem[x][y+1])
            l3= (M[2][0]*imagem[x+1][y-1]) + (M[2][1]*imagem[x+1][y]) + (M[2][2]*imagem[x+1][y+1])
            novopixel= (l1+l2+l3)//D
            if novopixel<0:
                novopixel = 0
            if novopixel>255:
                novopixel=255
            imagemresultado[x-1][y-1]= novopixel

    return imagemresultado

# Leitura da entrada

filtro = input()
_ = input() # P2 (linha a ser ignorada)

m, n = [int(x) for x in input().split()]

_ = input() # 255 - linha a ser ignorada

imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

# Aplica o filtro
if filtro == "negativo":
    imagem= filtro_negativo(imagem)
if filtro == "mediana":
    imagem= filtro_mediana(imagem)
if filtro == "blur":
    M=[[1,1,1],[1,1,1],[1,1,1]]
    D=9
    imagem= convolucao(imagem,M,D)
if filtro == "sharpen":
    M=[[0,-1,0],[-1,5,-1],[0,-1,0]]
    D=1
    imagem= convolucao(imagem,M,D)
if filtro == "edge-detect":
    M=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    D=1
    imagem= convolucao(imagem,M,D)
# Imprime a imagem gerada
imprime_imagem(imagem)
