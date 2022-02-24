from flask import request
from flask_restx import Namespace, Resource

from implemented import user_service
from dao.model.user import UserSchema

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    """
    Class-Based View для отображения режиссеров из БД.
    Реализовано:
    - отображение всех пользователей GET-запросом на /users.
    """

    def get(self):
        """
        Метод реализует отправку GET-запроса на /users.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        """
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self) -> tuple:
        """
        Метод реализует отправку POST-запроса на /users.
        Записывает данные о новом пользователе с использованием переданных в формате JSON в теле POST-запроса.
        :return: Возвращает пустую строку и HTTP-код 201
        """
        json_data = request.json
        user_service.create(json_data)

        return '', 201


@user_ns.route('/<uid>')
class UserView(Resource):
    """
    Class-Based View для отображения конкретного пользователя из БД.
    Реализовано:
    - отображение данных о конкретном пользователе GET-запросом на /users/id;
    """
    def get(self, uid):
        """
        Метод реализует отправку GET-запроса на /users/id.
        :param uid: id пользователя, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        user_by_id = user_service.get_one(uid)
        if user_by_id is None:
            return '', 404
        return user_schema.dump(user_by_id), 200

    def put(self, uid: int) -> tuple:
        """
        Метод реализует PUT-запрос на /users/id.
        В теле запроса необходимо передать данные со всеми полями таблицы users, для обновления данных.
        :param uid: id пользователя, информацию о котором нужно заменить из БД.
        :return: Записывает в БД обновленные данные о конкретном пользователе.
        Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        json_data = request.json
        user_service.update(uid, json_data)

        return '', 204

    def delete(self, uid: int) -> tuple:
        """
        Метод реализует отправку DELETE-запроса на /users/id.
        :param uid: id пользователя, информацию о котором нужно удалить из БД.
        :return: Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        user_service.delete(uid)
        return '', 204
