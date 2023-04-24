
def maior(* nun):
    cont=maior=0
    print('Analisando os valores passados...')
    for valor in nun:
        print(f'{valor}',end=' ')
        if cont==0:
            maior=valor
        else:
            if valor>cont:
                maior=valor
        cont=cont+1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(2,9,9)
maior(2,2)
maior(6)
maior(0)
