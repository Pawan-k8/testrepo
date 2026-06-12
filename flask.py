"import Flask class"
from flask import Flask

"create an instance of the Flask class"
app = Flask(__name__)

"define a route for the root URL"
@app.route('/')
def hello_world():
    "function that handles request"
    return "hello world!"

