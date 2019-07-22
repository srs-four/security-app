import smtplib

recipient = "shahidmmed@gmail.com"
username = "mysecurwork@gmail.com"
password = "securitysys123."


def sendr():
    if username and password:
    # Connect to the server and send an emails
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)

        msg = "Intruder Alert!"
        server.sendmail(username, recipient, msg)
        

sendr()