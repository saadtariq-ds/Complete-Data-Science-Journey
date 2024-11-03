from flask import Flask

'''
It creates an instance of the Flask class, which will be your WSGI
(Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Lecture"

@app.route("/index")
def index():
    return "Welcome to the Index Page"


if __name__ == "__main__":
    app.run(debug=True)