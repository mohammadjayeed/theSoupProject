
def send(filename):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from dotenv import dotenv_values

    config = dotenv_values(".env")
    from_address = config["ADDR"]
    to_address = config["TO"]
    subject = config["SUBJECT"]
    body = "<h1>Welcome to the Finance Club</h1>"
    password = config["PASS"]

    message = MIMEMultipart()

    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(body,'html'))

    file = open(filename, 'rb')

    # upload attachment
    part = MIMEBase('application','octet-stream')

    part.set_payload(file.read())

    # read the byte stream and encode the attachment
    encoders.encode_base64(part)

    part.add_header('Content-Disposition','attachment; filename='+filename)
    message.attach(part)
    file.close()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_address,password)

    server.sendmail(from_address,to_address,message.as_string())
