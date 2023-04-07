
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

    venues = db.relationship('Venue')



class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    place = db.Column(db.String(35))
    location = db.Column(db.String(50))
    capacity = db.Column(db.Integer)
    availability = db.Column(db.Integer, default=capacity)

    shows = db.relationship('Show', backref='venue', passive_deletes=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    rating = db.Column(db.Float)
    ticket_price = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id', ondelete="CASCADE"))

    #This will look to ShowTag
    tags = db.relationship('Tags', backref='show', passive_deletes=True)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25))
    show_id = db.Column(db.Integer, db.ForeignKey('show.id', ondelete='CASCADE'))


def init_db():
    db.create_all()

if __name__ == '__main__':
    print("Created")
    init_db()
