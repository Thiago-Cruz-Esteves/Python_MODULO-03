def an(ano):
    from datetime import datetime
    at = datetime.now().year
    c=at-ano
    print(f'Com {c} anos:', end=' ')
    if c>=16 and c<=17 or c>=67:
        print('Voto Opsonal')
    elif 18<=c<67:
        print('Voto Obrigatorio!')
    elif c<16:
        print('Não Vota!')
ano=int(input('Em que ano Você nasceu? '))
an(ano)

