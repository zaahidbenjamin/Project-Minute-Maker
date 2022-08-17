from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dates = db.Column(db.String(10000))
    Topic = db.Column(db.String(10000))
    Attendees = db.Column(db.String(10000))
    Raisedby = db.Column(db.String(10000))
    Actionrequired = db.Column(db.String(10000))
    Actionedby  = db.Column(db.String(10000))
    Information     = db.Column(db.String(10000))
    Dateofcompletion = db.Column(db.String(10000))

    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')