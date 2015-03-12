# Dev Hugo Espinosa

import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = ("hugo@softcoders.mx")
password = getpass.getpass("Password: ")

# Variables para las cabeceras de email
remitente = ("hugo@softcoders.mx")
destinatarios = ("<hugo@softcoders.mx>", "<hector@softcoders.mx>")
asunto = ("New Commit")
mensaje = ("New commit test webhook")

# Servidor Smtp & Puerto Smtp
gmail = smtplib.SMTP("smtp.gmail.com", 587)

# Protocolo de sifrado de datos utilizado por gmail:
gmail.starttls()

# Credenciales del usuario:
gmail.login(user, password)

# Muestra la depuracion (a medida que se envia el email)
gmail.set_debuglevel(1) # 1 = True

# Cabecera de email
header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = ",".join(destinatarios)

mensaje = MIMEText(mensaje, 'html') # Tipo de mensaje (HTML)(Plain)
header.attach(mensaje) # Agregamos el mensaje a la cabeceras

# Enviar email
gmail.sendmail(remitente, destinatarios, header.as_string())

# Cerrar la conexion SMTP
gmail.quit()