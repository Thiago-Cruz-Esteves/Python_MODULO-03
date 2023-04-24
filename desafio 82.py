listn=[]
par=list()
impar=list()
while True:
    listn.append(int(input('Digite os valores: ')))
    resp=str(input('Quer continuar:[S/N] ')).strip().upper()[0]
    while resp not in 'NS':
        resp = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
    if resp=='N':
        break
for i,v1 in enumerate(listn):
    if v1%2==0:
        par.append(v1)
    else:
        impar.append(v1)
listn.sort(reverse=True)
print(f'A lista completa é {listn}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
