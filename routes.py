from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models import db, User, Post
from forms import SignupForm, LoginForm, NewpostForm
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "s14a"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/lab_5'

db.init_app(app)

@app.route('/')
@app.route('/index')
def index():
	

@app.route('/login', methods=['GET', 'POST'])
def login():
	
    
@app.route('/logout', methods=['POST'])
def logout():
	
    
@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
	

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	

if __name__ == "__main__":
    app.run(debug=True)
