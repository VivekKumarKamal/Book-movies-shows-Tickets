
from . import db
from flask_login import UserMixin
from sqlalchemy import func, ForeignKey

import base64


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20))
    admin = db.Column(db.Integer, default=0)
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    place = db.Column(db.String(35))
    capacity = db.Column(db.Integer)

    shows = db.relationship('Show')

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    rating = db.Column(db.Float)
    ticket_price = db.Column(db.Integer)
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)


    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

    tags = db.relationship('ShowTag')

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))

    tag_id = db.relationship('ShowTag')

class ShowTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))


def init_db():
    db.create_all()

if __name__ == '__main__':
    print("Created")
    init_db()
