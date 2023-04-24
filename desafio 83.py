expr=str(input('Digite a expreçao: '))
pilha=[]
for simb in expr:
    if simb=='(':
        pilha.append('(')
    elif simb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expreçao esta certa')
else:
    print('sua expreçao esta errada')

