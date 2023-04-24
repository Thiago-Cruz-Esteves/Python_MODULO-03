import ex107
din=float(input('Digite o Valor: R$'))
ta1=float(input('Digite a  porcentagem da taxa de aumento: '))
ta2=float(input('Digite a  porcentagem da taxa de desconto: '))
print(f'A metade de {din:.2f} é {ex107.metade(din):.2f}')
print(f'O dobro de {din:.2f} é {ex107.dobro(din):.2f}')
print(f'O aumento de  de {ta1}% de R$:{din:.2f} é R$:{ex107.aum(din,ta1):.2f}')
print(f'O desconto  de {ta2}% de R$:{din:.2f}  é R$:{ex107.dimi(din,ta2):.2f}')