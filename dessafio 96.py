def area(*ara):
    print('Controle de terrenos')
    print('-' * 20)
    l = float(input('Lagura (M): '))
    c = float(input('Comprimento (M): '))
    a=l*c
    print(f'A area de um terreno {l:.2f}x{c:.2f} é de {a:.2f}m².')
print(area())

