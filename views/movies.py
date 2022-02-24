from flask import request
from flask_restx import Namespace, Resource

from helpers import auth_required, admin_required
from implemented import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Class-Based View для отображения фильмов.
    Реализовано:
    - отображение всех фильмов GET-запросом на /movies;
    - отображение фильмов отфильтрованных по конкретному режиссеру
    (GET-запросом на /movies с использованием квери-параметра director_id);
    - отображение фильмов отфильтрованных по конкретному жанру
    (GET-запросом на /movies с использованием квери-параметра genre_id);
    - отображение фильмов отфильтрованных по конкретному году выпуска
    (GET-запросом на /movies с использованием квери-параметра year);
    - добавление нового фильма в базу данных POST-запросом на /movies.
    """

    @auth_required
    def get(self) -> tuple:
        """
        Метод реализует отправку GET-запросов на /movies.
        Возможные варианты исполнения:
        - отображение всех фильмов GET-запросом на /movies;
        - отображение фильмов отфильтрованных по конкретному режиссеру
        (GET-запросом на /movies с использованием квери-параметра director_id);
        - отображение фильмов отфильтрованных по конкретному жанру
        (GET-запросом на /movies с использованием квери-параметра genre_id);
        - отображение фильмов отфильтрованных по конкретному году выпуска
        (GET-запросом на /movies с использованием квери-параметра year);
        :return: Сериализованные данные в формате JSON, в зависимости от реализации запроса и HTTP-код 200
        """
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        # Фильтрация по режиссеру
        if director_id:
            movies_with_director = movie_service.get_all_on_director(director_id)
            return movies_schema.dump(movies_with_director), 200
        # Фильтрация только по жанру
        elif genre_id:
            movies_with_genre = movie_service.get_all_on_genre(genre_id)
            return movies_schema.dump(movies_with_genre), 200
        # Фильтрация по году выпуска
        elif year:
            movies_by_year = movie_service.get_all_by_year(year)
            return movies_schema.dump(movies_by_year), 200
        # Без фильтрации
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    @admin_required
    def post(self) -> tuple:
        """
        Метод реализует отправку POST-запроса на /movies.
        Записывает данные о новом фильме с использованием переданных в формате JSON в теле POST-запроса.
        :return: Возвращает пустую строку и HTTP-код 201
        """
        json_data = request.json
        movie_service.create(json_data)

        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    Class-Based View для отображения конкретного фильма из БД.
    Реализовано:
    - отображение данных о конкретном фильме GET-запросом на /movies/id;
    - изменение данных о конкретном фильме в БД PUT-запросом на /movies/id;
    - удаление фильма из БД DELETE-запросом на /movies/id.
    """

    @auth_required
    def get(self, mid: int) -> tuple:
        """
        Метод реализует GET-запрос на /movie/id.
        :param mid: id фильма, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        movie = movie_service.get_one(mid)
        if movie is None:
            return '', 404
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid: int) -> tuple:
        """
        Метод реализует PUT-запрос на /movie/id.
        В теле запроса необходимо передать данные со всеми полями таблицы movie, для обновления данных.
        :param mid: id фильма, информацию о котором нужно заменить из БД.
        :return: Записывает в БД обновленные данные о конкретном фильме.
        Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        json_data = request.json
        movie_service.update(mid, json_data)

        return '', 204

    @admin_required
    def delete(self, mid: int) -> tuple:
        """
        Метод реализует отправку DELETE-запроса на /movie/id.
        :param mid: id фильма, информацию о котором нужно удалить из БД.
        :return: Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        movie_service.delete(mid)
        return '', 204
