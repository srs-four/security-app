import os
import smtplib

def sendr():
    recipient = os.environ['RECIPIENT']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    if username and password:
    # Connect to the server and send an emails
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)

        msg = "Intruder Alert!"
        server.sendmail(username, recipient, msg)
