# -*- coding:utf-8 -*-

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

from typing import NewType, Tuple

# 用户名和密码Tuple(username, password)
Credential = NewType("Credential", Tuple[str, str])
# SMTP (host, port, use_tls)
SmtpServer = NewType("SmtpServer", Tuple[str, int, bool])
# Message = ("发件人邮箱", "发件人姓名", "收件人邮箱", "收件人姓名", "主题", "内容")
Message = NewType("Message", Tuple[str, str, str, str, str, str])


def sendmail(credential: Credential, smtp: SmtpServer, message: Message):
    # Create the message
    msg = MIMEText(message[5])
    msg.set_unixfrom(message[1])
    msg['To'] = email.utils.formataddr((message[3], message[2]))
    msg['From'] = email.utils.formataddr((message[1], message[0]))
    msg['Subject'] = message[4]
    if smtp[2]:
        print('正在建立一个安全连接...')
        server = smtplib.SMTP_SSL(smtp[0], smtp[1])
    else:
        print('正在建立一个不安全的连接...')
        server = smtplib.SMTP(smtp[0], smtp[1])
    try:
        server.set_debuglevel(True)
        # identify ourselves, prompting server for supported features
        server.ehlo()
        # If we can encrypt this session, do it
        if server.has_extn('STARTTLS'):
            print('starting TLS...')
            server.starttls()
            server.ehlo()  # reidentify ourselves over TLS connection
        else:
            print('no STARTTLS')
        if server.has_extn('AUTH'):
            print('开始登录邮箱...')
            server.login(credential[0], credential[1])
        else:
            print('信息认证失败')
        server.sendmail(message[0], [message[2]], msg.as_string())
    finally:
        server.quit()


if __name__ == "__main__":
    password = getpass.getpass("请输入您的的邮箱密码: ")
    credential: Credential = ("username@mail.com", password)
    smtp: SmtpServer = ("smtp.mxhichina.com", 465, True)
    message: Message = ("author@mail.com", "发件人姓名", "recipient@mail.com",
                        "收件人姓名", "主题", "内容")
    sendmail(credential=credential, smtp=smtp, message=message)
