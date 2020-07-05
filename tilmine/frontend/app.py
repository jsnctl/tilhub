import logging
from flask import Flask, render_template, request
from tilmine.frontend.forms import TILSearch, Login
from tilmine.config import Config
import requests
from tilmine.frontend.usecase.search import tag_search
from tilmine.frontend.extensions import login_manager
from tilmine.frontend.routes import blueprint


logger = logging.getLogger(__name__)

SERVER = Config.config['server']
PORTS = Config.config['ports']


def create_app():
    app = Flask(__name__)
    # login_manager.init_app(app)
    app.register_blueprint(blueprint)

    return app



# @app.route("/", methods=['GET', 'POST'])
# def home():
#
#     login = Login(request.form)
#     search = TILSearch(request.form)
#     tils = []
#     if request.method == 'POST':
#         tils = tag_search(search)
#
#     return render_template("tils.html", posts=tils, form=search)
#
#
# def search_results(search):
#     query = search.data['search']
#
#     tils = requests.post("http://{0}:{1}/til/search/tags".format(SERVER, PORTS['api']),
#                          json={"tags": "{0}".format(query)},
#                          headers={'content-type': 'application/json'}).json()
#
#     return tils


if __name__ == '__main__':
    create_app().run(debug=True, port=3000)