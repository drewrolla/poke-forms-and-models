from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')