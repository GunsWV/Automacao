#importando o módulo após a instalação pelo pip install requests

import requests

#fazendo a requisição do tipo GET
response = requests.get('https://www.google.com/')

#verificando o status após a requisição
if response.status_code == 200:
    print('Conexão realizada')
else:
    print(f"erro na conexão com servidor : {response.status_code}")  