from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

from .poke.poke_routes import poke
from .save_poke.save_routes import save_poke
from .auth.authroutes import auth
from .profiles.routes import profile

from .models import User

app = Flask(__name__)
login = LoginManager()
moment = Moment(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(poke)
app.register_blueprint(save_poke)
app.register_blueprint(auth)
app.register_blueprint(profile)

app.config.from_object(Config)


from .models import db

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)

login.login_view = 'auth.logMeIn'

from . import routes
from . import models
