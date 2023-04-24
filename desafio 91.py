from random import randint
CONT=0
lista=[]
for c in range(1,5):
    jo=randint(0,6)
    lista.append(jo)
    print(f'Jogador {c} tirou {jo}')
lista.sort(reverse=True)
print(lista)
for pos in range(0,len(lista)):
    for p in lista:
        print(f'{pos+1} Lugar: Jogsdor {...} com {lista[pos]}')


