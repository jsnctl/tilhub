from wtforms import Form, StringField, PasswordField, SubmitField


class TILSearch(Form):
    search = StringField('', render_kw={
        'style': 'font-size:30pt;'
    })


class Login(Form):
    username = StringField('')
    password = PasswordField('')
    submit = SubmitField()