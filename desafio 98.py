from time import sleep
def contagem(i,f,p):
    print(f'Contagem de {i} ate {f} de {p} em {p}.')
    if p<0:
        p=p*-1
    if p==0:
        p=1
    if i<f:
        cont=i
        while cont<=f:
            sleep(1)
            print(f'{cont}',end=' ')
            cont=cont+p
        print('Fim')
    else:
        cont=i
        while cont>=f:
            sleep(1)
            print(f'{cont}',end=' ')
            cont=cont-p
        print('Fim')
# principal
contagem(1,10,1)
contagem(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
i1=int(input('Inicio: '))
f1=int(input('Fim: '))
p1 = int(input('Passo: '))
contagem(i1,f1,p1)
