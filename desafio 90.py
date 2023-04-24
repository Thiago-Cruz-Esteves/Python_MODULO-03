dados={}
lista=[]
dados['nome']=str(input('Nome: '))
dados['media']=float(input(f'Media de {dados["nome"]}: '))
lista.append(dados.copy())
for no in lista:
    for k,v in no.items():
        print(f'O {k} é igual a {v}')
if dados['media']<7:
    print('Situação é igual a Reprovado')
else:
    dados['media']>=7
    print('Situação é igual a Aprovado')

