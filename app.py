from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.user import User
from implemented import user_service
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.user import user_ns


def create_app(config_object: Config) -> Flask:
    """
    Функция производит создание Flask приложения с необходимой конфигурацией
    :param config_object: Конфигурация Flask приложения
    :return: Flask приложение
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask) -> None:
    """
    Функция производит инициализацию базы данных и создание API.
    :param app: Сконфигурированное Flask-приложение.
    :return: None
    """
    db.init_app(app)
    api = Api(app)
    # create_data(app, db)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_data(app: Flask, db) -> None:
    """
    Функция производит запись данных в базу данных и создание таблицы user
    :param app: Сконфигурированное Flask-приложение
    :param db: База данных SQLAlchemy
    :return: None
    """
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password=user_service.make_user_password_hash('my_little_pony'), role="user")
        u2 = User(username="oleg", password=user_service.make_user_password_hash('qwerty'), role="user")
        u3 = User(username="oleg", password=user_service.make_user_password_hash('P@ssw0rd'), role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
