import time
from flask_restful import Resource, reqparse, fields, marshal_with

#请求格式定制
from app.models import Movie

parser = reqparse.RequestParser()
parser.add_argument('flag', type=str, default='0')

# 响应格式定制
movie_fields = {
    'id': fields.Integer,
    'showname': fields.String,
    'shownameen': fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.Integer,
    'screeningmodel': fields.String,
    'openday': fields.String,
    'backgroundpicture': fields.String,
    'flag': fields.String,
}

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'date': fields.String(default=str(time.time())),
    'data': fields.List(fields.Nested(movie_fields), default='')
}

class MovieResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        flag = parse.get('flag')
        print(flag)
        if int(flag):
            movie = Movie.query.filter(Movie.flag==flag)
        else:
            movie = Movie.query.all()
        responseData = {
            'status': 200,
            'msg': '电影列表获取成功',
            'data': movie
        }

        return responseData
