listesco=('Lapis',1.75,'Borrcha',2,'Carderno',15.90,'Estojo',25,'Transferidor'
          ,9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)# numeros nao presição de ''.
print('='*40)
print(f'{"LISTAGEM DE PREÇO":^40}')# para sentralizar utiliza':^40'
print('='*40)
for posição in range(0,len(listesco)):
    if posição%2==0:# A união da sua 'lista' e da posição gera impreçao com ordem. exp: print(listesco[posição])
        print(f'{listesco[posição]:.<30}',end='')# para jogar os '.' a direita. EXP:'.<30'
    if posição%2==1:# a divisão da posiçao gera par e impar por esse motivo fica facio denominar o print.
        print(f'R${listesco[posição]:>5.2f}')

