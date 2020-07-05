import requests
from flask import Blueprint, request, render_template, url_for, redirect

from tilmine.frontend.forms import TILSearch, Login
from tilmine.frontend.usecase.search import tag_search

blueprint = Blueprint("frontend", __name__)


@blueprint.route("/", methods=['GET', 'POST'])
def home():
    search = TILSearch(request.form)
    tils = []
    if request.method == 'POST':
        tils = tag_search(search)

    return render_template("tils.html", posts=tils, search_form=search)


@blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = Login(request.form)

    # TODO: request_handler from flask-login
    req = requests.post("http://localhost:5000/auth/login",
                      json={"username": form.username.data,
                          "password": form.password.data},
                      headers={'content-type': 'application/json'}).json()
    print(req)

    return render_template("login.html", form=form)


