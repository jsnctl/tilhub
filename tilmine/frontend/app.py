import logging
from flask import Flask, render_template, request
from tilmine.frontend.forms import TILSearch
from tilmine.config import Config
import requests


logger = logging.getLogger(__name__)
app = Flask(__name__)

SERVER = Config.config['server']
PORTS = Config.config['ports']


@app.route("/", methods=['GET', 'POST'])
def home():

    search = TILSearch(request.form)
    tils = []
    if request.method == 'POST':
        tils = search_results(search)

    return render_template("tils.html", posts=tils, form=search)


def search_results(search):
    query = search.data['search']

    tils = requests.post("http://{0}:{1}/til/search/tags".format(SERVER, PORTS['api']),
                         json={"tags": "{0}".format(query)},
                         headers={'content-type': 'application/json'}).json()

    return tils



if __name__ == '__main__':
    app.run(debug=True, port=3000)