import ex108
din=float(input('Digite o Valor: R$'))
ta1=float(input('Digite a  porcentagem da taxa de aumento: '))
ta2=float(input('Digite a  porcentagem da taxa de desconto: '))
print(f'A metade de {ex108.ex108(din)} é {ex108.ex108(ex108.metade(din))}')
print(f'O dobro de {ex108.ex108(din)} é {ex108.ex108(ex108.dobro(din))}')
print(f'O aumento de  de {ta1}% de {ex108.ex108(din)} é R$:{ex108.ex108(ex108.aum(din,ta1))}')
print(f'O desconto  de {ta2}% de {ex108.ex108(din)}  é R$:{ex108.ex108(ex108.dimi(din,ta2))}')