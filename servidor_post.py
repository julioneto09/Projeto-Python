import requests

#-Criar um relatório-#


def enviar_relatorio(imagens):

    arquivo = {}
    for index, img in enumerate(imagens):
        arquivo['image['+str(index)+']'] = open(img, 'rb')

    print('Enviando arquivos...')

    payload = {'observacao': 'Nova ocorrência identificada'}
    try:
        x = requests.post('http://localhost:8000/api/relatorio', data=payload, files=arquivo)
        print('Upload enviado com sucesso')
    except:
        print('Falha no upload')


enviar_relatorio(['C:\\Users\\jaylt\\Downloads\\imgRuido.jpg', 'C:\\Users\\jaylt\\Downloads\\img.jpg'])
