import requests

def servidor():
    print('Carregando dados...')
    #-Ler os dados da api (tempo e email) e salvar no código-#
    r = requests.get('http://9595-192-141-108-70.ngrok.io/api/config')

    dicionario = r.json()
    #print(dicionario)
    segundos = dicionario['tempo_funcionamento']
    destino = dicionario['email']
    return dicionario