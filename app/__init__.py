from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

from .poke.poke_routes import poke
from .save_poke.save_routes import save_poke
# was wondering why I got an error when trying to load the login/signup, just forgot to add it here
from .auth.authroutes import auth
from .models import User
from .profile.profileroutes import profile

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(poke)
app.register_blueprint(save_poke)
app.register_blueprint(auth)
app.register_blueprint(profile)

app.config.from_object(Config)


# initialize db to work with app
from .models import db

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)

# user must log in view this page
login.login_view = 'auth.logMeIn'

from . import routes
from . import models
