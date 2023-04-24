def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a=open(nome,'wt+')
    except:
        print('Houve um ERRO na Criaçao do Arquivo!')
    else:
        print(f'Aquivo {nome} criado com sucesso!')

