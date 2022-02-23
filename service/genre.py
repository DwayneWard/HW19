from dao.genre import GenreDAO


class GenreService:
    """
    Класс описывает сервисы для работы в приложении Flask с таблицей жанров.
    """
    def __init__(self, dao: GenreDAO):
        """
        Метод инициализирует DAO
        :param dao: DAO объект
        """
        self.dao = dao

    def get_one(self, gid: int) -> None or list:
        """
        Метод реализует получение записи об одном фильме из базы данных по id.
        :param gid: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о фильме по id.
        При отсутствии id в базе данных возвращает None.
        """
        genre = self.dao.get_one(gid)
        if not genre:
            return None
        return genre

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

    def update(self, gid: int, data: dict) -> None:
        """
        Метод реализует обновление записи о фильме в базах данных.
        :param gid: id фильма в базе данных.
        :param data: Данные о фильме, которые нужно записать в базу данных.
        :return:
        """
        genre = self.get_one(gid)

        genre.id = data.get('id')
        genre.name = data.get('name')

        self.dao.update(genre)

    def delete(self, gid: int) -> None:
        """
        Метод реализует удаление записи о фильме в базе данных по id.
        :param gid: id фильма в базе данных.
        :return: None
        """
        genre = self.get_one(gid)

        self.dao.delete(genre)
