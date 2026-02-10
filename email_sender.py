import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password

def send_email(receiver_email,content):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Test Email from Python 🚀"

    body = content
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP server
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

send_email(receiver_email, "Hieeeeee will you be my galentine!!!!")