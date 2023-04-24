nome = input('Nome do jogador: ')
quant = int(input(f'Quantas partidas {nome} jogou: '))
gols = [int(input(f'Quantos gols na partida {i+1}: ')) for i in range(quant)]
daddos = {'nome': nome, 'gols': gols, 'total': sum(gols)}
print('=-=' * 15)
print(daddos)
print('=-=' * 15)
for k, v in daddos.items():
    print(f'O {k} é referente a {v}')
print('=-=' * 15)
print(f'O jogador {daddos["nome"]} jogou {quant} partidas')
for i, gol in enumerate(gols):
    print(f' => Na partida {i+1}, fez {gol} gols.')
print(f'Foi um total de {daddos["total"]} gols.')
