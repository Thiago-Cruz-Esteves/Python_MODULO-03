from datetime import datetime
dados={}
dados['nome']=str(input('Qual seu nome: '))
nas=int(input('Ano de nascimento: '))
dados['idade']=datetime.now().year-nas
dados['ctps']=int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] !=0:
    dados['contrataçao']= int(input('Ano de Contratação: '))
    dados['salario']=float(input('Salario: R$'))
    dados['aposentadoria']=dados['idade']+dados['contrataçao']+35-datetime.now().year
print('=-='*40)
for k,v in dados.items():
    print(f'- {k} e referente a {v}')
