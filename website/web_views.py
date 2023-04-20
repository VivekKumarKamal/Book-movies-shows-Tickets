import calendar

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user
from . import db
from .web_models import User, Venue, Show, Tags


web_views = Blueprint('web_views', __name__)

# here are the IDs of admins, if I'll add more admins, then I'll add the IDs here and I'll add some code
# in the view below at venues
admins = [1]

@web_views.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.admin == 1:
            new_id = db.session.query(db.func.max(Venue.id)).filter_by(admin_id=current_user.id).scalar()

            new_id = 1 if not new_id else new_id + 1

            return render_template("admin_files/web_admin-dashboard.html", user=current_user, new_venue_id=new_id)
        else:


            venues = User.query.filter_by(id=admins[0]).first().venues

            return render_template("user_files/web_user-dashboard.html", user=current_user, venues=venues, calendar=calendar)
    else:
        return render_template("web_home.html")


@web_views.route('/searched/<searched>', methods=['GET', 'POST'])
@login_required
def searched(searched):
    lis = set(Show.query.filter(Show.name.like('%' + searched + '%')))
    lis_by_tag = list(Tags.query.filter(Tags.tag.like('%' + searched + '%')))
    lis_by_venue = list(Venue.query.filter(Venue.name.like('%' + searched + '%')))
    lis_by_location = list(Venue.query.filter(Venue.location.like('%' + searched + '%')))
    lis_by_place = list(Venue.query.filter(Venue.place.like('%' + searched + '%')))
    for a in lis_by_tag:
        lis.add(a.show)
    for a in lis_by_venue:
        for s in a.shows:
            lis.add(s)
    for a in lis_by_location:
        for s in a.shows:
            lis.add(s)
    for a in lis_by_place:
        for s in a.shows:
            lis.add(s)

    return render_template('web_search-results.html', searched=searched, user=current_user, shows=lis, calendar=calendar)


@web_views.route('/venue/<int:venue_id>')
@login_required
def venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()

    if venue:
        new_id = db.session.query(db.func.max(Show.id)).scalar()

        new_id = 1 if not new_id else new_id + 1

        return render_template("admin_files/web_venue.html", venue=venue,
                               new_show_id=new_id,
                               venue_id=venue_id,
                               calendar=calendar,
                               user=current_user)



@web_views.route('/bookings')
@login_required
def bookings():
    if current_user.admin == 1:
        flash('Log in as user to book/view tickets', category='error')
        return redirect(url_for('web_views.home'))

    return render_template('user_files/web_bookings.html', user=current_user, calendar=calendar)