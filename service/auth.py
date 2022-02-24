import datetime
import calendar
from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService
import jwt


class AuthService:
    def __init__(self, user_service: UserService):
        """
        Инициализация сервисов для работы.
        :param user_service: сервисы, организующие работу с таблицей пользователей
        """
        self.user_service = user_service

    def generate_token(self, username: str, password: str, is_refresh=False):
        """
        Метод производит генерацию токенов на основе учетных данных пользователя или refresh токена
        :param username: Имя пользователя
        :param password: Пароль
        :param is_refresh: Параметр, который указывает необходимо ли использовать refresh токен
        :return: Exception или словарь, состоящий из access и refresh токенов
        """
        user = self.user_service.get_by_username(username)

        if user is None:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                raise Exception()

        data = {
            'username': user.username,
            'role': user.role
        }

        exp_access_token = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(exp_access_token.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        exp_refresh_token = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(exp_refresh_token.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        tokens = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

        return tokens

    def approve_refresh_token(self, refresh_token: str):
        """
        Метод генерирует запрос на формирование пары access
        :param refresh_token: refresh токен, который будет использоваться для генерации новых токенов
        :return: Exception или словарь, состоящий из access и refresh токенов
        """
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get('username')

        user = self.user_service.get_by_username(username)

        if user is None:
            raise Exception()

        return self.generate_token(username, user.password, is_refresh=True)
