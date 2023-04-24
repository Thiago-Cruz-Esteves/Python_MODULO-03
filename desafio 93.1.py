dados={}
listagols=[]
dados['nome']=str(input('Nome do jogador: '))
tot=int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0,tot):
    listagols.append(int(input(f'Quantas partidas {c+1} jogou ? ')))
dados['gols']=listagols[:]
dados['total']=sum(listagols)
print('=-='*30)
print(dados)
print('=-='*30)
for k,i in dados.items():
    print(f'O {k} é referente a {i}')
print('=-='*30)
print(f'O jogagdor {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i,v in enumerate(dados['gols']):
    print(f' =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')