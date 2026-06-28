# Concept: Flask intro
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "First Flask"

@app.route("/other")
def other():
    return "<h1>First Time Ever</h1> <br> <p>This is the start of a revolution</p>"

app.run(debug=True)


