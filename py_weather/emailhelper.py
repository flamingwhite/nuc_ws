import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class GmailHelper:
    def __init__(self, username, password, fromuser):
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._server.ehlo()
        self._server.starttls()
        self._server.login(username, password)
        self._fromuser = fromuser
        self._sender = username

    def send_html_email(self, to, toname, subject, body):
        message = MIMEText(body, 'html')
        message['from'] = self._fromuser
        message['To'] = toname
        message['Subject'] = subject
        serilizable = message.as_string()
        self._server.sendmail(self._sender, to, serilizable)

    def send_img_email(self, to, toname, subject, body):
        message = MIMEMultipart('body')
        message['from'] = self._fromuser
        message['To'] = toname
        message['Subject'] = subject

        alternative = MIMEMultipart('alternative')
        message.attach(alternative)

        msgText = MIMEText('plain email text')
        alternative.attach(msgText)

        msgText = MIMEText('<img src="https://media.giphy.com/media/3o7abnemh3dNldgi5i/giphy.gif">', 'html')
        alternative.attach(msgText)

        msgText = MIMEText('<img src="http://i.imgur.com/6oGlPO9.gif">', 'html')
        alternative.attach(msgText)


        # msgText = MIMEText('<video width="300" height="200"> <source src="https://g.redditmedia.com/079TEfQFjyN65PGdL3D-sW4OeS0FJ1sVbDXM0wDUZms.gif?w=480&fm=mp4&mp4-fragmented=false&s=75cb224ec142aab06f2d03790e4ae8be"></video>', 'html')
        # alternative.attach(msgText)

        msgText = MIMEText('<video class="preview" preload="auto" autoplay="autoplay" muted="muted" loop="loop" webkit-playsinline="" style="width: 480px; height: 480px;"><source src="https://g.redditmedia.com/079TEfQFjyN65PGdL3D-sW4OeS0FJ1sVbDXM0wDUZms.gif?w=480&amp;fm=mp4&amp;mp4-fragmented=false&amp;s=75cb224ec142aab06f2d03790e4ae8be" type="video/mp4"></video>', 'html')
        alternative.attach(msgText)


        serilizable = message.as_string()
        self._server.sendmail(self._sender, to, serilizable)

    # def send_img_email(self, to, toname, subject, body):
    #     message = MIMEMultipart('body')
    #     message['from'] = self._fromuser
    #     message['To'] = toname
    #     message['Subject'] = subject

    #     alternative = MIMEMultipart('alternative')
    #     message.attach(alternative)

    #     msgText = MIMEText('plain email text')
    #     alternative.attach(msgText)

    #     msgText = MIMEText('<img src="https://media.giphy.com/media/3o7abnemh3dNldgi5i/giphy.gif">', 'html')
    #     # msgText = MIMEText('<img src="cid:image1">', 'html')

    #     alternative.attach(msgText)

    #     # fp = open('./imgs/giphy.gif', 'rb')
    #     # msgImg = MIMEImage(fp.read())
    #     # fp.close()

    #     # msgImg.add_header('Content-ID', '<image1>')
    #     # message.attach(msgImg)

    #     serilizable = message.as_string()
    #     self._server.sendmail(self._sender, to, serilizable)






# helper = GmailHelper('yongwang.cloud@gmail.com', 'Ever0702', 'Yong Wang <yongwang.cloud@gmail.com>')
# html = '<h1>Name</h1>'
# to = 'yongwang.cs@gmail.com'
# toname = 'Yong Wang <yongwang.cs@gmail.com>'
# subject = 'Greetings'

# helper.send_img_email(to, toname, subject, html)
