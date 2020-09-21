# Responde um email obtido na lista  de emails na caixa de entrada

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "EMAIL do Remetende"
toaddr = "EMAIL  do Destinatário"

# instancia do MIMEMultipart 
msg = MIMEMultipart() 

# armazena o endereço do remetente
msg['De'] = fromaddr 

# armazena o endereço do Destinatario
msg['Para'] = toaddr 

# armazena o assunto
msg['Assunto'] = "assunto do email"

# string para armazenar o corpo da mensagem 
body = "Corpo do email"

# anexa o corpo do email com o restante da mensagem 
msg.attach(MIMEText(body, 'plain')) 

# abre o arquivo para envio 
filename = "lista de email.txt"
attachment = open("lista de emails.txt", "rb") 

# instancia de MIMEBase e nomeada como p 
p = MIMEBase('application', 'octet-stream') 

# Muda payload pra formulario codificado
p.set_payload((attachment).read()) 

# codificado em base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# anexa instancia 'p' para instancia 'msg' 
msg.attach(p) 

# cria uma sessão SMTP 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# Inicia TSL para segurança
s.starttls() 

# Authentica
s.login(fromaddr, "Password_of_the_sender") 

# Converte a mensagem em uma string 
text = msg.as_string() 

# envia o email
s.sendmail(fromaddr, toaddr, text) 

# termina a sessão
s.quit() 
