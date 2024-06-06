###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - De salto em salto
# Nome: Mateus Henrique Silva Araujo	
# RA: 184940
###################################################


'''
Dado um tabuleiro e duas posições (a,b) e (c,d), verifica se é
possível deslocar uma peça da posição (a,b) até a posição (c,d).

Em caso positivo, sua função deve retornar True e, em caso negativo,
False.
'''
def existe_caminho(tabuleiro, a, b, c, d):
	if (a,b) == (c,d):
		return True
	if tabuleiro[a][b] == 0:
		return False
	else:
		valornacasa=tabuleiro[a][b]
		tabuleiro[a][b]=0
		podedescer=True
		podesubir=True
		podeesquerda=True
		podedireita=True
		if a + valornacasa>=len(tabuleiro):
			podedescer=False
		if a - valornacasa<0:
			podesubir=False
		if b + valornacasa>=len(tabuleiro[0]):
			podedireita=False
		if b - valornacasa<0:
			podeesquerda=False
		if podedescer:
			if existe_caminho(tabuleiro,a+valornacasa,b,c,d):
				return True
		if podesubir:
			if existe_caminho(tabuleiro,a-valornacasa,b,c,d):
				return True
		if podeesquerda:
			if existe_caminho(tabuleiro,a,b-valornacasa,c,d):
				return True
		if podedireita:
			if existe_caminho(tabuleiro,a,b+valornacasa,c,d):
				return True
		return False



# Leitura de dados
n, m = [int(i) for i in input().split()]
tabuleiro = []
for _ in range(n):
	tabuleiro.append([int(i) for i in input().split()])
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

copiatabuleiro=[]
for linha in tabuleiro:
	copialinha= linha.copy()
	copiatabuleiro.append(copialinha)


# Verifica se existe caminho entre as posições dadas
caminho_1="nao existe caminho"
caminho_2="nao existe caminho"
if existe_caminho(tabuleiro,a,b,c,d):
	caminho_1="existe caminho"
if existe_caminho(copiatabuleiro,c,d,a,b):
	caminho_2="existe caminho"
# Impressão do resultado

print("({},{}) -> ({},{}):".format(a,b,c,d), caminho_1)
print("({},{}) -> ({},{}):".format(c,d,a,b), caminho_2)
