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
    secQuestion=db.Column(db.String(30))
    answer=db.Column(db.String(30))
    diaries=db.relationship('Diary')

    def __init__(self,email,firstName,lastName,password,secQuestion,answer):
        self.email=email
        self.firstName=firstName
        self.lastName=lastName
        self.password=password
        self.secQuestion=secQuestion
        self.answer=answer

class Diary(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    privacy=db.Column(db.String(10))
    name=db.Column(db.String(150))
    user_id=db.Column(db.Integer, db.ForeignKey('User.id'))

