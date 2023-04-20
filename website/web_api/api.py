from flask_restful import Resource, fields, marshal_with
from website.web_models import User, Show, Venue


user_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "user_name": fields.String,
    "is_admin": fields.Integer
}

class UserApi(Resource):
    @marshal_with(user_fields)
    def get(self, username):
        user = User.query.filter_by(user_name=username).first()

        if user:
            return user
        else:
            return "", 404

    def put(self, username):
        pass

    def delete(self, username):
        pass

    def post(self):
        pass
