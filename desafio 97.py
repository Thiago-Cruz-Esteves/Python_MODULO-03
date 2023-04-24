def escreva (msg):
    es=str(input('Escreva uma frase ou palavra? '))
    cont=2
    for pos in enumerate(es):
        cont=cont+1
    print('-'*cont)
    print(f'{es:^{cont}}')
    print('-' * cont)

print(escreva())