Dalunos={}
Dalunos['nome']=str(input('Nome: '))
Dalunos['media']=float(input(f'Media de {Dalunos["nome"]}: '))
if Dalunos['media']>=7:
    Dalunos['Situação']='Aprovado'
elif 5<=Dalunos['media']<7:
    Dalunos['Situação']='Recuperação'
else:
    Dalunos['Situação']='Reprovado'
print('=-='*30)
for k, v in Dalunos.items():
    print(f' -{k} é igual a {v}')