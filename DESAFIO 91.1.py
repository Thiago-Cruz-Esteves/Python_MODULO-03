from  random import randint
from operator import itemgetter
jogo={'jogador 1':randint(1,6),
      'jogador 2':randint(1,6),
      'jogador 3': randint(1, 6),
      'jogador 4': randint(1, 6),}
rank=[]
print('Valores sorteados: ')
print('==Ranking dos Jogadores')
for k,v in jogo.items():
      print(f'{k} tirou {v} no dado')
rank=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print(rank)
for i,v in enumerate(rank):
      print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
