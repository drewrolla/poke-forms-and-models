from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import EditProfile
from app.models import User

from app.models import db

profile = Blueprint('profile', __name__, template_folder='profiletemplates')

@profile.route('/profile')
def userProfile():
    return render_template('profile.html')

@profile.route('/edit', methods=["GET", "POST"])
def edit():
    form = EditProfile()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # add user to database
            user = User(username, email, password)

            db.session.add(user)
            db.session.commit()

            flash("Changes saved.", 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash("Error making changes. Please try again.", 'error')
    return render_template('edit.html', form=form)