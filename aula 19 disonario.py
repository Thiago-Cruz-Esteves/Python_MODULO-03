estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('Unidade federativa: '))
    estado['sigla']=str(input('sigla do estado: '))
    brasil.append(estado.copy())# para copiar usa o '.copy'
print(brasil)
for est in brasil:
    print(est)
    for k,v in est.items():
        print(f'O campo {k} e referente a {v}')
        print(est)
print('=-='*15,'EXEMPLO','=-='*15)
for est in brasil:
    print(est)
    for v in est.values():
        print(f'{v}',end=' ')
        print()

