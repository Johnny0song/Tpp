import time
from flask_restful import Resource, reqparse, fields, marshal_with

#请求格式定制
from werkzeug.security import generate_password_hash

from app.ext import cache
from app.models import User
from app.tools import save_db

parser = reqparse.RequestParser()
parser.add_argument('token', type=str)
parser.add_argument('parsecode', type=str, required=True, help='参数parsecode缺失')
parser.add_argument('newpassword', type=str, required=True, help='参数newpasswrod缺失')
parser.add_argument('phone', type=str, required=True, help='参数phone缺失')

#响应格式定制
result_fields ={
    'status':fields.Integer(default=200),
    'msg':fields.String,
    'date': fields.String(default=str(time.time()))

}

class PasswordResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        token = parse.get('token')
        parsecode = parse.get('parsecode')
        newpassword = parse.get('newpassword')
        phone = parse.get('phone')

        responseData ={}
        #根据手机号唯一约束来找到用户
        user = User.query.filter(User.phone==phone).first()
        print(user.name)

        #从缓存中拿到验证码
        temp_random = cache.get(phone)

        print(phone,type(phone),temp_random)

        if not temp_random:
            responseData['status'] = 400
            responseData['msg'] = '验证码超时，请重新获取验证码'

        elif str(temp_random) == str(parsecode):
            user.password = generate_password_hash(newpassword)
            save_db(user)
            responseData['status'] = 200
            responseData['msg'] = '修改密码成功'

        else:
            responseData['status'] = 400
            responseData['msg'] = '验证码错误，请重新输入'
        return responseData


