from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, UserCreationForm, EditProfileForm
from app.models import User, db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='authtemplates')


@auth.route('/login', methods=["GET", "POST"])
def logMeIn():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            print(user.username, user.password, user.id)
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('pokemon'))
                else:
                    flash('Incorrect username or password.', 'error')
            else:
                flash('Account does not exist. Please sign up!', 'error')
    return render_template('login.html', form=form)

@auth.route('/logout')
def logMeOut():
    flash("You've yee'd your last haw.", 'success')
    logout_user()
    return redirect(url_for('auth.logMeIn'))


@auth.route('/signup', methods=["GET", "POST"])
def signMeUp():
    form = UserCreationForm()
    if request.method == "POST":
        print("POST request made.")
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)

            db.session.add(user)
            db.session.commit()

            flash('Account registered.', 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Validation failed. Please try again.', 'error')
    return render_template('signup.html', form=form)
