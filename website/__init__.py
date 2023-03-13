from flask import Flask

def create_app():
    app = Flask(__name__)
    app.debug = True

    from .web_views import web_views
    from .web_auth import web_auth

    app.register_blueprint(web_views)
    app.register_blueprint(web_auth)


    return app
