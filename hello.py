from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_mail import Mail

app = Flask(__name__, template_folder='app/templates/')
#secret_key should be changed
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
mail = Mail(app)

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/',methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		#form.name.data = '?'
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

# ERROR HANDLE
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
#
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500


if __name__ == '__main__':
	app.run(debug = True)