# Concept: Flask intro
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about.html", name="Dustin")

@app.route("/other")
def other():
    return render_template("home.html")

app.run(debug=True)

