from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime

dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# create message object instance
msg = MIMEMultipart()

temperatura = input('Qual é a temperatura atual (em graus Celsius)? ')

# setup the parameters of the message
password = "muhyuxvpsedjqjng"
msg['From'] = "jayltonokra15@gmail.com"
msg['To'] = "jaylton.alencar@ufpe.br"
msg['Subject'] = "ALERTA DE TEMPERATURA"

mensagem = 'A temperatura atual é de '+temperatura+'ºC \nData e hora: '+dataHora

msg.attach(MIMEText(mensagem, 'plain'))  # add in the message body

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

server.login(msg['From'], password)  # Login Credentials for sending the mail


# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("Email enviado com sucesso para %s" % (msg['To']))