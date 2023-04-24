dados={}
listagols=[]
time=[]
while True:
    dados.clear()
    dados['nome']=str(input('Nome do jogador: '))
    quant=int(input(f'quantas partida {dados["nome"]} jogou: '))
    listagols.clear()
    for c in range(0,quant):
        listagols.append(int(input(f' -Quantos gols na apartida {c+1}: ')))
    dados['gols']=listagols[:]
    dados['total']=sum(listagols)
    time.append(dados.copy())
    while True:
        resp=str(input('Quer continuar [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apena s ou n')
    if resp=='N':
        break
print('=-='*40)
print(f'{"Cod"}',end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>4} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print('-'*30)
while True:
    busaca=int(input('Mostars dados de qual jogador? (999 para parar)'))
    if busaca==999:
        break
    if busaca >=len(time):
        print(f'Erro! nao existe esse jogador com codigo da busca {busaca} !')
    else:
        print(f"--Levantamento do jogador {time[busaca]['nome']}: ")
        for i,g in enumerate(time[busaca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<<VOLTE SEMPRE>>')











