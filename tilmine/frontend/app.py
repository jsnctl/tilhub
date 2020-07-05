import logging
from flask import Flask, render_template, request
from tilmine.frontend.forms import TILSearch
import requests


logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home():

    search = TILSearch(request.form)
    tils = []
    if request.method == 'POST':
        tils = search_results(search)

    return render_template("home.html", posts=tils, form=search)


def search_results(search):
    query = search.data['search']

    tils = requests.post("http://localhost:5000/til/search/tags",
                         json={"tags": "{0}".format(query)},
                         headers={'content-type': 'application/json'}).json()

    return tils



if __name__ == '__main__':
    app.run(debug=True, port=3000)