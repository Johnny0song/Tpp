from flask_restful import Resource


class helloFlask(Resource):
    def get(self):
        return {'msg':'hello flask'}