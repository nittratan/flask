# flask basics
# flask is a microframework of python for web development 
# flask is a microframework because it does not require particular tools or libraries
# flask use for restful api development
# flask is a lightweight WSGI web application framework

# basic structure of flask application

# import the Flask class from the flask module

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


# run the application
# python basic.py
# flask --app basic --debug run


# run the application in debug mode

# Running on http://127.0.0.1:5000/
