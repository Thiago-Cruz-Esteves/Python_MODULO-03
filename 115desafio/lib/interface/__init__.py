def linflot(msg):
    while True:
        try:
            nu=float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: Por Favor digite um numero real\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return nu
def linint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: Por favor digite um Número.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
def lin(tam=42):
    return '-'*tam
def cabeçanho(txt):
    print(lin())
    print(txt.center(42))
    print(lin())
def menu(lista):
    cabeçanho('Menu Principal')
    c=1
    for item in lista:
        print(f'{c}-{item}')
        c=c+1
    print(lin())
    opc=linint('Sua Opção: ')
    return opc