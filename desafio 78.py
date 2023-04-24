listn=[]
mai=0
men=0
for pos in range(0,5):
    listn.append(int(input(f'Digite o numero da posiçao {pos}:')))# potao de add.
    if pos==0:# condiçao de comparaçao
        main=men=listn[pos]
    else:
        if listn[pos]>mai:
            mai=listn[pos]
        if listn[pos]<men:
            men=listn[pos]
print('-=-'*20)
listn.sort()
print(f'Voce digitou {listn}')
maior=max(listn)
menor=min(listn)
print(f'O maior valor foi {maior} nas poições {listn.index(maior)}')
print(f'O menor valor foi {menor} nas poições {listn.index(menor)}')
print('*Condiçao de comparaçao')
print(f'O maior valor foi {mai} nas poições',end=' ')
for i,v1 in enumerate(listn):# dentro de um i=int tem um valor=v vou enumerar com enumerate
    if v1==mai:
        print(f'{i}...',end='')
print(f'\nO menor valor foi {men} nas poições',end=' ')
for i,v2 in enumerate(listn):
    if v2 ==men:
        print(f'{i}...',end='')






