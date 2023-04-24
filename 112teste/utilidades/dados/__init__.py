def leidin(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.')# 'replace e usado para ubstitur em uma 'str' EX: vai subistuir ',' por '.'.
        if entrada.isalpha() or entrada.strip()=='':
            print(f'\033[0;31mErro:\"{entrada}"\ é um valor invalidao!\033[m')
        else:
            valido=True
            return float(entrada)