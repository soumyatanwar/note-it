from app import app, db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
    _is_done = db.Column(db.Boolean, nullable=False, default = False)
    _is_deleted = db.Column(db.Boolean, nullable=False, default = False)
    note_image = db.Column(db.LargeBinary, nullable=True)
    created_user = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))
    
class User(db.Model):
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    bio = db.Column(db.Text, unique=False, nullable=True)
    friendly_name = db.Column(db.String(20), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

# db.create_all() # should only create db once
