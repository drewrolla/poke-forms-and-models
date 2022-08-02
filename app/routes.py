from flask_login import current_user
from app import app
from flask import render_template

from .models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokemon')
def pokemon():
    users = User.query.all()
    
    return render_template('pokemon.html', names=users) #names=users, following=following