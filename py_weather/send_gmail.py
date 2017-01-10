#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText


TO = 'yongwang.cs@gmail.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'yongwang.cloud@gmail.com'
gmail_passwd = 'Ever0702'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])


title = 'My title'
msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)

content = '<span>Dear {name}</span>'.format(name='Yong')
msg_content+=content

message = MIMEText(msg_content, 'html')

message['From'] = 'Mercury Wang <yongwang.cloud@gmail.com>'
message['To'] = 'Yong Wang <yongwang.cs@gmail.com>'
# message['Cc'] = 'Receiver2 Name <receiver2@server>'
message['Subject'] = 'Any subject'

msg_full = message.as_string()

try:
    server.sendmail(gmail_sender, [TO], msg_full)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()