import urllib
import urllib.request
try:
    site=urllib.request.urlopen('https://coinmarketcap.com/pt-br/')
except urllib.error.URLError:
    print('O site nao esta acessivel no momento.')
else:
    print('Consegui acessar o site  com sucesso!')
    print(site.read())