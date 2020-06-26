from db.models import TodayILearned, Tag
import logging
from extensions import db
from config import Config
from sqlalchemy.exc import SQLAlchemyError
from itertools import chain

logger = logging.getLogger(__name__)
config = Config().config


class TILController:

    def get_til_by_id(self, til_id):
        result = TodayILearned.query.filter_by(id=til_id).first()
        return result

    def _get_tils_by_tag(self, tag: str):
        til_ids_with_tag = [tag.til_id for tag in Tag.query.filter_by(name=tag).all()]

        logger.debug(til_ids_with_tag)

        tils = []
        for til_id in til_ids_with_tag:
            tils.append(self.get_til_by_id(til_id))

        return tils

    def get_tils_by_tags(self, tags: list):

        tils = []
        for tag in tags:
            tils.append(self._get_tils_by_tag(tag))

        return list(chain(*tils))

    def get_tils_by_user(self, user: str):
        result = TodayILearned.query.filter_by(user=user).all()
        return result

    def add_til(self, user, til, tag_names):

        try:
            til = TodayILearned(user=user, til=til, display_tags=tag_names)
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
