from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, defautlt=datetime.utc)
    _is_done = db.Column(db.Boolean, nullable=False)
    _is_deleted = db.Column(db.Boolean, nullable=False)
    note_image = db.Column(db.LargeBinary, nullable=False)
    created_user = db.Column(db.Integer, db.ForeignKey('user.username'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))
    
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class UserProfile(db.Model):
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.Text, unique=False, nullable=True)
    username = db.Column(db.Integer, db.ForeignKey('user.username'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<Profile %r>' % self.bio