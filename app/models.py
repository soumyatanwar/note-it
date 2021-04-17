from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    created_on = db.Column(db.Date(), nullable=False)
    # _is_done
    # _is_deleted
    # created_user_id
    # shared_with_user_id