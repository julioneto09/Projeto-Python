import smtplib

email_destino=[]
while True:
    print('\n1. Adicionar email\n2. Finalizar')
    op=int(input('Que operação deseja realizar: '))
    if op==1:
        while True:
            try:
                de=input('Informe um email de destino: ')
                email_destino.append(de)
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break
    elif op == 2:
        print('saindo...')
        break
    else:
        print('1 ou 2')
        continue

email_origem = input('\nInforme o email: ')
senha = input('\nSenha do email: ')

try:
    sm = smtplib.SMTP('smtp.gmail.com', 587)
    sm.ehlo()
    sm.starttls()
    sm.login(email_origem, senha)
    mensagem = 'Enviar anexo...'                
    sm.sendmail(email_origem,email_destino,'Subject: Aletra da câmera de segurança\n{}'.format(mensagem))
    print('Email enviado!')
    sm.quit()
except:
    print('Erro ao enviar e-mail')
