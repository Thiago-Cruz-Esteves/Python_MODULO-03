c=['\033[m','\033[0;30;41m','\033[0;30;42m','\033[0;30;43m','\033[0;30;44m','\033[0;30;45m','\033[7;30m']
def ajuda(com):
    print(c[4])
    help(com)
    print(c[0])
def titulo(msg,cor=0):
    tan=len(msg)+2
    print('-'*tan)
    print(f'{c[1]}{msg:^{tan}}{c[0]}')
    print('-' * tan)
comando=''
while True:
    titulo('SISTEMA DE AJUDA PyHELP!')
    comando= str(input("Função ou Biblioteca> ")).strip()
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
print(f'{c[1]}Ate logo!{c[0]}')