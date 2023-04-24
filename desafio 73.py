letras=('q','w','e','r','t','y','u','i','o','p')
print(f'Letras do teclado:{letras}')
print(f'Os 5 primeiras teclas:{letras[0:5]}')
print(f'As 4 Ultimas teclas são:{letras[-5:]}')
print(f'Teclas em ordem alfabetica são{sorted(letras)}')
l=str(input('Você quer a posiçao de que letra: ')).strip().lower()[0]
print( f'A tecla {l} esta em {letras.index(l)+1}ª posição.')