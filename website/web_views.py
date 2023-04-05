from flask import Blueprint, render_template
from flask_login import login_user, login_required, current_user


web_views = Blueprint('web_views', __name__)

@web_views.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.admin == 1:
            return render_template("admin_files/web_admin-dashboard.html")
        else:
            return render_template("user_files/web_user-dashboard.html")
    else:
        return render_template("web_home.html")


@web_views.route('/search')
@login_required
def search():
    return "hal"
