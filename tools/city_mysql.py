import json
import pymysql

'''
self, host=None, user=None, password="",
                 database=None, port=0, unix_socket=None,
               mi  charset='', sql_mode=None,
                 read_default_file=None, conv=None, use_unicode=None,
                 client_flag=0, cursorclass=Cursor, init_command=None,
'''

db = pymysql.connect(host='localhost',user='root',password='rock1204',database='Tppdb',charset='utf8',port=3306)
cursor = db.cursor()

with open('city.json','r') as f:
    #json序列化

    city_collection = json.load(f)
    '''
    {
        "A":Array[8],
        "B":Array[8],
        "C":Array[8],
    }
    '''
    #从json对象里获取city_collection
    returnValue = city_collection.get('returnValue')

    #获取所有的keys也就是字母
    letters = returnValue.keys()

    for key in letters:
        #讲对应的字母存入数据库
        #INSERT INTO letter(name) VALUES ('A')
        db.begin()
        cursor.execute("INSERT INTO letters(name) VALUES ('{}')".format(key))
        db.commit()

        #获取key 对应的id(因为后续插入城市时，需要设置外键)
        db.begin()
        cursor.execute("SELECT * FROM letters WHERE name='{}'".format(key))
        db.commit()

        letter_result = cursor.fetchone()
        # print(type(letter_result))
        letter_id = letter_result[0]

        #将字母对应的城市插入数据库
        letter_cities = returnValue.get(key)

        #遍历字母对应的城市
        for city in letter_cities:
            # print(city)
            #INSERT INTO citys(id,parentId,regionName,cityCode,pinYin) VALUES (2,1,'ss',1221,'dsd')
            db.begin()
            cursor.execute("INSERT INTO citys(id,parentId,regionName,cityCode,pinYin,c_letter) VALUES ({},{},'{}',{},'{}',{})".format(city.get('id'),city.get('parentId'),city.get('regionName'),city.get('cityCode'),city.get('pinYin'),letter_id))
            db.commit()





