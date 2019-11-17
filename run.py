import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "luggage9#9#"
messages = []
# Hard-coded url to avoid redirecting to localhost. This problem needs investigated in due course.
app_url = "https://5000-ba52b9a9-48ff-4236-ad65-8b8bf116efb5.ws-eu01.gitpod.io/"

def add_message(username, message):
    """ Add a chat message to the message list. """
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({ "timestamp": now, "from": username, "message": message})

@app.route('/', methods = ["GET", "POST"])
def index():
    """ Main page with instructions """
    if request.method == "POST":
        """ Save the entered username in a Session cookie. """
        session["username"] = request.form["username"]

    if "username" in session:
        #return redirect(app_url + session["username"])
        return redirect(app_url + url_for("user", username = session["username"]))
    return render_template("index.html")

@app.route('/chat/<username>', methods = ["GET", "POST"])
def user(username):
    """ Add and display chat messages. """
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(app_url + url_for("user", username = session["username"]))

    return render_template("chat.html", username = username, chat_messages = messages)

app.run(host=os.getenv('IP'),
        port=os.getenv('PORT'),
        debug=True)