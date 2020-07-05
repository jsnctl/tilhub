from wtforms import Form, StringField


class TILSearch(Form):
    search = StringField('')
