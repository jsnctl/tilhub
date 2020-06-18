from db.models import TodayILearned


class TILController:

    def get_til_by_id(self, id):
        result = TodayILearned.query.filter_by(id=id).first()
        return result