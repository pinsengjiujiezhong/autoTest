#coding=utf-8
'''
Created on 2018年7月1日
@author: kai.yang
'''
from selenium import webdriver
import time
import  smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(mailDict,ResultReport):
    sender, receiver, subject = mailDict['sender'], mailDict['receiver'], mailDict['subject']
    with open('../Testdata/test.html','rb') as f:
        lines = f.read()
    for key in ResultReport.keys():
        if not isinstance(ResultReport[key], list):
            # lines = lines.replace(key.encode('utf-8'), str(ResultReport[key]).encode('utf-8'))
            lines = lines.replace(key.encode('utf-8'), str(ResultReport[key]).encode('utf-8'))
    psw='xirdblxjymitbcbc'
    smtp_server='smtp.qq.com'
    message = MIMEMultipart()
    message['From'] = Header('autotester <%s>'%sender)
    message['To'] =  Header("tester <test@test.com>")
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(lines, 'html', 'utf-8'))
    att1 = MIMEText(open('../Report/CaseReport.html', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="autotestReport.html"'
    message.attach(att1)
    server=smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.starttls()
    server.login(sender,psw)
    server.sendmail(sender,receiver,message.as_string())
    server.quit()
