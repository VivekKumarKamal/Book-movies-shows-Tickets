from flask import Blueprint, render_template


web_auth = Blueprint('web_auth', __name__)

@web_auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("web_login.html")


@web_auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("web_sign-up.html")
