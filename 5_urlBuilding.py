### url building
# URL Binding in Flask
# Dynamic Urls in Flask

from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
  return jsonify("Welcome to the home page")


# @app.route("/users/<username>")
# def users(username):
#     return f"User Name : {username}"
# # http://127.0.0.1:5000/users/ratan


@app.route("/admin")
def api_admin():
  return jsonify("Hello Admin")


@app.route("/guest/<guestName>")
def api_guest(guestName):
  return jsonify(f"Hello guest {guestName}")


# url_for() function is used to build a URL to the specific function dynamically.
@app.route('/users/<name>')
def users(name):
  if name == 'admin':
    return redirect(url_for('api_admin'))
  else:
    return redirect(url_for('api_guest', guestName=name))


if __name__ == "__main__":
  app.run(debug=True)
