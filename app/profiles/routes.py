from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import current_user
from app.auth.forms import EditProfileForm

profile = Blueprint('profile', __name__, template_folder='profiletemplates')

from app.models import User, db

@profile.route('/profile', methods=["GET", "POST"]) 
def editProfile():
    form = EditProfileForm()
    user = User.query.filter_by(id = current_user.id).first()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # as long as the input isn't empty/blank, the username will update to whatever is put in
            # fingers crossed this will work
            if username != "":
                user.username = username
            if email != "":
                user.email = email
            if password != "":
                user.password = password

            db.session.add(user)
            db.session.commit()
            flash('Profile updated!', 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Validation failed.', 'danger')
    return render_template('profile.html', form=form)