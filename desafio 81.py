listan=[]
while True:
    listan.append(int(input('Digite um valor: ')))
    sn=str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if sn=='N':
        break
print(f'Voce digitou {len(listan)} elementos')
listan.sort(reverse=True)
print(f'Os valores em ordem decrecente são {listan}')
if 5 in listan:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')