from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import current_user, login_required
from app.auth.forms import EditProfileForm
from werkzeug.security import generate_password_hash

from app.models import User, db

profile = Blueprint('profile', __name__, template_folder='templates_profile')

@profile.route('/profile', methods=["GET", "POST"])
@login_required
def editProfile():
    form = EditProfileForm()
    user = User.query.filter_by(id = current_user.id).first()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            if username != " ":
                user.username = username
            if email != " ":
                user.email = email
            if password != " ":
                user.password = generate_password_hash(password)

            user.updateProfile()
            
            # db.session.add(user) not needed becuase we are only updating 
            # db.session.commit() Calling this using user.updateProfile()
            flash('Profile updated!', 'warning')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Validation failed.', 'danger')
    return render_template('profile.html', form=form, user=user)