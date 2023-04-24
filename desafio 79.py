nu=list()
while True:
    n=(int(input('Digite um valor: ')))
    if n not in nu:
        nu.append(n)
        print('valor disonado com sucesso...')
    else:
        print('Valor dublicado! Não vou adisonar')

    sn=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if sn=='N':
        break
print('-=-'*20)
nu.sort()
print(f'Voce digitou valores {nu}')