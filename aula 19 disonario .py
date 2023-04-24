print('Disonarios')
dados=dict()
dados1={}
dados={'nome':'Pedro','idade':25}
print(dados['nome'])# dar printi com a determinaçao ex: nome='Pedro'
print(dados['idade'])
dados['sexo']='M'
print(dados)
dados['sexo1']='F'#Para adisonar nomencaltura 'sexo1' e rferencia 'f' e preciso enumerar ex: 'sexo1'
print(dados)
print('=-='*40)
filme={}
filme={'titulo':'star wars','ano':1977,'diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
print('=-='*15,'EXEMPLO','=-='*15)
for k,v in filme.items():
    print(f'O {k} é {v}')
print('=-='*15,'EXEMPLO','=-='*15)
locadora=[]
filme1={'titulo':'STAR WARS','ano':1977,'diretor':'George Lucas'}
filme2={'titulo':'AVENGER','ano':2012,'diretor':'Joss Whedon'}
filme3={'titulo':'MATRIX','ano':1999,'diretor':'Wachawski'}
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora)
print(locadora[0]['ano'])
print(locadora[2]['titulo'])