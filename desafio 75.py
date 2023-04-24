n=(int(input('Digite o valor: ')),int(input('Digite o valor: ')),int(input('Digite o valor: ')),int(input('Digite o valor: ')))
print(f'Você digitou os valores{n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apreceu na {n.index(3)+1}ª possição')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares digitados foram',end=' ')
for ns in n:
    if ns%2==0:
        print(ns,end=' ')
