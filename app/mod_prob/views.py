from flask import Blueprint, redirect, url_for, render_template

from app.mod_prob.forms import AnswerForm

mod_prob = Blueprint('prob', __name__, url_prefix='/prob', template_folder='templates', static_folder='static')

@mod_prob.route('/<int:ID>', methods=['POST','GET'])
def problem(ID):
    prob = Problem.query.get(ID)
    form = AnswerForm(request.form)

    if form.validate_om_submit():
        if prob.right_answer(10, form.answer.data):
            return redirect(url_for('.rightanswer'))
        else:
            return redirect(url_for('.wronganswer'))
    else:
        return render_template('prob/problem.html', content=prob.render_content(10), form=form)
        
