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

    def create(self, data: dict) -> None:
        """
        Метод реализует запись новых данных в базу данных.
        :param data: Данные, которые необходимо записать в базу данных.
        """
        new_director = Director(**data)

        self.session.add(new_director)
        self.session.commit()

    def update(self, director: list[Director]) -> None:
        """
        Метод реализует обновление записи о фильме в базах данных.
        :param director: Данные о фильме, которые нужно записать в базу данных.
        """
        self.session.add(director)
        self.session.commit()

    def delete(self, director: list[Director]) -> None:
        """
        Метод реализует удаление записи о фильме в базе данных по id.
        :param director: Данные о фильме, которые необходимо удалить из базы данных.
        :return: None
        """
        self.session.delete(director)
        self.session.commit()
