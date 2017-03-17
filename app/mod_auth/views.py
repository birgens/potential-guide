from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from werkzeug import check_password_hash, generate_password_hash

from app import db

from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth', 
                     template_folder='templates', static_folder='static')
login_manager = LoginManager()

@mod_auth.record_once
def on_load(state):
    login_manager.init_app(state.app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Routes
@mod_auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Welcome %s' % user.name)

            return redirect(url_for('index'))
        else:
            flash('Wrong email or password', 'error-message')

    return render_template("auth/login.html", form=form)

