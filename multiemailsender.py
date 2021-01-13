import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "from@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("username", "password")

with open('addresses.csv') as f:
    emails = [line.rstrip() for line in f]

for i in emails:
	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = i
	msg['Subject'] = "subject"

	body = "body text"

	msg.attach(MIMEText(body, 'plain'))

	filename = "fileName"
	attachment = open("D:\\pdf.pdf", "rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)

server.quit()