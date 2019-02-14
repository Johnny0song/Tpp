
import hashlib
import random
import time

#生成token
from flask import render_template
from flask_mail import Message
from flask_restful import fields

from app.ext import mail, db


def generate_token():
    md5 = hashlib.md5()
    temp = str(int(time.time())) + str(random.random)
    md5.update(temp.encode('utf8'))
    return md5.hexdigest()


# 响应格式定制
'''
responseData={

    'status':200,
    'msg':'注册成功',
    'date' :'',
    'data':{
        'id':1001,
        'name':'李四',
        'icon':'head.png',
        'token':''
    }
}
'''
class IconFormat(fields.Raw):
    def format(self, value):
        return '/static/img/' + value


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'icon': IconFormat(attribute='icon'),
    'token': fields.String
}

result_fields = {

    'status': fields.Integer,
    'msg': fields.String,
    'date': fields.String(default=str(time.time())),
    'data': fields.Nested(user_fields, default='')
}

#发送邮箱
def active_mail(user):
    msg = Message(
        'Tpp邮件激活',
        recipients=[user.email]
    )
    msg.html = render_template('active.html', name=user.name,
                               active_url='http://127.0.0.1:5000/api/v1/active/?token=' + user.token)
    # print(type(render_template('active.html')))
    mail.send(msg)

#存入数据库
def save_db(obj):
    db.session.add(obj)
    db.session.commit()





