def lin (msg=''):
    print('-'*40)
    print(f'{msg:^40}')
    print('-' * 40)
def dobro(v=0,formato=False):
    res=v*2
    return res if formato is False else moeda(res)
def metade(v=0,formato=False):
    res =v/2
    return res if formato is False else moeda(res)
def aum(v=0,t=0,formato=False):
    res =v+(v*(t/100))
    return res if formato is False else moeda(res)
def dimi(v=0,t=0,formato=False):
    res =v-(v*(t/100))
    return res if formato is False else moeda(res)
def moeda(v=0,moeda='R$'):
    return f'{moeda}{v:>2.2f}'.replace('.',',')
def resumo(d,t1,t2):
    print(f'Preço anlizado\t{moeda(d)}')#'\t' usa para organisar a tabela
    print(f'Dobro do preço: \t{dobro(d,True)}')
    print(f'Metade do preço:\t{metade(d,True)}')
    print(f'{t1}% de aumenta: \t{aum(d,t1,True)}')
    print(f'{t2}% de aumenta: \t{dimi(d,t1,True)}')
    lin('Fim!')