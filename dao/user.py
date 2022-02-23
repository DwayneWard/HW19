from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).filter(User.id == uid).one_or_none()

    def create(self, data):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def delete(self, user):
        self.session.delete(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
