from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Poke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke_name = db.Column(db.String(100), nullable=False)

    def __init__(self, poke_name):
        self.poke_name = poke_name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

# maybe I should combine these two classes into one, we want the users to have a max of 5 pokemon