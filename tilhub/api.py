from flask import Flask
from flask_cors import CORS
from extensions import db, api
from endpoints.til_endpoint import (TILGetEndpoint, TILPostEndpoint)
from endpoints.auth_endpoint import AuthEndpoint
from config import Config

config = Config().config
DATABASE_URL = "postgres://{0}:{1}@localhost:5432/tilhub".format(
    config['database']['username'],
    config['database']['password']
)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    api.add_resource(AuthEndpoint, '/auth')
    api.add_resource(TILGetEndpoint, '/til/<til_id>')
    api.add_resource(TILPostEndpoint, '/til')

    api.init_app(app)
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)