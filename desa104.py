def leiaint(msg):
    ok=False
    valor=0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor=float(n)
            ok=True
        else:
            print('\033[91mERRO!Digite um numero inteiro valido.\033[0m')
        if ok:
            break
    return valor
n=leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')