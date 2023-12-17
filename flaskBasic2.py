from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
  return jsonify("Hello world !")


if __name__ == '__main__':
  app.run()

# to run this app

# syntax - python fileName.py
