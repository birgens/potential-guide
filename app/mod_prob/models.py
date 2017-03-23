from app import db
from random import randint, uniform, seed
from jinja2 import Template

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Problem(Base):
    __tablename__ = 'prob_problem'
    
    name = db.Column(db.Text)
    content = db.Column(db.Text)
    variables = db.Column(db.Text)
    answer = db.Column(db.Text)

    
    def __init__(self, name, content, variables, answer):
        self.name = name
        self.variables = variables
        self.content = content
        self.answer = answer

    def render_content(self,seeding):
        seed(seeding)
        var = eval(self.variables)
        contentTemplate = Template(self.content)
        return contentTemplate.render(var)

    def right_answer(self, seeding, ans):
        seed(seeding)
        var = eval(self.variables)
        locals().update(var)
        correctAnswer = eval(self.answer)

        if correctAnswer == 0 and abs(ans) < 0.01:
            return True
        elif abs((ans-correctAnswer)/correctAnswer) < 0.01:
            return True
        else:
            return False
