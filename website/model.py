from datetime import timezone
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    __tablename__= 'User'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150), unique=True)
    firstName=db.Column(db.String(150))
    lastName=db.Column(db.String(150))
    password=db.Column(db.String(150))
    diaries=db.relationship('Diary')

    def __init__(self,email,firstName,lastName,password):
        self.email=email
        self.firstName=firstName
        self.lastName=lastName
        self.password=password

class Diary(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

