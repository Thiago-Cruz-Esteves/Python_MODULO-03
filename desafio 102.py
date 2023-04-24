def fa(n, show=False):
    """
    --> Calcula o fatorial de um numero, mas e mais facil importar maht!
    :param n:O numero a ser calculado
    :param show: (opicional) Mostrar ou nao a conta.
    :return:O valor do fatorial de um numero n .
    """
    f=1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(f'x', end='')
            else:
                print('=',end='')
        f=f*c
    return f
print(fa(5,show=True))