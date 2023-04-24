nu20=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez'
      ,'onze','doze','treze','quatorse','quinze','dezeseis','dezecete','dezoito','dezenove','vinte')
while True:
    nu = int(input('digite um numero entre 0 a 20: '))
    while nu<0 or nu>20 :# comando de repetição
        nu = int(input('digite um numero entre 0 a 20: '))
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':  # a posição do (if) é de acordo com while que pertence!
        break
    print('Tente novamente',end='')
print(f'Vovê digitou o Numero {nu20[nu]}')# O numero do 'nu' é igual a do nu20.



