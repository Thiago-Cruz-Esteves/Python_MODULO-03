galera=[]
dados=[]
totmai=totmen=0
for c in range(0,3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen+=1
print(f'temos {totmai} maiores e {totmen} ,enores de idade.')


