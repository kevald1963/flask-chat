import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return("<h1>Hello!</h1>")

app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)