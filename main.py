import smtplib
import config
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


with open('password.txt', 'r') as f:
    password = f.read()


server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo()
server.starttls()
server.login(config.EMAIL_ADDRESS, config.PASSWORD)

# Enviar mensagem
msg = MIMEMultipart()
msg['From'] = 'Jefferson_Gatinho'  # Não é tão necessário
msg['To'] = 'lazumbra@gmail.com'
msg['Subject'] = 'Just a Test'


with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# Enviar uma foto
filename = 'pics.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('lazumbra@gmail.com', 'lazumbra@gmail.com', text)
