from flask import jsonify
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token
from flask_restful import Resource, reqparse
from controllers.auth_controller import AuthController

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

        login_attempt = controller.attempt_login(args['username'], args['password'])

        if login_attempt:
            return jsonify(login_attempt)

        return jsonify("Wrong username or password")


class TokenRefreshEndpoint(Resource):

    @jwt_refresh_token_required
    def post(self):
        user = get_jwt_identity()
        access_token = create_access_token(identity=user)

        return jsonify({
            "access_token": access_token
        })




