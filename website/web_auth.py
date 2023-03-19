from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, login_manager, current_user
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from .web_models import User, Venue, Show, ShowTag, Tags


# -----------------------------Blueprint-----------------------------
web_auth = Blueprint('web_auth', __name__)



@web_auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("web_login.html")



@web_auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        # print(user_name, name)
        user = User.query.filter_by(user_name=user_name).first()
        # print(user)

        if user:
            flash("This user already exists. Log in", category='error')
            redirect(url_for('web_auth.login'))

        elif password != confirm_password:
            flash("Passwords don't match", category='error')
            # print("not matched")
        elif len(password) < 3:
            flash("Password is too short, should be greater than 7 characters", category='error')

        else:
            # new_user = User(user_name=user_name, name=name, password=generate_password_hash(password, method='sha256'))
            new_user = User(user_name=user_name, name=name, password=password)
            db.session.add(new_user)
            db.session.commit()

            flash('Account Created!', category='success')
            login_user(new_user, remember=True)

            return redirect(url_for('web_views.feed', user=current_user, user_name=new_user.user_name))

    return render_template('web_sign-up.html', user=current_user)

