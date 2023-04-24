def dobro(x):
    return x*2

valor=[1,2,3,4,5,6,7,8,9,10]

valor_dobro=map(dobro,valor)
test=map(dobro,valor)
for v in valor_dobro:
    print(v)
print('=-='*30)
from  functools import reduce

def soma(x=0,y=0):
    return x+y
valor_1=[1,2,3,4,5,6,7,8,9]
soma_lista=reduce(soma,valor_1)

print(soma_lista)

print('=-='*30)
valor_2=[1,2,3,4,5]
valor_3=['a','b','c','d','e']

for numero, letra in zip(valor_2,valor_3):
    print(numero,letra)