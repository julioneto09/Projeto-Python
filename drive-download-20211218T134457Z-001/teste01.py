import RPi. GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #Modo como referenciar os pinos da placa (.BOARD pega o numero do pino da placa)

GPIO.setup(11, GPIO.OUT) #Saida digital #Iluminação

noite = int(input('1- Ligar o sistema de iluminação\n0-Sair'))
if noite == 1:
  tempo = int(input('Informe quantas segundos o sistema ficará ligado: '))
  GPIO.output(11, GPIO.HIGH)
  time.sleep(tempo)
  GPIO.output(11, GPIO.LOW)
  
