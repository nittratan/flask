# basic.py
# basic of flask

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
  return jsonify("welcome to the home page")


# to run this file used the following Command
# syntax -  python -m flask --<app_name> <file_name> run

# ex -  python -m flask --app basic run

# flaskBasic1.py
