from dao.movie import MovieDAO


class MovieService:
    """
    Класс описывает сервисы для работы в приложении Flask с таблицей фильмов.
    """
    def __init__(self, dao: MovieDAO):
        """
        Метод инициализирует DAO
        :param dao: DAO объект
        """
        self.dao = dao

    def create(self, data: dict) -> None:
        """
        Метод реализует запись новых данных в базу данных.

        :param data: Данные, которые необходимо записать в базу данных.
        :return: None
        """
        return self.dao.create(data)

    def get_one(self, mid: int) -> None or list:
        """
        Метод реализует получение записи об одном фильме из базы данных по id.

        :param mid: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о фильме по id.
        При отсутствии id в базе данных возвращает None.
        """
        movie = self.dao.get_one(mid)
        if not movie:
            return None
        return movie

    def get_all(self) -> list:
        """
        Метод реализует получение записей о всех фильмах из базы данных.

        :return: Ответ базы данных на запрос получения данных о всех фильмах.
        """
        return self.dao.get_all()

    def get_all_on_director(self, director_id: int) -> list:
        """
        Метод реализует получение записей о всех фильмах по конкретному режиссеру.

        :param director_id: id режиссера в базе данных.
        :return: Ответ базы данных на запрос к базе данных.
        """
        return self.dao.get_all_on_director(director_id)

    def get_all_on_genre(self, genre_id: int) -> list:
        """
        Метод реализует получение записей о всех фильмах по конкретному жанру.

        :param genre_id: id жанра к базе данных.
        :return: Ответ базы данных на запрос.
        """
        return self.dao.get_all_on_genre(genre_id)

    def get_all_by_year(self, year: int) -> list:
        """
        Метод реализует получение записей о всех фильмах по конкретному году выпуска.

        :param year: Год выпуска фильма.
        :return: Ответ базы данных на запрос.
        """
        return self.dao.get_all_by_year(year)

    def update(self, mid: int, data: dict) -> None:
        """
        Метод реализует обновление записи о фильме в базах данных.

        :param mid: id фильма в базе данных.
        :param data: Данные о фильме, которые нужно записать в базу данных.
        :return:
        """
        movie = self.get_one(mid)

        movie.id = data.get('id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, mid: int) -> None:
        """
        Метод реализует удаление записи о фильме в базе данных по id.

        :param mid: id фильма в базе данных.
        :return: None
        """
        movie = self.get_one(mid)

        self.dao.delete(movie)
