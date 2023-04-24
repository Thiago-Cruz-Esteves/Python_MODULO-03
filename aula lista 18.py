teste=[]
teste.append('thiago')
teste.append(30)
print(teste)
print(len(teste))
galera=[]
galera.append(teste[:])# para coipiar e fazer ateraçoes usar '[:]'
teste[0]='maria gostosa'
teste[1]='32'
galera.append(teste)
print(galera)
print(len(teste))
print(len(galera))