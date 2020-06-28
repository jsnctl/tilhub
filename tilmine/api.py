from flask import Flask
from flask_cors import CORS
from extensions import db, api, jwt
from endpoints.til_endpoint import (TILGetEndpoint,
                                    TILPostEndpoint,
                                    TILSearchByTagEndpoint,
                                    TILSearchByUserEndpoint)
from endpoints.auth_endpoint import (SignupEndpoint,
                                     LoginEndpoint)
from config import Config

config = Config().config
DATABASE_URL = "postgres://{0}:{1}@localhost:5432/tilmine".format(
    config['database']['username'],
    config['database']['password']
)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    api.add_resource(SignupEndpoint, '/auth/signup')
    api.add_resource(LoginEndpoint, '/auth/login')

    api.add_resource(TILGetEndpoint, '/til/<til_id>')
    api.add_resource(TILSearchByTagEndpoint, '/til/search/tags')
    api.add_resource(TILSearchByUserEndpoint, '/til/search/user')
    api.add_resource(TILPostEndpoint, '/til')

    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    app.secret_key = config['jwt_secret']

    return app


if __name__ == '__main__':
    create_app().run(debug=True)