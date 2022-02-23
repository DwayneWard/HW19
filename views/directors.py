from flask import request
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

    def post(self) -> tuple:
        """
        Метод реализует отправку POST-запроса на /movies.
        Записывает данные о новом фильме с использованием переданных в формате JSON в теле POST-запроса.
        :return: Возвращает пустую строку и HTTP-код 201
        """
        json_data = request.json
        director_service.create(json_data)

        return '', 201


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

    def put(self, did: int) -> tuple:
        """
        Метод реализует PUT-запрос на /movie/id.
        В теле запроса необходимо передать данные со всеми полями таблицы movie, для обновления данных.
        :param did: id режиссера, информацию о котором нужно заменить из БД.
        :return: Записывает в БД обновленные данные о конкретном фильме.
        Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        json_data = request.json
        director_service.update(did, json_data)

        return '', 204

    def delete(self, did: int) -> tuple:
        """
        Метод реализует отправку DELETE-запроса на /movie/id.
        :param did: id режиссера, информацию о котором нужно удалить из БД.
        :return: Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        director_service.delete(did)

        return '', 204
