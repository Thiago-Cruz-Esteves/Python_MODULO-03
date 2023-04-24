from random import randint
sn=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: ',end="")
for listsn in sn:
    print(f'{listsn}', end=' ')
print(f'\no maior valor sorteado foi {max(sn)}')
print(f'o menor valor sorteado foi {min(sn)}')