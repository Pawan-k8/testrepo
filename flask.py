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
""" 
# Import the Flask class from the flask module
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

@app.route("/no_content")
def no_content():
    "no content found"
    return ({"message":"no content found"},204)

@app.route("/exp")
def index_explict():
    resp = make_response({"message":"hello_world"})
    resp.status_code = 200
    return resp
"""

