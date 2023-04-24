def mostralinha():# rotina
    print('=-='*25)
mostralinha()
print('oamcapaómmvva´çp')
mostralinha()
print('oamcapaómmvva´çp')
mostralinha()
def lin(txt):
    print('=-='*20)
    print(txt)
    print('=-=' * 20)
lin('OI tudo bm')
#programa principal
def soma(a,b):
    s=a+b
    print(s)

soma(5,6)
mostralinha()
def contador(*nun):
    for pos in nun:
        print(pos,end=' ')
    print()

contador(1,2,56,8,4,8,2)
mostralinha()
def dobra (lst):
    pos=0
    while pos <len(lst):
        lst[pos]=lst[pos]*2
        pos=pos+1
valores=[6,8,7,4,2,1,4,8,3]
dobra(valores)
print(valores)
mostralinha()


