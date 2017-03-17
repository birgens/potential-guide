from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(FlaskForm):
    username = TextField('Username', [Email(),Required(message='Forgot your username?')])
    password = PasswordField('Password', [Required(message='Forgot your password?')])

