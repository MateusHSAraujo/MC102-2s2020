#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Copa do Mundo de Futebol
# Nome: Mateus Henrique Silva Araújo 
# RA: 184940
#####################################################

# Leitura da lista de seleções

selecoes = []
dic = {}
for i in range(16):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0,
                  "vitorias": 0,
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}

# Leitura das partidas e processamento dos dados

for i in range(16):
  resultado=input()
  resultadosemparentese=resultado.replace("(","")
  resultadosemparentese=resultadosemparentese.replace(")","")
  lresultado= resultadosemparentese.split()
  if len(lresultado) <= 5:#Caso não ocorram pênaltis:
    nomep1= lresultado[0]
    golsmarcadosporp1= int(lresultado[1])
    golsmarcadosporp2=int(lresultado[3])
    nomep2=lresultado[4]
    for (selecao,dicdados) in dic.items():
      if selecao == nomep1:
        dicdados["partidas"]+=1
        if golsmarcadosporp1 > golsmarcadosporp2:
          dicdados['vitorias']+=1
        else:
          dicdados['derrotas']+=1
        dicdados['normal']+=1
        dicdados['marcados']= dicdados['marcados'] + golsmarcadosporp1
        dicdados['sofridos']= dicdados['sofridos'] + golsmarcadosporp2
      if selecao == nomep2:
        dicdados['partidas']+=1
        if golsmarcadosporp2 > golsmarcadosporp1:
          dicdados['vitorias']+=1
        else:
          dicdados['derrotas']+=1
        dicdados['normal']+=1
        dicdados['marcados']= dicdados['marcados'] + golsmarcadosporp2
        dicdados['sofridos']= dicdados['sofridos'] + golsmarcadosporp1
  else:#Caso ocorram penaltis
    nomep1=lresultado[0]
    golsmarcadosporp1=int(lresultado[1])
    golsmarcadosporp2=int(lresultado[3])
    penaltismarcadosp1=int(lresultado[4])
    penaltismarcadosp2=int(lresultado[6])
    nomep2=lresultado[7]
    for (selecao,dicdados) in dic.items():
      if selecao == nomep1:
        dicdados["partidas"]+=1
        if penaltismarcadosp1 > penaltismarcadosp2:
          dicdados['vitorias']+=1
        else:
          dicdados['derrotas']+=1
        dicdados['penaltis']+=1
        dicdados['marcados']= dicdados['marcados'] + golsmarcadosporp1
        dicdados['sofridos']= dicdados['sofridos'] + golsmarcadosporp2
      if selecao == nomep2:
        dicdados['partidas']+=1
        if penaltismarcadosp2 > penaltismarcadosp1:
          dicdados['vitorias']+=1
        else:
          dicdados['derrotas']+=1
        dicdados['penaltis']+=1
        dicdados['marcados']= dicdados['marcados'] + golsmarcadosporp2
        dicdados['sofridos']= dicdados['sofridos'] + golsmarcadosporp1        

for pais in selecoes:
  derrotas= dic[pais]['derrotas']
  if derrotas==0:
    campeao=pais

# Saída de dados

for selecao in selecoes:
  print("-" * 50)
  print("Pais:", selecao)
  print("Partidas:", dic[selecao]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
  print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
  print("Vitorias:", dic[selecao]["vitorias"])
  print("Derrotas:", dic[selecao]["derrotas"])
  print("Gols marcados:", dic[selecao]["marcados"])
  print("Gols sofridos:", dic[selecao]["sofridos"])

print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50)
