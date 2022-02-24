from flask import request
from flask_restx import Namespace, Resource

from helpers import auth_required, admin_required
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
    - запись в базу данных нового жанра POST-запросом на /genres.
    """

    @auth_required
    def get(self) -> tuple:
        """
        Метод реализует отправку GET-запроса на /genres.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        """
        all_directors = genre_service.get_all()
        return genres_schema.dump(all_directors), 200

    @admin_required
    def post(self) -> tuple:
        """
        Метод реализует отправку POST-запроса на /genres.
        Записывает данные о новом жанре с использованием переданных в формате JSON в теле POST-запроса.
        :return: Возвращает пустую строку и HTTP-код 201
        """
        json_data = request.json
        genre_service.create(json_data)

        return '', 201


@genre_ns.route('/<gid>')
class GenreView(Resource):
    """
    Class-Based View для отображения конкретного жанра из БД.
    Реализовано:
    - отображение данных о конкретном жанре GET-запросом на /genres/id;
    - изменение данных о конкретном жанре в БД PUT-запросом на /genres/id;
    - удаление фильма из БД DELETE-запросом на /genres/id.
    """

    @auth_required
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

    @admin_required
    def put(self, gid: int) -> tuple:
        """
        Метод реализует PUT-запрос на /genres/id.
        В теле запроса необходимо передать данные со всеми полями таблицы genres, для обновления данных.
        :param gid: id жанра, информацию о котором нужно заменить из БД.
        :return: Записывает в БД обновленные данные о конкретном жанре.
        Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        json_data = request.json
        genre_service.update(gid, json_data)

        return '', 204

    @admin_required
    def delete(self, gid: int) -> tuple:
        """
        Метод реализует отправку DELETE-запроса на /genres/id.
        :param gid: id жанра, информацию о котором нужно удалить из БД.
        :return: Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        genre_service.delete(gid)

        return '', 204
