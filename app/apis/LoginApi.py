from flask_restful import Resource,reqparse,marshal,marshal_with

#请求格式定制
from werkzeug.security import check_password_hash

from app.ext import cache
from app.models import User
from app.tools import active_mail, generate_token, save_db, result_fields

parser = reqparse.RequestParser()
parser.add_argument('email',type=str,required = True,help = 'email参数缺失')
parser.add_argument('password',type=str,required=True,help='password参数缺失')

class LoginResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        #获取数据
        parse = parser.parse_args()
        email = parse.get('email')
        password = parse.get('password')
        responseData ={}

        #获取用户
        users = User.query.filter(User.email==email)
        if users.count(): #有用户
            user = users.first()

            #密码校验
            if check_password_hash(user.password,password): #验证通过
                if user.is_delete == True: # 已删除
                    responseData['status'] = 401
                    responseData['msg'] = '登录失败，用户已被注销!'
                    return responseData
                if user.is_active == False: #未激活
                    #发送邮件
                    active_mail(user)

                    #缓存token
                    cache.set(user.token, '超时处理', timeout=30)

                    responseData['status'] = 401
                    responseData['msg'] = '用户未激活，请查看邮件激活后操作！'
                    return responseData

                    # 验证成功
                user.token = generate_token()
                save_db(user)

                responseData['status'] = 200
                responseData['msg'] = '登录成功'
                responseData['data'] = user
                return responseData

            else:
                responseData['status'] = 401
                responseData['msg'] = '登录失败，密码错误!'
                return responseData

        else:  #没有用户
            responseData['status'] =401
            responseData['msg'] = '邮箱错误，请重新登录'
            return responseData