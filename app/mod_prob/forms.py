from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import Required

class AnswerForm(FlaskForm):
    answer = FloatField(Required)


