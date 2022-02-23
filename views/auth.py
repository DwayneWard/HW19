from flask import request, abort
from flask_restx import Namespace, Resource

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    """
    Класс CBV для представления auth. Реализованы методы POST и PUT.
    POST-метод: производит генерацию access и refresh tokens на основе запроса пользователя.
    PUT-метод: производит генерацию access и refresh tokens на основе refresh token, передаваемого в запросе
    """
    def post(self):
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')

        if None in [username, password]:
            abort(401)

        tokens = auth_service.generate_token(username, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")

        if refresh_token is None:
            abort(401)

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201
