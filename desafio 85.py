listnun=[[],[]]
nun=0
for pos in range(1,8):
    nun=int(input('Digite  um numero: '))
    if nun%2==0:
        listnun[0].append(nun)
    else:
        listnun[1].append(nun)
print('-='*20)
listnun[0].sort()
listnun[1].sort()
print(f'Os numeros pares foram: {listnun[0]}')
print(f'Os numeros impar foram: {listnun[1]}')