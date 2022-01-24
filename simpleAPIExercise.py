from Flask import flask # import Flask.flask
import json

app = Flask(__name__)
# @ is a python decorator
# The decorator lets us use a Flask function called app without making
# changes to app function

longDistanceRunners = ['Mike', 'Joanne', 'Fred', 'Sally']
highJumpers = ['Sara', 'Ted', 'Mary', 'Kyle']
athletes = longDistanceRunners + highJumpers

@app.route("/")
def home ():
    return "Hello World" + athletes

@app.route("/users/<user>", methods=['GET'])
def users(athletes):
    return json.dumps("Hello "+ athletes)