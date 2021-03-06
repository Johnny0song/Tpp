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
    phone = db.Column(db.String(40), default='',unique=True)
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


# 电影 模型类
class Movie(db.Model):
    __tablename__ = 'movies'
    # id
    id = db.Column(db.Integer, primary_key=True)
    # 电影中文名
    showname = db.Column(db.String(256))
    # 电影英文名
    shownameen = db.Column(db.String(256))
    # 导演
    director = db.Column(db.String(40))
    # 主演
    leadingRole = db.Column(db.String(256))
    # 类型
    type = db.Column(db.String(256))
    # 产地
    country = db.Column(db.String(40))
    # 语言
    language = db.Column(db.String(40))
    # 时长
    duration = db.Column(db.Integer)
    # 放映类型(2D/3D)
    screeningmodel = db.Column(db.String(40))
    # 上映时间
    openday = db.Column(db.Date)
    # 宣传图
    backgroundpicture = db.Column(db.String(256))
    # 标志位(0全部， 1热映， 2即将上映)
    flag = db.Column(db.String(4))
    # 是否删除
    isdelete = db.Column(db.Boolean)

# 影院 模型类
# insert into
# cinemas
# (,flag,isdelete)
# (,1,0);
class Cinema(db.Model):
    __tablename__='cinemas'
    # id
    id = db.Column(db.Integer, primary_key=True)
    # 影院名
    name = db.Column(db.String(100))
    # 城市
    city = db.Column(db.String(100))
    # 地区
    district = db.Column(db.String(40))
    # 详细地址
    address = db.Column(db.String(256))
    # 座机
    phone = db.Column(db.String(200))
    # 评分
    score = db.Column(db.Float)
    # 放映厅数量
    hallnum = db.Column(db.Integer)
    # 服务评分
    servicecharge = db.Column(db.Float)
    # 限制
    astrict = db.Column(db.Integer)
    # 标志位
    flag = db.Column(db.Integer)
    # 是否删除
    isdelete = db.Column(db.Boolean)