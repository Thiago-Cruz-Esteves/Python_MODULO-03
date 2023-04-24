from random import randint
def sortear():
    sor=[]
    soma=0
    for c in range(0,5):
        sor.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in sor:
        print(f'{c}',end=' ')
        if c%2==0:
            soma=soma+c
    print('Pronto!')
    print(f'\nSomando os valores pares de {sor}, temos {soma}.')
print(sortear())
