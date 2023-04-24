dados={}
lisata=[]
soma=med=0
while True:
    dados['nome']=str(input('Nome: '))
    while True:
        dados['sexo']=str(input('Sexo:[M/F] ')).strip().upper()[0]
        if dados['sexo']  in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade']=(int(input('Idade: ')))
    soma=soma+dados['idade']
    lisata.append(dados.copy())
    while True:
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp=='N':
        break
print(f'Ao todo temos {len(lisata)} pessoas cadastradas. ')
med=float(soma/len(lisata))
print(f'A media de idade é de {med:2f}')
print('As mulheres cadastradas foram',end=' ')
for p in lisata:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
        print()
print('Lista das pessoas que estão acima da media: ')
for p in lisata:
    if p['idade']>med:
        print('   ')
        for k,v in p.items():
            print(f'{k}={v}',end='')
        print()
print('<<Encerrado>>')

