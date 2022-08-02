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
    caught = []
    caught_set = set()
    if current_user.is_authenticated:
        caught = current_user.caughtPoke.all()
        caught_set = {c.id for c in caught}
    for u in users:
        if u.id in caught_set:
            u.flag=True

    
    
    return render_template('pokemon.html', names=users)