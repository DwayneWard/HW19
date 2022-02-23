from dao.user import UserDAO


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        user = self.dao.get_one(uid)
        if not user:
            return None
        return user

    def create(self, data):
        return self.dao.create(data)

    def delete(self, uid):
        user = self.get_one(uid)
        self.dao.delete(user)

    def update(self, data):
        user = self.get_one(data.get("id"))
        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")

        self.dao.update(user)
