from wtforms import Form, StringField


class TILSearch(Form):
    search = StringField('', render_kw={
        'style': 'font-size:30pt;'
    })
