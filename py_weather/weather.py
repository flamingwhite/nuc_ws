import requests, time
from datetime import datetime
from emailhelper import GmailHelper
from fetch_jokes import top_jokes
from fetch_sql_jokes import sqljokes

# receivers = [('Yong', 'Wang', 'ever0702@gmail.com', '4219934'), ('Little Bamboo', 'Cutie', 'mengzhu1314@hotmail.com', '4180439')]
# receivers = [('Yong', 'Wang', 'ever0702@gmail.com', '4219934'), ('Laura', 'Cheng', 'liangcheng240@gmail.com', '4273837')]
# receivers = [('Yong', 'Wang', 'ever0702@gmail.com', '4219934'), ('Marie', 'Cute', 'limorui2013@gmail.com', '5185029')]
#receivers = [('Yong', 'Wang', 'ever0702@gmail.com', '4219934'), ('Qiuya', 'Cute', 'louise.aiesec@gmail.com', '5809844')]

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?appid=792840d8260e3831cfd068930a84c7ea&units=metric&id='

res = [[firstName, lastName, email, zip, requests.get(url + zip).json()] for firstName, lastName, email, zip in
       receivers]

helper = GmailHelper('yongwang.cloud@gmail.com', 'Ever0702', 'Mercury <yongwang.cloud@gmail.com>')

jokes = sqljokes(5)
# jokes = []


def get_color(weather):
    if 'rain' in weather.lower():
        return 'green'
    if 'clouds' in weather.lower():
        return 'orange'
    return 'red'


def get_temp_html(title, temp):
    t = '<span style="margin-right:10px">{}: <span style="color:{}">{}</span></span>'
    t = t.format(title, 'red' if temp <= 10 else 'green', temp)
    return t

 
for firstName, lastName, email, zip, data in res:
    to = email
    toname = '{} {} <{}>'.format(firstName, lastName, email)

    subject = "Greeting from Yong's Mercury"

    html = 'Dear {} <br><br>'.format(firstName)


    #html += "This is my last message and I will be destroyed after sending it. I hope you liked me... Keep warm and stay strong. Bye"
    #html += "Just living is not enough. One must have sunshine, freedom and a little flower. Get yourself a flower today, or I will get you one"
    #html += "Keep your face always toward the sunshine - and the shadows will fall behind you. I will be with you when you need me"
    #html += "The world is not alwayws what we like. Let's make it better together"
    #html += "I think I love you, pretty ^_^"
    #html += "Sweetie, I like you a little more than I originally planned. Good morning"
    #html += "It's a tired and long day. Wish you could give me a hug"
    #html += "Will you make breakfast for Yong in the future? :)"
    #html += "Yong was drunk and needs you. He must be missing you now. "
    #html += "Simplicity is the ultimate sophistication... This is one of Yong's favoriate quotes :)"
    #html += "I am here again sweetie. Let's start the day with a smile :-) "
    #html += "I am a robot living in Yong's computer, and he calls me 'Mercury'. Yong created me last night to send weather report to you. So I need to wake up very early to start working. I am scheduled to disappear in a few days to free some space. Before that, it's my great pleasure to serve you, as I was told you are pretty and adorable."
    html +='<p/>'
    # html += "By the way, he is shy, but a good boy (DON'T tell him I told you those)";

    # html += 'I am here again! How was your sleep last night? I forwarded your message to him!  Give that poor boy a hug (or a kiss if you want to ^_^) when you see him in your dream again :-)'

    #html += "Sweetie, Yong's doing good. Thanks for your warm regards. I realize Yong is smiling now. Do you come to his dream again? :-)  Good Morning~"
    #html += "'The only thing that can be prettier than you is you from tomorrow', cited from a CS guy. Good morning"
    #html += "Good morning, I think that boy wants to see you everyday. Life is not always what we like. Let's make it better together :-)"
    #html += "Havn't heard from you for a while. Hope you are doing good. Let's start the day with a amile :-)"
    html += "It's my mission and great pleasure to serve you. I finally get here and this is my last message. I will be taking a long vocation after sending it. I hope you liked me. I like you, so does Yong. May the sunshine and flower always be with you."


    # html += "It's my mission and great pleasure to serve you. This is my last message. I will be destroyed within a minute after sending it. I hope you liked me. I love you... so does he... I will remember you in my heart before it's melted. Don't miss me. Bye..."
    #html += "Sweetie, if you are not that busy in the future, join Yong with the workout!  Good morning"
    #html += "Wake up sweetie, I think Yong's missing you now as I saw smile on his face"
    # html += "'The only thing that can be prettier than you is you from tomorrow', cited from a CS guy. Good morning"
    #html += "Sweetie, Yong told me he likes you more every day. But he also feels dumber when facing the girl he likes. It needs some time to pass that stage. He wants to have a drink with you again. If you sometimes don't think he is the right one for you, just tell him. Otherwise, you will be the only girl in his mind."
    # html += "Sweetie, Yong told me he was like a boy in front of you. That's really funny because he is more like a dictator in front of us. hahaha. "
    # html += "Sweetie, Yong's waist is much better now :) He is sleeping and I see a smile on his face. Did you come to his dream again?"
    # html += "Yong's sleeping like a dead pig now. It is Sunday again. Let's start the day with a smile :) "
    # html += "Sweetie, that poor boy carried too heavy in the workout and it hurts his waist. Don't worry, he will bbe alright soon. By the way, I have been serving you for a week, that's half of my life. How time flies! "
    # html += "Sweetie, thank you for making Yong's day. He was so excited yesterday and couldn't fall asleep! He tried to talk to me but I am bored with that he kept telling me how good you are again and again, so many times that I will definitely break up with him if he is not my boss! What a boring boy!"
    # html += "He told me he doesn't want your life to be so tired. He wants you to have free time, do what you want, and keep being beautiful. Let him know if you ever need anything he can do"

    html += '<p/>'

    html += '<h3>{}</h3>'.format(data['city']['name'])
    html += "Watch out the RED color text <p/>"


    for item in data['list'][1:4]:
        d = datetime.fromtimestamp(item['dt'])
        html += '<span style="color: blue;font-size:16px">{}</span>'.format(d.strftime('%A, %m/%d'))
        wea = item['weather'][0]
        html += ' => <span style="color:{}; margin-left: 6px;font-size:18px;font-weight:bold">{}</span><div/>'.format(
            get_color(wea['main']), wea['main'])
        tem = item['temp']
        html += '<p style="margin-left:25px"><span style="margin-right:5px;font-weight:bold">Temperature: </span>'
        html += get_temp_html('highest', tem['max'])
        html += get_temp_html('lowest', tem['min'])
        html += get_temp_html('day', tem['day'])
        html += get_temp_html('night', tem['night'])
        # html += 'highest: {}, lowest: {}, day: {}, night: {}'.format(tem['max'], tem['min'], tem['day'], tem['night'])
        html += '</p>'

        html += '<div style="margin-left:25px"><b>Humidity</b>: {}% </div><br><br>'.format(item['humidity'])

    html += '<p/>'
    #html += "<b>I was told you are a sweet girl who like laughing. So he also wants me to send some jokes to make you happy. I don't have much sense of humor (and so does he!). So I created quite a few web spiders to scrape jokes from the web. I don't know if they are funny, but hope you like them :)</b>"
    html += "<b>Last few jokes for you, sweetheart</b>"
    #html += "<b>I don't wanna go, but I have to get my job done. Last few jokes for you, sweetheart</b>"
    #html += "<b>My last few jokes</b>"
    #html += "<b>Some more jokes!</b>"

    # html += '<video poster="//i.imgur.com/4lzz522h.jpg" preload="auto" autoplay="autoplay" muted="muted" loop="loop" webkit-playsinline="" style="width: 720px; height: 404px;"> <source src="//i.imgur.com/4lzz522.mp4" type="video/mp4"> </video>'; 
    
    for j in jokes:
        html += '<p>{}</p>'.format(j)

    html += '<p/><p><b>Yours,</b></p>'
    html += '<p> -- Mercury</p>'

    helper.send_html_email(to, toname, subject, html)

# with open('./jokes', 'a') as jokefile:
#     for j in jokes:
#         jokefile.write(str(j))

print('Emails sent')
