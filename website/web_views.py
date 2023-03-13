from flask import Blueprint, render_template


web_views = Blueprint('web_views', __name__)

@web_views.route("/")
def hello_world():
    return render_template("web_feed.html")


