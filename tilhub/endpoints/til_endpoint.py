from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.til_controller import TILController

controller = TILController()

parser = reqparse.RequestParser()
parser.add_argument("user")
parser.add_argument("til")


class TILGetEndpoint(Resource):

    @staticmethod
    def get(til_id):
        til = controller.get_til_by_id(til_id)
        return jsonify(til)


class TILPostEndpoint(Resource):

    @staticmethod
    def post():
        args = parser.parse_args()
        result = controller.add_til(user=args['user'],
                                    til=args['til'])

        if result is None:
            return jsonify("Error creating TIL")

        return jsonify(result)

