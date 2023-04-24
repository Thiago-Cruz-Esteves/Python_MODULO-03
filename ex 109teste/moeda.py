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
    return f'{moeda}{v:>8.2f}'.replace('.',',')