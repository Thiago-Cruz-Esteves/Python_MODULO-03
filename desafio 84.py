anlise=[]
dados=[]
totp=0
maior=0
menor=0
while True:
    totp=totp+1
    dados.append(str(input('Digite o seu nome: ')))
    dados.append((float(input('Digite o seu peso: '))))
    if len(anlise)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
    anlise.append(dados[:])
    dados.clear()
    resp=str(input('Quer continuar[S/N]:  ')).strip().upper()[0]
    while resp not in'SN':
        resp = str(input('Quer continuar[S/N]:  ')).strip().upper()[0]
    if resp=='N':
        break
print('='*30)
print(f"Os dados foram {anlise}")
print(f'Ao todo você cadastrou {len(anlise)} pessoas')
print(f'O maoir pesso foi de {maior}kg. Peso de ',end=' ')
for p in anlise:
    if p[1]==maior:
        print(f'{p[0]}')
print(f'\nO menor peso foi de {menor}kg. Peso de ',end=' ')
for p in anlise:
    if p[1]==menor:
        print(f'{p[0]}')



