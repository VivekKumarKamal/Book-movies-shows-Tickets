from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, current_user
from . import db
from .web_models import User, Venue, Show, ShowTag, Tags


web_views = Blueprint('web_views', __name__)

@web_views.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.admin == 1:
            new_id = db.session.query(db.func.max(Venue.id)).filter_by(admin_id=current_user.id).scalar()

            new_id = 1 if not new_id else new_id + 1
            print(new_id)
            return render_template("admin_files/web_admin-dashboard.html", user=current_user, id=new_id)
        else:
            return render_template("user_files/web_user-dashboard.html", user=current_user)
    else:
        return render_template("web_home.html")


@web_views.route('/search')
@login_required
def search():
    return "hal"





