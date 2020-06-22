from db.models import TodayILearned, Tag
import logging
from extensions import db
from config import Config
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)
config = Config().config


class TILController:

    def get_til_by_id(self, til_id):
        result = TodayILearned.query.filter_by(id=til_id).first()
        return result

    def get_tils_by_tag(self, tag):
        til_ids_with_tag = [tag.til_id for tag in Tag.query.filter_by(name=tag).all()]

        logger.debug(til_ids_with_tag)

        tils = []
        for til_id in til_ids_with_tag:
            tils.append(self.get_til_by_id(til_id))

        return tils

    def add_til(self, user, til, tag_names):

        try:
            til = TodayILearned(user=user, til=til)
            db.session.add(til)
            db.session.flush()

            for tag_name in tag_names:
                tag = Tag(name=tag_name, til_id=til.id)
                db.session.add(tag)

            db.session.commit()
            return til

        except SQLAlchemyError as error:
            logger.error(error)

            return None
