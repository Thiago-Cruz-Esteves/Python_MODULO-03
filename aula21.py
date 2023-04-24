def lin ():
    print('-' *30)
def somar(a=0,b=0,c=0):
    soma=a+b+c
    print(soma)
lin()
somar(1,3,)
lin()
from math import factorial
f1=factorial(5)
print(f1)
def fa(nun=1):
    f=1
    for c in range(nun,0,-1):
        f=f*c
    return f
f2=fa(5)
print(f2)
lin()
def par (n=0):
    if n%2==0:
        return True
    else:
        return False
num=int(input('Digite um numero: '))
if par (num):
    print('É par!')
else:
    print('É impar!')