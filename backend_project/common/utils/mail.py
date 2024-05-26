import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def send_email(target, byte_file, file_name, processing_service_name):
    subject = processing_service_name
    mail = "platformuunit@mail.ru"
    text = "Добрый день! Отправляем Вам результаты анализа"

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(mail, 'AzxKRj56TiH6LE8ucfFa')

    msg = MIMEMultipart()
    msg['From'] = mail
    msg['To'] = target
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    part = MIMEApplication(
        byte_file,
        Name=file_name
    )
    part['Content-Disposition'] = 'attachment; filename="%s"' % 'report.pdf'
    msg.attach(part)

    server.sendmail(mail, target, msg.as_string())
    server.quit()
    server.close()