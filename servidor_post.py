import requests
#-Criar um relatório-#
arquivo = {'file': open('C:\\Users\\judon\\Desktop\\imagem1.png','rb')}
data = {'observacao':'xacdasdasdas', 'imagens':arquivo}
x = requests.post('http://9595-192-141-108-70.ngrok.io/api/relatorio', data = data)
print(x.content)