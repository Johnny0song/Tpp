from flask_restful import Resource, reqparse, marshal_with, fields

#请求格式定制
from app.ext import cache
from app.models import User
from app.tools import result_fields, save_db

parser = reqparse.RequestParser()
parser.add_argument('token',type=str,required=True,help='token参数缺失')

class activeResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()

        #不使用缓存，直接获取token
        #获取token
        # token = parse.get('token')
        #
        # user = User.query.filter(User.token==token).first()
        # user.is_active = True
        # save_db(user)
        # responseData = {
        #     'status': 201,
        #     'msg': '用户激活成功',
        #     'data': user
        # }
        #
        # return responseData

        #使用缓存超时处理

        token = parse.get('token')
        value = cache.get(token)

        if value:
            user = User.query.filter(User.token == token).first()
            user.is_active = True
            save_db(user)
            responseData = {
                'status': 200,
                'msg': '用户激活成功',
                'data': user
            }

            return responseData
        else:
            responseData ={
                'status': 201,
                'msg': '用户激活超时，请联系管理员',
            }
            return responseData