from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.til_controller import TILController

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

        tils = []
        for tag in tags:
            tils.append(controller.get_tils_by_tag(tag))
        return jsonify(tils)


class TILPostEndpoint(Resource):

    def post(self):
        args = parser.parse_args()
        result = controller.add_til(user=args['user'],
                                    til=args['til'],
                                    tag_names=args['tags'])

        if result is None:
            return jsonify("Error creating TIL")

        return jsonify(result)

