from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserCreationForm
from .forms import UserLoginForm
from app.models import User

# create the Blueprint
auth = Blueprint('auth', __name__, template_folder='authtemplates')

from app.models import db

# routes 'n stuff
@auth.route('/login')
def logMeIn():
    form = UserLoginForm()
    if form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        return redirect(url_for('/'))
    else:
        print('Validation failed.')
    return render_template('home.html', form=form)

@auth.route('/signup')
def signMeUp():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            account = User(username, email, password)
            
            db.session.add(account)
            db.session.commit()

            return redirect(url_for('auth.logMeIn'))
        else:
            print('Validation failed.')
    return render_template('signup.html', form=form)
