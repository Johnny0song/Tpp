import time
from flask_restful import Resource, fields, marshal_with, marshal

from app.models import City, Letter

# 请求格式定制


# 响应格式定制
'''
    responseData={
        'status' : 200,
        'msg' :'获取区域数据成功',
        'date':'',
        'data':{
            'A':[{
                    "id":3643,
                "parentId":0,
                "regionName":"阿坝",
                "cityCode":513200,
                "pinYin":"ABA"
                },
                {
                    "id":3643,
                "parentId":0,
                "regionName":"阿坝",
                "cityCode":513200,
                "pinYin":"ABA"
               },
               {
                    "id":3643,
                "parentId":0,
                "regionName":"阿坝",
                "cityCode":513200,
                "pinYin":"ABA"
               }],
            'B':[{},{},{}],
        }
    }
'''

########################## 方式一 ##########################
city_fields = {
                  "id": fields.Integer,
                  "parentId": fields.Integer,
                  "regionName": fields.String,
                  "cityCode": fields.Integer,
                  "pinYin": fields.String
              }

letter_fields = {
    'A': fields.List(fields.Nested(city_fields)),
    'B': fields.List(fields.Nested(city_fields)),
    'C': fields.List(fields.Nested(city_fields)),
    'D': fields.List(fields.Nested(city_fields)),
}

result_fields = {
    'status': fields.Integer(default=200),
    'msg': fields.String(default='区域数据获取成功'),
    'date': fields.String(default=str(time.time())),
    'data': fields.Nested(letter_fields),
    'num' : fields.Integer
}


# class CityResource(Resource):
#     @marshal_with(result_fields)
#     def get(self):
#         #所有字母
#         letters = Letter.query.all()
#         # print(letters)
#
#         #获取字母对应的城市信息
#         temp_dir = {
#             #一个字母对应多个城市
#             #'A': fields.List(fields.Nested(city_fields))
#         }
#         for letter in letters:
#             temp_dir[letter.name]=letter.citys
#         # print(temp_dir)
#         responseData ={
#             'data':temp_dir,
#             'num' : len(letters)
#         }
#         return responseData



########################## 方式二 ##########################

class CityResource(Resource):

    def get(self):
        #所有字母
        letters = Letter.query.all()
        # print(letters)

        #获取字母对应的城市信息
        # temp_dir = {
            #一个字母对应多个城市
            #'A': fields.List(fields.Nested(city_fields))
        # }

        temp_dir = {}    #动态letter_fields_dynamic数据源
        letter_fields_dynamic = {}   #动态格式定制

        for letter in letters:
            temp_dir[letter.name]=letter.citys
            letter_fields_dynamic[letter.name] = fields.List(fields.Nested(city_fields))
        print(temp_dir)

        result_fields_dynamic={
            'status':fields.Integer,
            'msg':fields.String,
            'date': fields.String(default=str(time.time())),
            'data': fields.Nested(letter_fields_dynamic),
            'num': fields.Integer

        }

        responseData ={
            'data':temp_dir,
            'num' : len(letters)
        }
        return marshal(responseData,result_fields_dynamic)
