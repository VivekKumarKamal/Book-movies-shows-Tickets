from flask import Blueprint


web_models = Blueprint('web_models', __name__)

@web_models.route("/")
def hello_world():
    return "<p>Hello, World!</p>"