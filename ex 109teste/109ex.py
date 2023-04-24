import moeda
din=float(input('Digite o Valor: R$'))
ta1=float(input('Digite a  porcentagem da taxa de aumento: '))
ta2=float(input('Digite a  porcentagem da taxa de desconto: '))
print(f'A metade de {moeda.moeda(din)} é {moeda.metade(din,True)}')
print(f'O dobro de {moeda.moeda(din)} é {moeda.dobro(din,True)}')
print(f'O aumento de  de {ta1}% de {moeda.moeda(din)} é R$:{moeda.aum(din,ta1,True)}')
print(f'O desconto  de {ta2}% de {moeda.moeda(din)}  é R$:{moeda.dimi(din,ta2,True)}')