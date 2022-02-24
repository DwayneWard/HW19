import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    """
    Класс описывает сервисы для работы в приложении Flask с таблицей фильмов.
    """

    def __init__(self, dao: UserDAO):
        """
        Метод инициализирует DAO

        :param dao: DAO объект
        """
        self.dao = dao

    def get_all(self) -> list:
        """
        Метод реализует получение записей о всех пользователях из базы данных.

        :return: Ответ базы данных на запрос получения данных о всех пользователях.
        """
        return self.dao.get_all()

    def get_one(self, uid: int) -> None or list:
        """
        Метод реализует получение записи об одном пользователе из базы данных по id.

        :param uid: id пользователя в базе данных.
        :return: Ответ базы данных на запрос о получении записи о пользователе по id.
        При отсутствии id в базе данных возвращает None.
        """
        user = self.dao.get_one(uid)
        if not user:
            return None
        return user

    def get_by_username(self, username: str):
        """
        Метод реализует получение записи об одном пользователе из базы данных по username.

        :param username: Имя пользователя.
        :return: Ответ базы данных на запрос о получении записи о пользователе по username
        """
        return self.dao.get_by_username(username)

    def create(self, data: dict) -> list:
        """
        Метод реализует запись новых данных в базу данных.

        :param data: Данные, которые необходимо записать в базу данных.
        """
        return self.dao.create(data)

    def delete(self, uid: int) -> None:
        """
        Метод реализует удаление записи о пользователе в базе данных.

        :param uid: id пользователя в базе данных.
        """
        user = self.get_one(uid)
        self.dao.delete(user)

    def update(self, data: dict) -> None:
        """
        Метод реализует обновление записи о пользователе в базе данных.

        :param data:
        :return:
        """
        user = self.get_one(data.get("id"))
        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")

        self.dao.update(user)

    def make_user_password_hash(self, password: str):
        """
        Метод производит генерацию хеша из передаваемого пароля. Кодируется методом SHA256,
        с использованием SALT и количеством иттераций 100000.

        :param password: Пароль в виде строки.
        :return: Сгенерированный хэш-пароль
        """
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, other_password: str) -> bool:
        """
        Функция производит сравнивание двух паролей, переводит пароль, введенный пользователем в хэш
        и сравнивает с имеющимся.

        :param password_hash: Хеш-пароль.
        :param other_password: Пароль в открытом виде.
        :return: True или False
        """
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            ))
