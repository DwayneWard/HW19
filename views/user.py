from flask_restx import Namespace, Resource

from implemented import user_service
from dao.model.user import UserSchema

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class DirectorsView(Resource):
    """
    Class-Based View для отображения режиссеров из БД.
    Реализовано:
    - отображение всех фильмов GET-запросом на /directors.
    """
    def get(self):
        """
        Метод реализует отправку GET-запроса на /directors.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        """
        all_directors = user_service.get_all()
        return users_schema.dump(all_directors), 200


@user_ns.route('/<uid>')
class DirectorView(Resource):
    """
    Class-Based View для отображения конкретного режиссера из БД.
    Реализовано:
    - отображение данных о конкретном режиссере GET-запросом на /directors/id;
    """
    def get(self, uid):
        """
        Метод реализует отправку GET-запроса на /directors/id.
        :param uid: id режиссера, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        user_by_id = user_service.get_one(uid)
        if user_by_id is None:
            return '', 404
        return user_schema.dump(user_by_id), 200
