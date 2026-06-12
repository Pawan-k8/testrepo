"import Flask class"
from flask import Flask

"create an instance of the Flask class"
app = Flask(__name__)

"define a route for the root URL"
@app.route('/')
def hello_world():
    "function that handles request"
    return "hello world!"

""" 
"import Flask class"
from flask import Flask, jsonify

"create an instance of the Flask class"
app = Flask(__name__)

"define a route for the root URL"
@app.route('/')
def hello_world():
    "function that handles request"
    return jsonify (message="hello world!")

"""

or 

""" 
"import Flask class"
from flask import Flask

"create an instance of the Flask class"
app = Flask(__name__)

"define a route for the root URL"
@app.route('/')
def hello_world():
    "function that handles request"
    return {"message" : "hello world!"}

"""
