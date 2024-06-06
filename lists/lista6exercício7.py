def hanoi(n, inicial , final , auxiliar ):
    s="Mova o disco {} do pino {} para o pino {}"
    if n ==1:
        print(s.format(n,inicial,auxiliar))
        print(s.format(n,auxiliar,final))
    if n>1:
        hanoi(n-1,inicial,final,auxiliar)
        print(s.format(n,inicial,auxiliar))
        hanoi(n-1,final,inicial,auxiliar)
        print(s.format(n,auxiliar,final))
        hanoi(n-1,inicial,final,auxiliar)
