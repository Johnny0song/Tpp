import time
from flask_restful import reqparse, fields, Resource, marshal_with

#请求格式定制
from app.models import Cinema

parser = reqparse.RequestParser()
parser.add_argument('city', type=str, default='全部')
parser.add_argument('district', type=str)
parser.add_argument('sort', type=int, default=1)    # 1按分数降序， -1 按分数升序
parser.add_argument('limit', type=int)

cinemas_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'district': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'score': fields.Float,
    'hallnum': fields.Integer,
    'servicecharge': fields.Float,
    'astrict': fields.Integer,
    'flag': fields.Integer,
}

result_fields = {
    'status': fields.Integer(default=200),
    'msg': fields.String,
    'date': fields.String(default=str(time.time())),
    'data': fields.List(fields.Nested(cinemas_fields), default='')
}



class CinemaResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        city = parse.get('city')
        district = parse.get('district')
        sort = parse.get('sort')
        limit_n = parse.get('limit')

        cinemas = []
        if limit_n:
            cinemas =Cinema.query.limit(limit_n)
        if sort == 1:   # 按分数降序
            cinemas = Cinema.query.order_by(-Cinema.score)
        elif sort == -1:    # 按分数升序
            cinemas = Cinema.query.order_by(Cinema.score)

        if city=='全部':
            cinemas = Cinema.query.all()
        else:
            cinemas = Cinema.query.filter(Cinema.city==city)

        if district:
            cinemas =Cinema.query.filter(Cinema.district==district)


        responseData={
            'msg':'影院获取成功',
            'data':cinemas
        }

        return responseData
