import random
import time
from flask_restful import reqparse, fields, Resource, marshal_with

#请求格式定制
from app.ext import cache

parser=reqparse.RequestParser()
parser.add_argument('phone',type=str,required=True,help = 'phone缺失')

#响应格式定制
result_fields ={
    'status':fields.Integer(default=200),
    'msg':fields.String,
    'date': fields.String(default=str(time.time()))

}

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

class MesResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        phone = parse.get('phone')


        # 短信应用SDK AppID
        appid = 1400112809  # SDK AppID是1400开头

        # 短信应用SDK AppKey
        appkey = "8d8b808cb9073023631d241951f49fb4"

        # 需要发送短信的手机号码
        phone_numbers = [phone]


        # 短信模板ID，需要在短信应用中申请
        template_id = 166915  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
        # templateId 7839 对应的内容是"您的验证码是: {1}"
        # 签名
        sms_sign = "钟远智工作经验分享"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`


        ssender = SmsSingleSender(appid, appkey)

        # 模板需要的参数
        # 短信验证码: {1}，请于{2}分钟内填写。如非本人操作，请忽略本短信。

        temp_random = random.randrange(10000,100000)

        # 缓存验证码(后续过期处理，以及验证处理)
        cache.set(phone, temp_random, timeout=30)
        print(phone,cache.get(phone),type(phone))

        params = [temp_random,10]  # 当模板没有参数时，`params = []`，数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
        try:
            result = ssender.send_with_param(86, phone_numbers[0],
                                             template_id, params, sign=sms_sign, extend="",
                                             ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

        responseData={
            'msg':'发送短信成功'
        }

        return responseData
