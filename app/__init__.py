from app.apis import init_apis
from app.ext import init_ext
from app.settings import init_app


def create_app(env_name='default'):
    from flask import Flask

    app = Flask(__name__)
    # 配置
    init_app(app,env_name)


    init_ext(app)

    #api接口
    init_apis(app)

    return app