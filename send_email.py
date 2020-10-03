#Function to send email with an attachment using the library smtplib
#google is not allowing you to log in via smtplib because
# it has flagged this sort of login as "less secure",
# so what you have to do is go to this link while you're logged in to your google account, and allow the access:
#https://www.google.com/settings/security/lesssecureapps


import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(gmail_user,gmail_password,receiver_email):

    body = "This is an email with attachment"
    message = MIMEMultipart()
    message["Subject"] = "email from {0}".format(gmail_user)
    message["From"] = gmail_user
    message["To"] = receiver_email
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    # file name should be in same directory as script
    filename = "dummy.pdf"
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    try:
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as server:
            server.login(gmail_user, gmail_password)
            print("logged in")
            server.sendmail(gmail_user, receiver_email, message.as_string())
    except:
        print('Something went wrong and the email is not send successfully')

gmail_user = input("enter gmail_user")
gmail_password = input("enter your password")
receiver_email = input("enter reciever user")
print(send_email(gmail_user,gmail_password,receiver_email))
