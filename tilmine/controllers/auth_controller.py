from db.models import User
from hashlib import md5
import logging
from extensions import db
from config import Config
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import safe_str_cmp


logger = logging.getLogger(__name__)
config = Config().config


class AuthController:

    def add_user(self, username, password, email):

        hashed_password = hash_password(password)

        try:
            user = User(username=username,
                        email=email,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return user

        except SQLAlchemyError:
            logger.error('Problem creating user')
            return None

    def get_user_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        return user

    def attempt_login(self, username, password):
        user = self.get_user_by_username(username)

        if safe_str_cmp(hash_password(password), user.password):
            return user


def _salt_password(password):
    return config['salt'] + password + config['salt']


def hash_password(password):
    salted_password = _salt_password(password)
    return md5(salted_password.encode()).hexdigest()
