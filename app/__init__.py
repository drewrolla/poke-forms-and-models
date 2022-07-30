from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

from .poke.poke_routes import poke
from .save_poke.save_routes import save_poke
# was wondering why I got an error when trying to load the login/signup, just forgot to add it here
from .auth.authroutes import auth

app = Flask(__name__)
app.register_blueprint(poke)
app.register_blueprint(save_poke)
app.register_blueprint(auth)

app.config.from_object(Config)


# initialize db to work with app
from .models import db

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models
