lanche='haburguer','suco','Pizza','Pudim','Batata Frita'
for cont in range(0,len(lanche)):
    print(f'vou comer {lanche[cont]} na posiçao {cont}')# o cont ja registra a posição.
print('='*40)
for pos,comida in enumerate(lanche):#o 'pos' que é referencia do 'enumerate' ja registra a posição.
    print(f'vou comer {comida} na posiçao {pos}')
print('=' * 40)
print(sorted(lanche))#SORTED serve para organizar alfabeticamente.
print(lanche)
print(lanche.index('suco'))# ve a posiçao atraves do produto'suco', mas pega o primeiro prosuto se estiver repetido
#'del (lanche)' comando para deletar ela inteira