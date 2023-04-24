lista=[]
for pos1 in range(0,5):
   nu=(int(input('Digite um valor:')))
   if pos1==0 or nu>lista[-1]:
       lista.append(nu)
       print('Adicionado no final da lista...')
   else:
       pos2=0
       while pos2 < len(lista):
           if nu<=lista[pos2]:
               lista.insert(pos2,nu)
               print(f'Adicionado na posição {pos2} da Lista')
               break

           pos2=pos2+1
print('-='*30)
print(f'Os valores digitados em ordem foram{lista}')





