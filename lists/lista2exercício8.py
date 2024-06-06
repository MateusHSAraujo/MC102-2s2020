valor = int( input (" Digite um número : "))
fatorial = n = valor

if n >= 0:
    while n > 1:
     n = n - 1
     fatorial = fatorial * n
    print ("O fatorial de", valor , "é igual a:", fatorial)
else:
    print ("Não existe fatorial de", valor )
#O erro do código fonte era que n acabava assumindo o valor 0, bem como o print estava ocorrendo mesmo o número tendo fatorial