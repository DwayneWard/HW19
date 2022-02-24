from dao.director import DirectorDAO


class DirectorService:
    """
    Класс описывает сервисы для работы в приложении Flask с таблицей режиссеров.
    """
    def __init__(self, dao: DirectorDAO):
        """
        Метод инициализирует DAO
        :param dao: DAO объект
        """
        self.dao = dao

    def get_one(self, did: int) -> None or list:
        """
        Метод реализует получение записи об одном фильме из базы данных по id.
        :param did: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о фильме по id.
        При отсутствии id в базе данных возвращает None.
        """
        director = self.dao.get_one(did)
        if not director:
            return None
        return director

    def get_all(self) -> list:
        """
        Метод реализует получение записей о всех фильмах из базы данных.
        :return: Ответ базы данных на запрос получения данных о всех фильмах.
        """
        return self.dao.get_all()

    def create(self, data: dict) -> None:
        """
        Метод реализует запись новых данных в базу данных.
        :param data: Данные, которые необходимо записать в базу данных.
        :return: None
        """
        return self.dao.create(data)

    def update(self, did: int, data: dict) -> None:
        """
        Метод реализует обновление записи о фильме в базах данных.
        :param did: id фильма в базе данных.
        :param data: Данные о фильме, которые нужно записать в базу данных.
        :return:
        """
        director = self.get_one(did)

        director.id = data.get('id')
        director.name = data.get('name')

        self.dao.update(director)

    def delete(self, did: int) -> None:
        """
        Метод реализует удаление записи о фильме в базе данных по id.
        :param did: id фильма в базе данных.
        :return: None
        """
        director = self.get_one(did)

        self.dao.delete(director)

