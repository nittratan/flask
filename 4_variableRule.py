#### variable rule

# Flask -Variable Rules:

# By using variable rules we can create a dynamic URL by adding variable parts, to the rule parameter.
# We can define variable rule by <variable-name> using this syntax in our code.
# Variable is always passed as a keyword argument to the function with which the rule is properly associated.

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
  return jsonify("Welcome to Blog page ")


# variable to the function
@app.route('/blog/<int:postID>')
def blogPost(postID):
  return jsonify(f"the post id of this blog {postID}")


# http://127.0.0.1:5000/blog/68


@app.route('/blogPostBy/<userName>')  # default string
def blogPostBy(userName):
  return jsonify(f"this blog is posted by {userName}")


# http://127.0.0.1:5000/blogPostBy/ratan

if __name__ == '__main__':
  app.run(debug=True)
