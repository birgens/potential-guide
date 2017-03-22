from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_auth.views import mod_auth as auth_module
from app.mod_edit.views import mod_edit as edit_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(edit_module)


db.create_all()
