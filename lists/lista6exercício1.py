def média(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return média(lista[0:len(lista)-1])+(lista[len(lista)-1]//2)

