nu=[5,2,7,4,1]
nu[2]=3# subistuir
nu.append(6)# disonou o numero '6'
nu.sort()
nu.insert(0,0)# adisonou '0' na posiçao '0'
nu.sort(reverse=True)
nu.pop(0)#remove a posição 0
nu.remove(0)# remove o numero 0
print(nu)
print(len(nu))#quantidade de elemento
print('='*50)
valores=[]
valores.append(5)
valores.append(9)
valores.append(4)
for c,v in enumerate(valores):
    print(f'Na psiçao {c} encontrei o valor {v}!')
print('cheguei ao final da lista.')
print('='*50)
a=[2,3,4,5,6,7]
b=a# interligando a lista 'a' a 'b'
b[2]=8
print(a)
print(b)
print('='*50)
a=[2,3,4,5,6,7]
b=a[:]#copia da lista  ou seja vc copiou 'a' em 'b' e auteraçao nao sava na outra
b[2]=8
print(a)
print(b)
