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

n1=linint('Digite um numero inteiro: ')
n2=linflot('Digite um numero real: ')
print(f"O valor inteiro foi {n1} e o real foi {n2}.")