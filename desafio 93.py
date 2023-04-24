daddos={}
daddos['nome']=str(input('Nome do jogador: '))
quant=float(input(f'Quntas partidas {daddos["nome"]} jogou: '))
tot=0
soma=0
listagol=[]
while True:
    tot=tot+1
    listagol.append(int(input(f'Quantos gols na partida {tot-1} : ')))
    if tot==quant:
        break
for pos in range(0,len(listagol)):
    soma=soma+listagol[pos]
daddos['gols']=listagol
daddos['total']=soma
print('=-='*30)
print(daddos)
print('=-='*30)
for k,v in daddos.items():
    print(f'O {k} é referente a {v} ')
print('=-='*30)
print(f'O jogador {daddos["nome"]} jogou {quant} partidas ')
for pos in range(0,len(listagol)):
    print(f' => Na partida {pos}, fez {listagol[pos]} gols. ')
print(f'Foi um total de {soma} gols. ')

