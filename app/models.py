from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Poke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke_name = db.Column(db.String(100), nullable=False)

    def __init__(self, poke_name):
        self.poke_name = poke_name