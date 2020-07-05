from flask import Blueprint, request, render_template

from tilmine.frontend.forms import Login, TILSearch
from tilmine.frontend.usecase.search import tag_search

blueprint = Blueprint("frontend", __name__)


@blueprint.route("/", methods=['GET', 'POST'])
def home():

    login = Login(request.form)
    search = TILSearch(request.form)
    tils = []
    if request.method == 'POST':
        tils = tag_search(search)

    return render_template("tils.html", posts=tils, form=search)
