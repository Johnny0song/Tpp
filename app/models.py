from app.ext import db


class Letter(db.Model):
    __tablename__= 'letters'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(40))

    # 字母对应的城市
    citys = db.relationship('City',backref='letter')
    def save(self):
        db.session.add(self)
        db.session.commit()

class City(db.Model):
    __tablename__= 'citys'
    '''
    {
                "id":3643,
                "parentId":0,
                "regionName":"阿坝",
                "cityCode":513200,
                "pinYin":"ABA"
            },
    '''
    id = db.Column(db.Integer, primary_key=True)
    parentId =db.Column(db.Integer)
    regionName = db.Column(db.String(40))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(40))
    # 外键(哪个字母下)
    c_letter = db.Column(db.Integer,db.ForeignKey(Letter.id))

    def save(self):
        db.session.add(self)
        db.session.commit()

# 用户 模型类
class User(db.Model):
    __tablename__='users'
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名字
    name = db.Column(db.String(40))
    # 密码
    password = db.Column(db.String(255))
    # 邮箱
    email = db.Column(db.String(40), unique=True)
    # 手机号
    phone = db.Column(db.String(40), default='')
    # 头像
    icon = db.Column(db.String(100), default='head.png')
    # 是否激活
    is_active = db.Column(db.Boolean, default=False)
    # 权限
    permisstion = db.Column(db.Integer,default=1)
    # 令牌
    token = db.Column(db.String(256))
    # 是否删除
    is_delete = db.Column(db.Boolean, default=False)