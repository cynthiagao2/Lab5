from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models import db, User, Post
from forms import SignupForm, LoginForm, NewpostForm
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "s14a"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/lab_5'

db.init_app(app)

@app.route('/')
@app.route('/index')
def index():
	if 'username' in session:
		session_user = User.query.filter_by(username=session['username']).first()
		return render_template('index.html', title='Home', session_username=session_user.username)
	else:
		return render_template('index.html', title='Home')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		existing_user = User.query.filter_by(username=username).first()
		
		if existing_user:
			flash('The username already exists. Please pick another one.')
			return redirect(url_for('signup'))
		
		else:
			user = User(username=username, password=sha256_crypt.hash(password))
			db.session.add(user)
			db.session.commit()
			flash('Congratulations, you are now a registered user!')
			return redirect(url_for('login'))
	else:
		return render_template('signup.html', title='Signup', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		user = User.query.filter_by(username=username).first()

			if user is None or not sha256_crypt.verify(password, user.password):
				flash('Invalid username or password')
				return redirect(url_for('login'))

			else: 
				session['username'] = username
				return redirect(url_for('index'))
	else: 
		return render_template('login.html', title='Login', form=form)
    
@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return redirect(url_for('index'))
	
    
@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
	

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	

if __name__ == "__main__":
    app.run(debug=True)
