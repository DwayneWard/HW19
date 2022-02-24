from dao.model.movie import Movie


class MovieDAO:
    """
    Класс описывает Data Access Object (DAO) для работы с базой данный, с таблицей фильмов.
    """

    def __init__(self, session):
        """
        Метод инициализирует поле класса session, как сессию работы с базой данных.
        :param session: Сессия базы данных
        """
        self.session = session

    def create(self, data: dict) -> None:
        """
        Метод реализует запись новых данных в базу данных.
        :param data: Данные, которые необходимо записать в базу данных.
        """
        new_movie = Movie(**data)

        self.session.add(new_movie)
        self.session.commit()

    def get_one(self, mid: int) -> list[Movie]:
        """
        Метод реализует получение записи об одном фильме из базы данных по id.
        :param mid: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о фильме по id.
        """
        return self.session.query(Movie).filter(Movie.id == mid).one_or_none()

    def get_all(self) -> list[Movie]:
        """
        Метод реализует получение записей о всех фильмах из базы данных.
        :return: Ответ базы данных на запрос получения данных о всех фильмах.
        """
        return self.session.query(Movie).all()

    def get_all_on_director(self, director_id: int) -> list[Movie]:
        """
        Метод реализует получение записей о всех фильмах по конкретному режиссеру.
        :param director_id: id режиссера в базе данных.
        :return: Ответ базы данных на запрос к базе данных.
        """
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_all_on_genre(self, genre_id: int) -> list[Movie]:
        """
        Метод реализует получение записей о всех фильмах по конкретному жанру.
        :param genre_id: id жанра к базе данных.
        :return: Ответ базы данных на запрос.
        """
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_all_by_year(self, year: int) -> list[Movie]:
        """
        Метод реализует получение записей о всех фильмах по конкретному году выпуска.
        :param year: Год выпуска фильма.
        :return: Ответ базы данных на запрос.
        """
        return self.session.query(Movie).filter(Movie.year == year)

    def update(self, movie: list[Movie]) -> None:
        """
        Метод реализует обновление записи о фильме в базах данных.
        :param movie: Данные о фильме, которые нужно записать в базу данных.
        """
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie: list[Movie]) -> None:
        """
        Метод реализует удаление записи о фильме в базе данных по id.
        :param movie: Данные о фильме, которые необходимо удалить из базы данных.
        :return: None
        """
        self.session.delete(movie)
        self.session.commit()
