# load db url from the env variable. you can use python-dotenv package

from flask import Flask, request
from dotenv import load_dotenv 
import os
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# print(dir(Marshmallow))

load_dotenv()
db_url = os.environ["DATABASE_URL"]
print(db_url)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
# ma = Marshmallow(app)

import models

# class UserSchema(SQLAlchemySchema):
#     class Meta:
#         model = Note
        
#     username = ma.auto_field()
#     password = ma.auto_field()
#     user = ma.auto_field()

# class NoteSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Note
#         include_fk = True

# class UserProfileSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = UserProfile
#         include_fk = True

# user_schema = UserSchema()
# note_schema = NoteSchema()
# user_profile_schema = UserProfileSchema()
# # author = Author(name="Chuck Paluhniuk")
# # book = Book(title="Fight Club", author=author)
# # db.session.add(author)
# # db.session.add(book)
# # db.session.commit()
# author_schema.dump(author)

@app.route("/")
def home():
    return {"Status": "Success"}, 200 
    
# Create a new note in db    
@app.route("/notes", methods=["POST"])
def create_note():
    params = request.json
    result = models.Note(**params)
    print(type(result))
    print(result)
    # print(note_schema.dump(result))
    db.session.add(result)
    db.session.commit()
    return {"Status": "Success", "result": params}, 201

@app.route("/profile", methods=["POST"])
def create_user():
    params = request.json
    result = models.User(**params)
    db.session.add(result)
    db.session.commit()
    return {"Status": "Success", "result": params}, 201

# List all existing notes in the db
@app.route("/notes")
def show_notes():
    notes = models.Note.query.filter_by().all()
    return {"Status": "Success", "result": "response"}, 201

# Run the app in port 5000 and in debug mode
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)