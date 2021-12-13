import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #Modo como referenciar os pinos da placa (.BOARD pega o numero do pino da placa)

GPIO.setup(3, GPIO.IN) #Entrada digital #Sensor de presença
GPIO.setup(5, GPIO.IN) #Entrada digital #Sensor fotoelétrico
GPIO.setup(21, GPIO.OUT) #Saida digital #Iluminação
GPIO.setup(23, GPIO.OUT) #Saida digital #Câmera

'''Como no simulador não conseguimos mudar o estado das entradas, forçamos os valores para poder testar'''
sensor = 3 #GPIO = 3
ldr = 5 #GPIO = 5

'''Se o sistema de iluminação for ativado (=1),  a lampada é ativada e fica ligado por n tempo'''
noite = int(input('1- Ligar o sistema de iluminação\n0-Sair'))
if noite == 1:
  tempo = int(input('Informe quantas horas o sistema ficará ligado: '))
  segundos = 3600*tempo
  GPIO.output(21, GPIO.HIGH)
  time.sleep(segundos)
'''Tentar implementar esse trecho do código acima em um app'''

'''Se o sensor de presença for ativado, verifica a luminosidade do ambiente:
    se o ldr estiver desativado, significa que está claro -> tirar a foto
    se o ldr estiver ativado, está escuro, e vamos verificar o sistema de iluminação:
      se o sistema estiver desligado (está de noite, porem já foi desligado) -> liga o sistema, tira a foto, e desliga o sistema
      se o sistema estiver ligado -> tira a foto'''
if sensor == 3:
  if ldr < 5 :
    GPIO.output(23, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)
    #enviar email(colocar o código da lista)
  else:
    if noite < 1:
      GPIO.output(21, GPIO.HIGH)
      time.sleep(.5)
      GPIO.output(23, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(23, GPIO.LOW)
      #enviar email
      time.sleep(5)
      GPIO.output(21, GPIO.LOW)
    else:
      GPIO.output(23, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(23, GPIO.LOW)
      #enviar email