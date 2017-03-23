from flask_wtf import FlaskForm
from wtforms import FloatField, TextField
from wtforms.validators import Required

class ProblemForm(FlaskForm):
    name = TextField('Name')
    content = TextField('Content')
    variables = TextField('Variables')
    answer = TextField('Answer')
    
    

class AnswerForm(FlaskForm):
    answer = FloatField(Required)


