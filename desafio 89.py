listn=list()
while True:
    nome=(str(input('Nome: ')))
    nota1=(float(input('Nota 1: ')))
    nota2=(float(input('Nota 2: ')))
    med=(nota1+nota2)/2
    listn.append([nome, [nota1],[nota2], med])
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp not in 'NS':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
print('=-='*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-='*26)
for i, a in enumerate(listn):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    print('=-='*30)
    bot=int(input('Mostrar notas de qual aluno? ( 999 interompe!'))
    if bot==999:
        break
    if bot <=len(listn)-1:
        print(f'Notas de {listn[bot][0]} são {listn[bot][1]}')
print('<<<VOLTE SEMPRE>>>')
