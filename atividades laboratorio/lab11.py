###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Mateus Henrique Silva Araujo	
# RA: 184940
###################################################

"""
Esta função recebe seis parâmetros:
- tabuleiro: a configuração inicial do tabuleiro;
- altura_tabuleiro: o valor da altura do tabuleiro;
- largura_tabuleiro: o valor da largura do tabuleiro;
- peca: a configuração da peça a ser inserida;
- altura_peca: o valor da altura da peça a ser inserida;
- largura_peca: o valor da largura da peça a ser inserida.

A função deve retornar a configuração atualizada do tabuleiro 
e o status do jogo ("O jogo deve continuar" ou "Fim de jogo")
"""
def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                  peca, altura_peca, largura_peca):
	tabuleirovariavel=[linha.copy() for linha in tabuleiro]
	pecaivariavel=[linha.copy() for linha in peca]
	
	pecaparaanalise=[[0 for j in range(largura_peca)] for i in range(altura_peca)]
	for i in range(altura_peca):
		for j in range(largura_peca):
			pecaparaanalise[i][j] = (pecaivariavel[i][j]).replace(".","*")

	c=0
	l=0


	while l+altura_peca <= altura_tabuleiro:

		matrizanálise=[[0 for j in range(largura_peca)] for i in range(altura_peca)]

		for i in range(l,altura_peca+l):
			for j in range(c,largura_peca+c):
				matrizanálise[i-l][j-c]= (tabuleirovariavel[i][j]).replace(".","#")
		if matrizanálise == pecaparaanalise:
			for i in range(l,altura_peca+l):
				for j in range(c,largura_peca+c):
					tabuleiro[i][j]= (tabuleirovariavel[i][j]).replace(".","#")
			return tabuleiro, "O jogo deve continuar"
		c+=1
		if c+largura_peca >largura_tabuleiro:
			c=0
			l+=1


	return tabuleiro, "Fim de jogo"




# Leitura de dados
 
altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]

# Leitura do tabuleiro

tabuleiro=[ list(input()) for i in range(altura_tabuleiro)]

# Dica: use a função list() para transformar uma srting numa lista de caracteres

altura_peca, largura_peca = [int(x) for x in input().split()]
                           
# Leitura da peça

peca=[ list(input()) for i in range(altura_peca)]

# Dica: use a função list() para transformar uma srting numa lista de caracteres

# Impressão da configuração atualizada do tabuleiro

tabuleiro, status_do_jogo = verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                                          peca, altura_peca, largura_peca)

for linha in tabuleiro:
	print("".join(linha))

# Impressão do status do jogo
print(status_do_jogo)
