from flask import Flask
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'ticket_show_db.sqlite3'
def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = "It's a ticket show web app, built by Vivek"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    login_manager = LoginManager()
    login_manager.login_view = 'web_views.home'
    login_manager.login_message = "Log in to access the page"
    login_manager.init_app(app)

    from .web_models import User, Venue, Show, Tags, ShowTag
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .web_views import web_views
    from .web_auth import web_auth

    app.register_blueprint(web_views)
    app.register_blueprint(web_auth)

    with app.app_context():
        db.create_all()


    return app
