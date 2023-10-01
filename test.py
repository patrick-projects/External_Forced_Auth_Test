import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


gmail_user = 'user@gmail.com'
gmail_password = 'Create App Password- Put Here'

text = """From: fname lname <fname.lname1990@gmail.com>
Subject: Meeting Agenda
Do you have time Monday or Tuesday to discuss the meeting agenda?

I'd like to review what I have put together so far when you get a chance.

Also, found this picture online. Is this you?


Thanks,
Name here

    """
    
html= """
            <META HTTP-EQUIV="Content-Type" CONTENT="text/html; CHARSET=UTF-8">
Do you have time Monday or Tuesday to discuss the meeting agenda for next week?<BR>
<BR>
I'd like to review what I have put together so far when you get a chance.
<BR>
<BR>
Also, found this picture online. Is this you?
<BR>
<BR>
<BR>
<BR>
Thanks,<BR>
Janice Lynne<BR>
<IMG SRC="\\165.227.82.135\images__ID__\logo.gif" ALIGN="bottom" BORDER="0">
<IMG SRC="https://165.227.82.135/images__MESSAGE_ID__/logo.gif" ALIGN="bottom" BORDER="0">
            """


with open('test.email', 'r') as f:
  for line in f:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Meeting Agenda"
    msg['From'] = gmail_user
    msg['To'] = line
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    mail = MIMEMultipart('alternative')
    sent_from = gmail_user
    subject = 'Meeting Agenda'
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, line, msg.as_string())
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
