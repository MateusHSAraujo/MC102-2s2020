n= int(input("Digite o valor do tamanho dos vetores: "))
u=[int(input("Digite os valores dos componentes de u: ")) for a in range(1,n+1)]
v=[int(input("Digite os valores dos componentes de v: ")) for b in range(1,n+1)]
b=0
somaanterior=0
while b<n:
    produtoescalar= (u[b]*v[b])+ somaanterior
    somaanterior= produtoescalar
    b=b+1
print("O produto escalar dos vetores dados é:", produtoescalar)