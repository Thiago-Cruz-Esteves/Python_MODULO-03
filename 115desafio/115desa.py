from lib.interface import *
from lib.arquivo import *
arq='Curso em video. txt'
if arquivoExiste(arq):
    print(" Arquivo existe")
else:
    print(" Arquivo não existe")
    criararquivo(arq)
    while True:
        resposta = menu(['Criar arquivo', 'Cadastro Pessoas', 'Lista Pessoas', 'Sair do Sistema'])
        if resposta == 1:
            print('Opçao 1')
        elif resposta == 2:
            print('Opçao 2')
        elif resposta == 3:
            print('Saindo do sistema... Ate logo!')
            break
        else:
            print('\033[31m ERRO! Digite uma opção valida!\033[m')


