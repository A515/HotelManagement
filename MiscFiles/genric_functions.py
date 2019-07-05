import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generic_string(length = 10):
    letter = string.ascii_letters
    pattern = "".join(random.choice(letter)for i in range(length))
    return pattern


def link_send(email, link, password):
    msg = MIMEMultipart()  # assign a variable to the multipart class

    msg['From'] = 'testdemo799@gmail.com'
    msg['To'] = email
    msg['Subject'] = "Multipart"

    body = "Your password is"+password+"Your Verify Link " + link
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('testdemo799@gmail.com', 'python@123')
    text = msg.as_string()
    server.sendmail('testdemo799@gmail.com', msg['To'], text)
    server.quit()
    print("Email Sent Successfully")