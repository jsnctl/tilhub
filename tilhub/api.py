from flask import Flask
from flask_cors import CORS
from extensions import db, api
import yaml
from endpoints.til_endpoint import TILEndpoint

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)
DATABASE_URL = "postgres://{0}:{1}@localhost:5432/tilhub".format(
    CREDENTIALS['database']['username'],
    CREDENTIALS['database']['password']
)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    api.add_resource(TILEndpoint, '/til/<id>')

    api.init_app(app)
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)