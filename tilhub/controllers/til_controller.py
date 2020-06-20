from db.models import TodayILearned
import logging
from extensions import db
from config import Config
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)
config = Config().config


class TILController:

    @staticmethod
    def get_til_by_id(til_id):
        result = TodayILearned.query.filter_by(id=til_id).first()
        return result

    @staticmethod
    def add_til(user, til):

        try:
            til = TodayILearned(user=user, til=til)
            db.session.add(til)
            db.session.commit()
            return til
        except SQLAlchemyError:
            logger.error('Problem creating TIL')
            return None
