def area(l,c):
    a=l*c
    print(f'A area de um terreno {l}x{c} é de {a}m².')
#program principal
print('Controle de terrenos')
print('-' * 20)
l = float(input('Lagura (M): '))
c = float(input('Comprimento (M): '))
area(l,c)