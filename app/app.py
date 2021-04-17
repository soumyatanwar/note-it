# load db url from the env variable. you can use python-dotenv package

from flask import Flask, request
from dotenv import load_dotenv 

load_dotenv()
db_url = os.environ["DATABASE_URL"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

import models

@app.route("/")
def home():
    return {"Status": "Success"}, 200 


# Run the app in port 5000 and in debug mode
if __name__ == '__main__':
    app.run(port=5000, debug=True)