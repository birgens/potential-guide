from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db

from app.mod_edit.forms import ProblemForm

#from app.mod_prob.models import Problem

mod_edit = Blueprint('edit', __name__, url_prefix='/edit',
                     template_folder='templates', static_folder='static')

# Some simple functions
#def problem_readform()

# Routes
@mod_edit.route('/index')
def index():
    return render_template("edit/index.html")

@mod_edit.route('/problem/<int:ID>', methods=['GET','POST'])
def problem(ID):
    form = ProblemForm(request.form)

    if form.validate_on_submit():
        if form.ID.data == 0:
            problem = Problem(name,content,variables,answer)
            db.add(problem)
            db.commit()
            return redirect(url_for('.index'))
        else:
            problem = Problem.query.get(form.ID.data)
            problem.name = form.name.data
            problem.content = form.content.data
            problem.variables = form.variables.data
            problem.answer = form.answer.data
            return redirect(url_for('.index'))
    else:
        return render_template("edit/problem.html", form=form)
    
