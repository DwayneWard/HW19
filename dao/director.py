from dao.model.director import Director


class DirectorDAO:
    """
    Класс описывает Data Access Object (DAO) для работы с базой данный, с таблицей фильмов.
    """

    def __init__(self, session):
        """
        Метод инициализирует поле класса session, как сессию работы с базой данных.
        :param session: Сессия базы данных
        """
        self.session = session

    def get_one(self, did: int) -> list[Director]:
        """
        Метод реализует получение записи об одном фильме из базы данных по id.
        :param did: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о фильме по id.
        """
        return self.session.query(Director).get(did)

    def get_all(self) -> list[Director]:
        """
        Метод реализует получение записей о всех фильмах из базы данных.
        :return: Ответ базы данных на запрос получения данных о всех фильмах.
        """
        return self.session.query(Director).all()
