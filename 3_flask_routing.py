# routing
# Flask app routing
# App Routing means mapping the URLs to a specific function that will handle the logic for that URL.

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
  return jsonify("Welcome to home page")


def aboutUs():
  return jsonify("I am a Software Engineer ")


# add_url_rule()

# syntax - add_url_rule(<url rule>, <endpoint>, <view function>)

app.add_url_rule("/about", "about", aboutUs)
# http://127.0.0.1:5000/about

if __name__ == "__main__":
  app.run(debug=True)
