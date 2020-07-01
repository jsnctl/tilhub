from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.til_controller import TILController
from flask_jwt_extended import jwt_required

controller = TILController()

parser = reqparse.RequestParser()
parser.add_argument("user")
parser.add_argument("til")
parser.add_argument("tags", action='append')


class TILGetEndpoint(Resource):

    def get(self, til_id):
        til = controller.get_til_by_id(til_id)
        return jsonify(til)


class TILSearchByTagEndpoint(Resource):


    def post(self):
        args = parser.parse_args()
        tags = args['tags']
        tils = controller.get_tils_by_tags(tags)

        return jsonify(tils)


class TILSearchByUserEndpoint(Resource):

    @jwt_required
    def post(self):
        args = parser.parse_args()
        tags = args['user']
        tils = controller.get_tils_by_user(tags)

        return jsonify(tils)


class TILPostEndpoint(Resource):

    @jwt_required
    def post(self):
        args = parser.parse_args()
        result = controller.add_til(user=args['user'],
                                    til=args['til'],
                                    tag_names=args['tags'])

        if result is None:
            return jsonify("Error creating TIL")

        return jsonify(result)

