from db.models import User
from hashlib import md5
import logging
from extensions import db
from config import Config
from sqlalchemy.exc import SQLAlchemyError


logger = logging.getLogger(__name__)
config = Config().config


class AuthController:

    def add_user(self, user, password, email):

        salted_and_hashed_password = hash_salted_password(salt_password(password))

        try:
            user = User(username=user,
                        email=email,
                        password=salted_and_hashed_password)
            db.session.add(user)
            db.session.commit()
            return user

        except SQLAlchemyError:
            logger.error('Problem creating user')
            return None


def salt_password(password):
    return config['salt'] + password + config['salt']


def hash_salted_password(salted_password):
    return md5(salted_password.encode()).hexdigest()
