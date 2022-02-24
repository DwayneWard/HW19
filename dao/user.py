from dao.model.user import User


class UserDAO:
    """
    Класс описывает Data Access Object (DAO) для работы с базой данный, с таблицей фильмов.
    """

    def __init__(self, session):
        """
        Метод инициализирует поле класса session, как сессию работы с базой данных.
        :param session: Сессия базы данных
        """
        self.session = session

    def get_all(self) -> list[User]:
        """
        Метод реализует получение записей о всех пользователях из базы данных.
        :return: Ответ базы данных на запрос получения данных о всех пользователях.
        """
        return self.session.query(User).all()

    def get_one(self, uid: int) -> list[User]:
        """
        Метод реализует получение записи об одном пользователе из базы данных по id.
        :param uid: id фильма в базе данных.
        :return: Ответ базы данных на запрос о получении записи о пользователе по id.
        """
        return self.session.query(User).filter(User.id == uid).one_or_none()

    def get_by_username(self, username: str):
        """
        Метод реализует получение записи об одном пользователе из базы данных по username.
        :param username: Имя пользователя.
        :return: Ответ базы данных на запрос о получении записи о пользователе по username
        """
        return self.session.query(User).filter(User.username == username).first()

    def create(self, data: dict) -> list[User]:
        """
        Метод реализует запись новых данных в базу данных.
        :param data: Данные, которые необходимо записать в базу данных.
        """
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def delete(self, user: list[User]) -> None:
        """
        Метод реализует обновление записи о пользователе в базе данных.
        :param user: Данные о пользователе, которые нужно записать в базу данных.
        """
        self.session.delete(user)
        self.session.commit()

    def update(self, user: list[User]) -> None:
        """
        Метод реализует обновление записи о пользователе в базах данных.
        :param user: Данные о пользователе, которые нужно записать в базу данных.
        :return: None
        """
        self.session.add(user)
        self.session.commit()
