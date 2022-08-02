from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


# hw stuff(?)
# class Followers(db.Model):
#     follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
#     followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
# if anything run this
# followers = db.Table('followers', 
#     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
# )
pokemon = db.Table('pokemon', 
    db.Column('pokemon_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('caughtPoke_id', db.Integer, db.ForeignKey('user.id'))
)

# will need to do flask db init/flask db migrate/flask db upgrade
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    team = db.relationship("PokeTeam", backref="trainer", lazy=True)
    caught = db.relationship("User",
        primaryjoin = (pokemon.c.caughtPoke_id==id),
        secondaryjoin = (pokemon.c.pokemon_id==id),
        secondary = pokemon,
        backref = db.backref('pokemon', lazy='dynamic'),
        lazy = 'dynamic'
    )

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

    def catch(self, user):
        self.caught.append(user)
        db.session.commit()

    def release(self, user):
        self.caught.remove(user)
        db.session.commit()

    def showSavedPokemon(self):
        saved = PokeTeam.query.join(pokemon, (PokeTeam.user_id==pokemon.c.caughtPoke_id)).filter(pokemon.c.caughtPoke_id==self.id))
        mine = PokeTeam.query.filter_by(user_id = self.id)
        all = saved.union(mine)

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


