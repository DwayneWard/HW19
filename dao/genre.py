from dao.model.genre import Genre


class GenreDAO:
    """
    Класс описывает Data Access Object (DAO) для работы с базой данный, с таблицей фильмов.
    """

    def __init__(self, session):
        """
        Метод инициализирует поле класса session, как сессию работы с базой данных.
        :param session: Сессия базы данных
        """
        self.session = session

    def get_one(self, gid: int) -> list[Genre]:
        """
        Метод реализует получение записи об одном фильме из базы данных по id.
        :param gid: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о фильме по id.
        """
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """
        Метод реализует получение записей о всех фильмах из базы данных.
        :return: Ответ базы данных на запрос получения данных о всех фильмах.
        """
        return self.session.query(Genre).all()