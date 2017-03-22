from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField

class ProblemForm(FlaskForm):
    ID = IntegerField('ID')
    name = TextField('Name')
    content = TextField('Content')
    variables = TextField('Variables')
    answer = TextField('Answer')
