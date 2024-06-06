def somatorioharmonico(n):
    if n ==1:
        return 1
    else:
        return somatorioharmonico(n-1)+(1/n)
