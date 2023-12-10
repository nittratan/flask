# flask basics

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Flask World!'


@app.route('/aboutUs')
def aboutUs():
    return 'About Us Page'


# parameter for run method

# debug=True
# Defaults to false. If set to true, provides a debug information. The server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.
# host

# Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally as well.
# host='localhost'


# port=5000
# Defaults to 5000

if __name__ == '__main__':
    app.run(host='localhost' , port=5000 , debug=True)


# to run the application
# python basic1.py
# flask --app basic1 --debug run

