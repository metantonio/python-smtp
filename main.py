import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



smtp_address = 'smtp.gmail.com'
smtp_port = 465

email_address = "email@gmail.com"
email_password = "password" ##aquí va el codigo de aplicacion generado por google
print(email_address)
email_receiver = 'destinatario@hotmail.com'

# al crear un e-mail
message = MIMEMultipart("alternative")
# Asunto
message["Subject"] = "[DataScientest] e-mail essai"
# el que envía
message["From"] = email_address
# el correo de quién recibe
message["To"] = email_receiver

# on crée un texte et sa version HTML
texte = '''
Bonjour 
Ma super newsletter
Cdt
mon_lien_incroyable
'''

html = '''
<html>
<body>
<h1>Hola</h1>
<p>Nueva Carta</p>
<b>Cdt</b>
<br>
<a href="https://www.github.com/metantonio">Link a una página</a>
</body>
</html>
'''

# crea elemento MIMEText 
texte_mime = MIMEText(texte, 'plain')
html_mime = MIMEText(html, 'html')

# adjunta
message.attach(texte_mime)
message.attach(html_mime)

# conecta  envía
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:  
    server.login(email_address, email_password)  
    server.sendmail(email_address, email_receiver, message.as_string())
