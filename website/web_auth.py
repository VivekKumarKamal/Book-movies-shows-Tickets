from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, login_manager, current_user
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from .web_models import User, Venue, Show, Tags
from .web_forms import ShowForm
from datetime import datetime
from datetime import datetime


# -----------------------------Blueprint-----------------------------
web_auth = Blueprint('web_auth', __name__)


@web_auth.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        user = User.query.filter_by(user_name=user_name, admin=1).first()
        if not user:
            flash("No User found with this User-Name", category='error')
        else:
            if user.password == password:
                login_user(user)

                return render_template('admin_files/web_admin-dashboard.html', user=user)
    return render_template("admin_files/web_admin-login.html")


@web_auth.route('/user-login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        user = User.query.filter_by(user_name=user_name, admin=0).first()
        if not user:
            flash("No User found with this User-Name", category='error')
        else:
            if user.password == password:
                login_user(user)

                return render_template('user_files/web_user-dashboard.html', user=user)
    return render_template("user_files/web_user-login.html")


@web_auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        # print(user_name, name)
        user = User.query.filter_by(user_name=user_name, admin=0).first()
        # print(user)

        if user:
            flash("This user already exists. Log in", category='error')
            redirect(url_for('web_auth.user_login'))

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

            return redirect(url_for('web_views.home', user=current_user, admin=False))

    return render_template('web_sign-up.html')


@web_auth.route('/log-out')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web_views.home'))


@web_auth.route('/manage-venue/<int:venue_id>', methods=['GET', 'POST'])
@login_required
def manage_venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    if request.method == "GET":
        name = venue.name if venue else ""
        place = venue.place if venue else ""
        location = venue.location if venue else ""
        capacity = venue.capacity if venue else ""

        return render_template("admin_files/web_venue-management.html",
                               user=current_user,
                               venue_name=name,
                               place=place,
                               location=location,
                               capacity=capacity)
    else:
        venue_name = request.form.get('venue_name')
        place = request.form.get('place')
        location = request.form.get('location')
        capacity = request.form.get('capacity')

        if not venue:
            new_venue = Venue(id=venue_id,
                              admin_id=current_user.id,
                              name=venue_name,
                              place=place,
                              location=location,
                              capacity=capacity)
            db.session.add(new_venue)
            db.session.commit()

        else:
            venue.name = venue_name
            venue.place = place
            venue.location = location
            venue.capacity = capacity

            db.session.commit()

    return redirect(url_for('web_views.home'))


@web_auth.route('/manage-show/<int:venue_id>/<int:show_id>', methods=['GET', 'POST'])
@login_required
def manage_show(venue_id, show_id):
    show = Show.query.filter_by(id=show_id).first()
    if request.method == "GET":
        name = show.name if show else ""
        rating = show.rating if show else ""
        start_time = show.start_time if show else ""
        end_time = show.end_time if show else ""
        tags = show.tags if show else ""
        ticket_price = show.ticket_price if show else ""

        return render_template("admin_files/web_show-management.html",
                               user=current_user,
                               name=name,
                               rating=rating,
                               start_time=start_time,
                               end_time=end_time,
                               tags=tags,
                               ticket_price=ticket_price)
    else:
        show_name = request.form.get('show_name')
        rating = request.form.get('rating')
        tags = list(request.form.get('tags').split(","))
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        price = request.form.get('price')

        for tag in tags:
            new_tag = Tags(tag=tag, show_id=show_id)
            db.session.add(new_tag)
            db.session.commit()

        new_show = Show(id=show_id,
                        venue_id=venue_id,
                        name=show_name,
                        rating=rating,
                        start_time=datetime.strptime(start_time, '%Y-%m-%dT%H:%M'),
                        end_time=datetime.strptime(end_time, '%Y-%m-%dT%H:%M'),
                        ticket_price=price)
        db.session.add(new_show)
        db.session.commit()
    return redirect(url_for('web_views.venue', venue_id=venue_id))
