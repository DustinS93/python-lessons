# Concept: Flask intro
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "First Flask"

app.run(debug=True)


