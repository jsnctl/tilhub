from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.auth_controller import AuthController

controller = AuthController()

parser = reqparse.RequestParser()
parser.add_argument("username")
parser.add_argument("password")
parser.add_argument("email")


class AuthEndpoint(Resource):

    def post(self):
        args = parser.parse_args()
        result = controller.add_user(user=args['username'],
                                     password=args['password'],
                                     email=args['email'])

        if result is None:
            return jsonify("Error creating user")

        return jsonify(result)
