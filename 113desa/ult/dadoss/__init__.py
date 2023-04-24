def leidin(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.')# 'replace e usado para ubstitur em uma 'str' EX: vai subistuir ',' por '.'.
        if entrada.isalpha() or entrada.strip()=='':
            print(f'\033[0;31mErro:Por favor digite um número inteiro real valido.\033[m')
        else:
            valido=True
            return float(entrada)