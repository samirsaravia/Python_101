import urllib
import urllib.request

try:
    response = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('Não foi possível acessar no momento')
else:
    print('Consegui acessar ao site com sucesso')
