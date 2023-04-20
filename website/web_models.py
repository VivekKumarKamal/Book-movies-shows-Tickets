
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
    bookings = db.relationship('Booking')



class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    place = db.Column(db.String(35))
    location = db.Column(db.String(50))
    capacity = db.Column(db.Integer)

    shows = db.relationship('Show', backref='venue', passive_deletes=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'location': self.location,
            'capacity': str(self.capacity)
        }
        return data

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    rating = db.Column(db.Float)
    ticket_price = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, nullable=False)
    timing = db.Column(db.Integer)

    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id', ondelete="CASCADE"))
    availability = db.Column(db.Integer)

    tags = db.relationship('Tags', backref='show', passive_deletes=True)
    bookings = db.relationship('Booking', backref='show', passive_deletes=True)


    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'ticket_price': self.ticket_price,
            'start_time': str(self.start_time),
            'duration': self.timing
        }
        return data
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    show_id = db.Column(db.Integer, db.ForeignKey('show.id', ondelete="CASCADE"))


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25))
    show_id = db.Column(db.Integer, db.ForeignKey('show.id', ondelete='CASCADE'))


def init_db():
    db.create_all()

if __name__ == '__main__':
    print("Created")
    init_db()
