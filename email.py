# modules
import smtplib
from email.message import EmailMessage

# content
sender = input("enter email address: ")
receiver = input("Enter Email address: ")
password = input("Enter The Password: ")
msg_body = input(str("Type Your message here: "))

# action
msg = EmailMessage()
msg['subject'] = input(str("Enter the subject of E-Mail: "))
msg['from'] = sender
msg['to'] = receiver
msg.set_content(msg_body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)

    smtp.send_message(msg)
