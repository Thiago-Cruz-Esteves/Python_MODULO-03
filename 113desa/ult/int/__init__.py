def leiaint(msg):
    ok=False
    valor=0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[91mERRO:Por vafor,digite um numero inteiro valido.\033[0m')
        if ok:
            break
    return valor
