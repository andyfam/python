import smtplib

sender = "andyfam@gmail.com"
receiver = "yufeng.fan229@gmail.com"
password = "190706&famN"
subject = "Python email test"
body = "I wrote an email!"

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

# this method may not available because of the gmail update, use oauth2 instead
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in!")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in!")