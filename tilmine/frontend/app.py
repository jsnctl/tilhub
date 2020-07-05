import logging
from flask import Flask
from tilmine.config import Config
from tilmine.frontend.routes import blueprint


logger = logging.getLogger(__name__)

SERVER = Config.config['server']
PORTS = Config.config['ports']


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, port=3000)