from flask_restx import Namespace, Resource

from implemented import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
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
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<did>')
class DirectorView(Resource):
    """
    Class-Based View для отображения конкретного режиссера из БД.
    Реализовано:
    - отображение данных о конкретном режиссере GET-запросом на /directors/id;
    """
    def get(self, did):
        """
        Метод реализует отправку GET-запроса на /directors/id.
        :param did: id режиссера, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        director_by_id = director_service.get_one(did)
        if director_by_id is None:
            return '', 404
        return director_schema.dump(director_by_id), 200
