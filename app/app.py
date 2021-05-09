# load db url from the env variable. you can use python-dotenv package

from flask import Flask, request
from dotenv import load_dotenv 
import os
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db_url = os.environ["DATABASE_URL"]
print(db_url)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
import models

@app.route("/")
def home():
    return {"Status": "Success"}, 200 
    
# Create a new note in db    
@app.route("/notes", methods=["POST"])
def create_note():
    params = request.json
    result = models.Note(**params)
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
    
    response = []
    for note in notes:
        returned_note = {
        "id": note.id, 
        "title": note.title,
        "description":note.description, 
        "created_on":note.created_on, # will not be modified under any circumstances
        "updated_on":note.updated_on, # will be changed on any modification to note 
        "_is_done":note._is_done, # needs to triggered based on a UI interaction
        "_is_deleted":note._is_deleted, # soft delete, triggered by UI interaction
        "note_image":note.note_image # optional addition
        }
        response.append(returned_note)

    return {"Status": "Success", "result": response}, 201

# Run the app in port 5000 and in debug mode
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)