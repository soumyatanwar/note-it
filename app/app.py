# load db url from the env variable. you can use python-dotenv package

from flask import Flask, request
from dotenv import load_dotenv 
import os

load_dotenv()
db_url = os.environ["DATABASE_URL"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

import models

@app.route("/")
def home():
    return {"Status": "Success"}, 200 
    
@app.route("/notes", methods=["POST"])
def create_note():
    params = request.json
    result = models.Note.create(**params)
    print(result)
    return {"Status": "Success", "result": result}, 201
    # models.db.session.add(result)
    # models.db.session.commit()

@app.route("/notes")
def show_notes():
    result = models.Note.query.filter_by().all()
    print(result)
    return {"Status": "Success", "result": result}, 201

# Run the app in port 5000 and in debug mode
if __name__ == '__main__':
    models.db.create_all()
    models.db.init_app(app)
    app.run(port=5000, debug=True)