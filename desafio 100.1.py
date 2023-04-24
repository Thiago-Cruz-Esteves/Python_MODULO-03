from random import randint
def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print(f'{n}',end='')
def somarpar(lista):
    soma=0
    for valor in lista:
        if valor %2==0:
            soma=soma+valor
    print(f'somando os valores pares de {lista}, temos {soma}')
nun=[]
sorteio(nun)
somarpar(nun)