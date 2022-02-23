import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
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

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

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

    def make_user_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, other_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            ))
