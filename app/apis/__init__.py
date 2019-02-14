from flask_restful import Api

from app.apis.CinemaApi import CinemaResource
from app.apis.CityApi import CityResource
from app.apis.LoginApi import LoginResource
from app.apis.MesApi import MesResource
from app.apis.MovieApi import MovieResource
from app.apis.PasswordApi import PasswordResource
from app.apis.RegisterApi import RegisterResource
from app.apis.ActiveApi import activeResource
from app.apis.helloFlask import helloFlask

api = Api()
def init_apis(app):
    api.init_app(app)

# 添加资源
api.add_resource(helloFlask,'/api/v1/helloFlask/')

#添加区域资源
api.add_resource(CityResource,'/api/v1/city/')

#添加注册接口
api.add_resource(RegisterResource,'/api/v1/register/')

#添加激活接口
api.add_resource(activeResource,'/api/v1/active/')

#添加登录接口
api.add_resource(LoginResource,'/api/v1/login/')

#添加短信接口
api.add_resource(MesResource,'/api/v1/mes/')

#添加修改密码接口
api.add_resource(PasswordResource,'/api/v1/pwd/')

#添加电影接口
api.add_resource(MovieResource,'/api/v1/movie/')

#添加影院接口
api.add_resource(CinemaResource,'/api/v1/cinema/')