from flask import Flask, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Shhhhhh... 🤫'

class NameForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[Length(min=6), DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return 'Form submitted successfully'

    