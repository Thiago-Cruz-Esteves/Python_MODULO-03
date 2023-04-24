palavras=('aprender','programar','linguagen','python','curso','estudar','praticar','Trabalhar','mercado'
          ,'programar','futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos',end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':# para pegar vogais com acento e so adisonar Explo: add 'ãêé'
            print(f'{letra}', end=' ')