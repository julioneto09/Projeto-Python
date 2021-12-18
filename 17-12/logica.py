import time
import ex_en
import servidor_get as sget

'''Como no simulador não conseguimos mudar o estado das entradas,
forçamos os valores para poder testar'''

sensor = 3 #GPIO = 3
ldr = 5 #GPIO = 5

'''Se o sistema de iluminação for ativado (=1),  a lampada é ativada e
fica ligado por n tempo'''
noite = int(input('1- Ligar o sistema de iluminação\n0-Sair'))
if noite == 1:
  dicionario = sget.servidor()
  tempo = dicionario['tempo_funcionamento']
  if(dicionario['enviar_email']==1):
      ex_en.enviar_email('aaaaaaaaaaaaa ',dicionario['email'])
  
  #post
  if(dicionario['tempo_segunda_inicio'] >= hora_atual and
     dicionario['tempo_segunda_fim'] <= hora_atual and dia_semana == 'monday' )
  
#ccolocar sleep