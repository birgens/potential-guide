from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_required

from app.mod_prob.forms import AnswerForm, ProblemForm
from app.mod_prob.models import Problem

from app import db

mod_prob = Blueprint('prob', __name__, url_prefix='/prob', template_folder='templates', static_folder='static')

@mod_prob.route('/index')
def index():
    problems = Problem.query.all()
    return render_template("prob/index.html", problems=problems)

@mod_prob.route('/<int:ID>', methods=['POST','GET'])
def problem(ID):
    prob = Problem.query.get(ID)
    form = AnswerForm(request.form)

    if form.validate_on_submit():
        if prob.right_answer(10, form.answer.data):
            return redirect(url_for('.rightanswer'))
        else:
            return redirect(url_for('.wronganswer'))
    else:
        return render_template('prob/problem.html', content=prob.render_content(10), form=form)

@mod_prob.route('/rightanswer')
def rightanswer():
    return "Right answer"

@mod_prob.route('/wronganswer')
def wronganswer():
    return "Wrong answer"


        
@mod_prob.route('/add', methods=['GET','POST'])
@login_required
def add():
    form = ProblemForm(request.form)

    if form.validate_on_submit():
        prob = Problem(form.name.data, form.content.data, form.variables.data, form.answer.data)
        db.session.add(prob)
        db.session.commit()
        flash('Problem created successfully')
        return redirect(url_for('.index'))
    return render_template('prob/add.html', form=form)
