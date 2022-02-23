from flask_restx import Namespace, Resource

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        pass

    def put(self):
        pass
