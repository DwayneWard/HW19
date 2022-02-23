from flask import request
from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """
    Class-Based View для отображения жанров из БД.
    Реализовано:
    - отображение всех фильмов GET-запросом на /genres.
    """
    def get(self):
        """
        Метод реализует отправку GET-запроса на /genres.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        """
        all_directors = genre_service.get_all()
        return genres_schema.dump(all_directors), 200

    def post(self) -> tuple:
        """
        Метод реализует отправку POST-запроса на /movies.
        Записывает данные о новом фильме с использованием переданных в формате JSON в теле POST-запроса.
        :return: Возвращает пустую строку и HTTP-код 201
        """
        json_data = request.json
        genre_service.create(json_data)

        return '', 201


@genre_ns.route('/<gid>')
class GenreView(Resource):
    """
    Class-Based View для отображения конкретного режиссера из БД.
    Реализовано:
    - отображение данных о конкретном режиссере GET-запросом на /genres/id;
    """
    def get(self, gid):
        """
        Метод реализует отправку GET-запроса на /genres/id.
        :param gid: id жанра, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        genre_by_id = genre_service.get_one(gid)
        if genre_by_id is None:
            return '', 404
        return genre_schema.dump(genre_by_id), 200

    def put(self, gid: int) -> tuple:
        """
        Метод реализует PUT-запрос на /movie/id.
        В теле запроса необходимо передать данные со всеми полями таблицы movie, для обновления данных.
        :param gid: id жфнра, информацию о котором нужно заменить из БД.
        :return: Записывает в БД обновленные данные о конкретном фильме.
        Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        json_data = request.json
        genre_service.update(gid, json_data)

        return '', 204

    def delete(self, gid: int) -> tuple:
        """
        Метод реализует отправку DELETE-запроса на /movie/id.
        :param gid: id жанра, информацию о котором нужно удалить из БД.
        :return: Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        genre_service.delete(gid)

        return '', 204
