from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# based off ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    team = db.relationship("Post", backref="trainer", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

class PokeTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke_name = db.Column(db.String(50), nullable=False)
    pokemon1 = db.Column(db.String(50), nullable=False)
    pokemon2 = db.Column(db.String(50), nullable=False)
    pokemon3 = db.Column(db.String(50), nullable=False)
    pokemon4 = db.Column(db.String(50), nullable=False)
    pokemon5 = db.Column(db.String(50), nullable=False)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, poke_name, user_id, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5):
        self.poke_name = poke_name
        self.user_id = user_id
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pokemon4 = pokemon4
        self.pokemon5 = pokemon5
