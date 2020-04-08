from flask_restful import Resource


class Health(Resource):
    def get(self):
        return 'ok'


class HealthGAE(Resource):
    def get(self):
        return 'ok'