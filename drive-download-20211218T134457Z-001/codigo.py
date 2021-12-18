import RPi.GPIO as GPIO
import time
import ex_en
import servidor_get as sget

GPIO.setmode(GPIO.BOARD) #Modo como referenciar os pinos da placa (.BOARD pega o numero do pino da placa)

#GPIO.setup(3, GPIO.IN) #Entrada digital #Sensor de presença
GPIO.setup(5, GPIO.IN) #Entrada digital #Sensor fotoelétrico
GPIO.setup(11, GPIO.OUT) #Saida digital #Iluminação
GPIO.setup(13, GPIO.OUT) #Saida digital #Câmera

sensor = 3 #GPIO = 3
ldr = 10 #GPIO = 5

dicionario = sget.servidor()
tempo = dicionario['tempo_funcionamento']
  
iluminacao = int(input('1- Ligar o sistema de iluminação\n0-Sair\n'))
if iluminacao == 1:
  GPIO.output(11, GPIO.HIGH)
  time.sleep(tempo)
  GPIO.output(11, GPIO.LOW)


if sensor == 3:
  if ldr < 5 :
    GPIO.output(13, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(13, GPIO.LOW)
    #enviar email(colocar o código da lista)
    if(dicionario['enviar_email']==1):
      ex_en.enviar_email('aaaaaaaaaaaaa ',dicionario['email'])
  else:
    if iluminacao < 1:
      GPIO.output(11, GPIO.HIGH)
      time.sleep(.5)
      GPIO.output(13, GPIO.HIGH)
      time.sleep(5)
      GPIO.output(13, GPIO.LOW)
      #enviar email
      if(dicionario['enviar_email']==1):
          ex_en.enviar_email('aaaaaaaaaaaaa ',dicionario['email'])
      time.sleep(tempo)
      GPIO.output(11, GPIO.LOW)
    else:
      GPIO.output(13, GPIO.HIGH)
      time.sleep(5)
      GPIO.output(13, GPIO.LOW)
      #enviar email
      if(dicionario['enviar_email']==1):
          ex_en.enviar_email('aaaaaaaaaaaaa ',dicionario['email'])
      