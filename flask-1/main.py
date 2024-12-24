from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'its my very secret password that no one supposed to know'

class FormNamer(FlaskForm):
    name = StringField('YOUR REAL NAME!!', validators = [DataRequired()])
    submit = SubmitField('submit')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', UN = name)


@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404   


@app.route('/name', methods = ['GET', 'POST'])
def name():
    name = None
    form = FormNamer()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
    return render_template('name.html', name = name, form = form)

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')