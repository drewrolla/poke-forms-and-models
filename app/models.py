from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# based off ERD
class Poke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke_name = db.Column(db.String(50), nullable=False)
    team = db.relationship("Post", backref="trainer", lazy=True)

    def __init__(self, poke_name):
        self.poke_name = poke_name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    team = db.relationship("Post", backref="trainer", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(300), nullable=False)
    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    poke_id = db.Column(db.Integer, db.ForeignKey('poke.id'))

    def __init__(self, user_id, poke_id):
        self.user_id = user_id
        self.poke_id = poke_id
