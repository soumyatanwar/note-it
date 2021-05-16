# All route definitions for views
from app import * 
from models import *

# Landing page
@app.route("/")
def home():
    return {"Status": "Success"}, 200 
    
# Create a new note in db - which must have all required cols - title, description and created_user
# Assumes user exists before creation of note and every note will have an owner   
@app.route("/notes", methods=["POST"])
def create_note():
    params = request.json
    result = models.Note(**params)
    db.session.add(result)
    db.session.commit()
    return {"Status": "Success", "result": params}, 201

# List all existing notes in the db
# This can be refined by adding filter/search criterions - which would be used on different pages 
# All incomplete notes (based on _is_done) or notes with 'word' in title/descr or 'time_elapsed' - 
# recently updated/created earliest
@app.route("/notes") # GET request
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

@app.route("/profile", methods=["POST"])
def create_user():
    params = request.json
    result = models.User(**params)
    db.session.add(result)
    db.session.commit()
    return {"Status": "Success", "result": params}, 201
