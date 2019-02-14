
from flask import render_template
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with

#请求格式定制
from werkzeug.security import generate_password_hash

from app.ext import db, mail, cache
from app.models import User
from app.tools import result_fields, generate_token, active_mail, save_db

parser = reqparse.RequestParser()

parser.add_argument('name',type=str,required=True,help='name参数缺失')
parser.add_argument('password',type=str,required=True,help='password参数缺失')
parser.add_argument('email',type=str,required=True,help='email参数缺失')
parser.add_argument('phone',type=str)



class RegisterResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()

        #用户信息
        user = User()
        user.name = parse.get('name')
        user.password = generate_password_hash(parse.get('password'))
        user.email = parse.get('email')
        user.phone = parse.get('phone')
        user.token = generate_token()

        #存入数据库(考虑账户邮箱有唯一约束，要捕获异常)
        try:
            #存入数据库
            save_db(user)

            responseData = {}
            responseData['status'] = 200
            responseData['msg'] = '注册成功'
            responseData['data'] = user

            #发送邮箱
            active_mail(user)

            #缓存设置
            cache.set(user.token,'超时处理',timeout=30)


            return responseData

        except Exception as e:
            responseData = {}
            responseData['status'] = 406
            responseData['msg'] = '该邮箱已经被占用'
            return responseData


