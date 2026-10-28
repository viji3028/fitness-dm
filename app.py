
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Project files are stored in the same folder as app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/register")
def register():
    return send_from_directory(BASE_DIR, "register.html")

@app.route("/login")
def login():
    return send_from_directory(BASE_DIR, "login.html")

@app.route("/dashboard")
def dashboard():
    return send_from_directory(BASE_DIR, "dashboard.html")

@app.route("/style.css")
def stylesheet():
    return send_from_directory(BASE_DIR, "style.css")

if __name__ == "__main__":
    app.run(debug=True)
