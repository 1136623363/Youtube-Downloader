import ssl
import requests
import json
from flask import jsonify
from flask import Flask, request
# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header
from email.message import EmailMessage
import schedule
import time
from threading import Timer
import datetime



def send(body):
    # 这里我调用接口了，如果不调用 可以直接删除
    #xg_url = ''
    # 无需安装第三方库
    key = 'hmabfuonsyzrbadg'  # 换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)
    EMAIL_ADDRESS = '1136623363@qq.com'  # 换成你的邮箱地址
    EMAIL_PASSWORD = key
    smtp = smtplib.SMTP('smtp.qq.com', 25)
    context = ssl.create_default_context()
    sender = EMAIL_ADDRESS  # 发件邮箱
    receiver = [ '1136623363@qq.com']#,'cb1136623363@gmail.com', '2020281102@email.szu.edu.cn']
    # 收件邮箱

    subject = f"{str(datetime.datetime.now())} 上传成功"
    # 这里我调用了自己的接口，如果不需要直接将body改为 body = '正文'
    #body = TextBody(download,filename,upload)#requests.get(xg_url).text
    msg = EmailMessage()
    msg['subject'] = subject  # 邮件主题
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)  # 邮件内容

    with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def TextBody(download,filename,upload):
    if download == 1 :
        if upload == 200 :
            Body = f'{filename} 上传成功'
        elif upload != 200 :
            Body = f'{filename} 下载成功，上传失败'
    elif download == -1:
        Body = f'{filename} 下载失败'
    return Body

