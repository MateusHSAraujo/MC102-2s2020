n= int(input("Digite o tamanho da primeiro conjunto: "))
m= int(input("Digite o tamanho da segundo conjunto: "))
l1=[int(input("Digite os valores da primeiro conjunto: ")) for a in range(1,n+1)]
l2=[int(input("Digite os valores da segundo conjunto: ")) for b in range(1,m+1)]
print("Primeiro conjunto:", l1)
print("Segundo conjunto:", l2)
luniao= l1+l2
for e in luniao:
    quantidadederepetiçoes= luniao.count(e)
    while quantidadederepetiçoes > 1:
        quantidadederepetiçoes= quantidadederepetiçoes -1
        luniao.remove(e)
print("Resultado:", luniao)