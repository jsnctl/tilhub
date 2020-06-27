from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.auth_controller import AuthController
from werkzeug.security import safe_str_cmp

controller = AuthController()

parser = reqparse.RequestParser()
parser.add_argument("username")
parser.add_argument("password")
parser.add_argument("email")


class SignupEndpoint(Resource):

    def post(self):
        args = parser.parse_args()
        result = controller.add_user(username=args['username'],
                                     password=args['password'],
                                     email=args['email'])

        if result is None:
            return jsonify("Error creating user")

        return jsonify(result)


class LoginEndpoint(Resource):

    def post(self):
        args = parser.parse_args()

        if controller.attempt_login(args['username'], args['password']):
            return jsonify("Success!")

        return jsonify("Wrong username or password")


