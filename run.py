import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "luggage9#9#"
messages = []
# Hard-coded url to avoid redirecting to localhost. This problem needs investigated in due course.
app_url = "https://5000-ba52b9a9-48ff-4236-ad65-8b8bf116efb5.ws-eu01.gitpod.io/"

def add_messages(username, message):
    """ Add a chat message. """
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = { "timestamp": now, "from": username, "message": message}

    messages.append(messages_dict)

@app.route('/', methods = ["GET", "POST"])
def index():
    """ Main page with instructions """

    if request.method == "POST":
        """ Save the entered username in a Session cookie. """
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(app_url + session["username"])
    
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """ Display chat messages. """
    return render_template("chat.html", username = username, chat_messages = messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect back to chat page. """
    add_messages(username, message)
    return redirect(app_url + username)

app.run(host=os.getenv('IP'),
        port=os.getenv('PORT'),
        debug=True)