# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '07/11/2017 12:00 AM'
from random import Random
from django.core.mail import send_mail


from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    random_code = random_str(16)
    email_record.email = email
    email_record.code = random_code
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "暮学在线网注册激活连接"
        email_body = "请点击下方链接激活账号: http://127.0.0.1:8000/active/{0}".format(random_code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕学在线网注册密码重置"
        email_body = "请点击此链接重置密码：http://127.0.0.1:8000/reset/{0}".format(random_code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

def random_str(randomlength=8):
    strs = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        strs += chars[random.randint(0, length)]
    return strs
