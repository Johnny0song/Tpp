import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(BaseConfig):
    DEBUG = True
    # 'mysql+pymysql://root:123456@localhost:3306/HelloFlask'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@localhost:3306/Tppdb'
    MAIL_SERVER='smtp.163.com'
    MAIL_DEFAULT_SENDER ='18281961891@163.com'
    MAIL_USERNAME = '18281961891@163.com'
    MAIL_PASSWORD ='sj123456'

config = {
    'develop' : DevelopConfig,
    'default' : DevelopConfig,
}
def init_app(app,env_name):
    app.config.from_object(config.get(env_name))