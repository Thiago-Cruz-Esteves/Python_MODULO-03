def dobro(v=0):
    return v*2
def metade(v=0):
    return v/2
def aum(v=0,t=0):
    return v+(v*(t/100))
def dimi(v=0,t=0):
    return v-(v*(t/100))
def ex108(v=0,ex108='R$'):
    return f'{ex108}{v:>8.2f}'.replace('.',',')