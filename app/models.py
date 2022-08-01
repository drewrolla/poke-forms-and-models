from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    team = db.relationship("PokeTeam", backref="trainer", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def updateUserInfo(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveUpdates(self):
        db.session.commit()

class PokeTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon1 = db.Column(db.String(50))
    pokemon2 = db.Column(db.String(50))
    pokemon3 = db.Column(db.String(50))
    pokemon4 = db.Column(db.String(50))
    pokemon5 = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, user_id):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pokemon4 = pokemon4
        self.pokemon5 = pokemon5
        self.user_id = user_id
