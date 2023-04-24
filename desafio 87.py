matriz=[[0,0,0],[0,0,0],[0,0,0]]
somap=0
somac=0
maior=0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor [{linha},{coluna}]: '))
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:
            somap = somap + matriz[linha][coluna]
    print()
print('-='*30)
print(f'Soma dos valores pares é {somap}')
for linha in range(0,3):
    somac=somac+matriz[linha][coluna]
print(f"A soma dos valores de terceira conula é {somac}.")
for coluna in range(0,3):
    if coluna==0:
        maior=matriz[1][coluna]
    elif matriz[1][coluna]>maior:
        maior=matriz[1][coluna]
print(f'O mair valor da segunda linha é {maior}')

