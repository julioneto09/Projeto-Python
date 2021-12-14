import requests
import envio1 as mail
import logica1

enviar = mail.email_origem # = "email.que.envia.os.arquivos"
receber = mail.email_destino # = "email.que.recebe.os.arquivos"
arquivo = mail.mensagem # = "foto01"
tempo = logica1.tempo # = int(input('Quantas horas o sistema ficará em funcionamento: '))

dados = {'email_origem':enviar,'duração':tempo,'email_destino':receber, 'anexo':arquivo}
r = requests.post('https://fd26-192-141-108-70.ngrok.io/api/config',data = dados)
r_dictionary= r.json()
print(r_dictionary['form'])