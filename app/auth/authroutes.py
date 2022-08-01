from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, UserCreationForm, EditProfileForm
from app.models import User, db

# import login functionality
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

# create the Blueprint
auth = Blueprint('auth', __name__, template_folder='authtemplates')

# routes 'n stuff
@auth.route('/login', methods=["GET", "POST"])
def logMeIn():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            # Query user based off of username
            user = User.query.filter_by(username=username).first()
            print(user.username, user.password, user.id)
            if user:
                # compare passwords
                if check_password_hash(user.password, password):
                    flash('ARE YOU READY TO CATCH THEM ALL???', 'success')
                    login_user(user)
                else:
                    flash('Incorrect username or password.', 'error')
            else:
                # user doesn't exist
                flash('Account does not exist. Please sign up!', 'error')

    return render_template('login.html', form=form)


@auth.route('/logout')
def logMeOut():
    flash('Hasta la vista!', 'success')
    logout_user()
    return redirect(url_for('auth.logMeIn'))


# @auth.route('/editprofile/<int:user_id>', methods=["GET", "POST"])
# @login_required
# def editProfile(user_id):
#     form = UserCreationForm()
#     user = User.query.get_or_404(user_id)
#     if request.method == "POST":
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         # db.update(User).values(user)
#         user.updateUserInfo(username, email, password)
#         user.saveUpdates()

#         flash("User Updated")
#         return redirect(url_for('index'))
#     else:
#         flash("Error occurred")
#         return render_template('editprofile.html', form=form, user=user)


@auth.route('/signup', methods=["GET", "POST"])
def signMeUp():
    form = UserCreationForm()
    if request.method == "POST":
        print("POST request made.")
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            print(username, email, password)

            # add user to database
            user = User(username, email, password)

            # add instance to db
            db.session.add(user)
            db.session.commit()

            flash('Account registered.', 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Validation failed. Please try again.', 'error')
    return render_template('signup.html', form=form)

@auth.route('/editprofile', methods=["GET", "POST"])
def editprofile():
    form = EditProfileForm()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # add user to database
            user = User(username, email, password)

            db.session.commit()

            flash("Changes saved.", 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash("Error making changes. Please try again.", 'error')
    return render_template('editprofile.html', form=form)


@auth.route('/editprofile/<int:id>', methods=["GET", "POST"])
@login_required
def editProfile(id):
    form = UserCreationForm()
    user = User.query.get_or_404(id)
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # db.update(User).values(to_update)
        user.updateUserInfo(username, email, password)
        user.saveUpdates()

        flash("User Updated", 'success')
        return redirect(url_for('index'))
    else:
        flash("Error occurred", 'danger')
        return render_template('editprofile.html', form=form, user=user)
