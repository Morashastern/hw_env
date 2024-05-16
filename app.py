from flask import Flask
from hey import hi

app = Flask(__name__)

@app.route("/")
def hello_world():
    return (hi("ELA"))
         