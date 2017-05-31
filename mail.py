#!/usr/bin/env python
# -*- coding: utf-8 0*0

import requests
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

base_url = 'https://hacker-news.firebaseio.com'
stories_file = 'stories.txt'
mails_file  = 'sendingto.txt'
sending_mail = ''
with open(stories_file) as f:
    meanwhile_stories = f.read().splitlines()
with open(mails_file) as f:
    mails = f.read().splitlines()

current_mail = ''

for s in meanwhile_stories:
    try:
        story = requests.get(base_url + '/v0/item/'+str(s)+'.json').json()
        print('add story :{0}'.format(str(s)))
        msg = ""
        if 'url' in story:
            msg = str(s) + '  -  ' + story['title'] + '  -  ' + story['url'] + ' comments : https://news.ycombinator.com/item?id='+ str(s)  +' \n'
            print(msg)
        else:
            msg = str(s) + ' - ' + story['title'] +  ' comments : https://news.ycombinator.com/item?id='+ str(s) + '\n'
            print(msg)
        current_mail+=msg
    except:
        print("Error for "+str(s))
print('=================')
if current_mail is not "":
    for mail in mails:
        try:
            if mail is not "":
                print(mail)
                email  = MIMEText(current_mail)
                email['Subject'] = "HN News Recap"
                email['From'] = sending_mail 
                email['To'] = mail
                s = smtplib.SMTP("localhost");
                s.sendmail(sending_mail, mail ,email.as_string())
                s.quit()
                print("Mail sent")
        except Exception as e:
            print("Error for :"+mail+" "+str(e));

 
with open(stories_file, 'w') as f:
	f.write('')

