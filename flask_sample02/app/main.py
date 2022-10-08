from flask import Flask

app = Flask(__name__)

@app.route("/world")
def hello_world():
    return "Hello, World!"

@app.route("/python")
def hello_python():
    return "Hello, Python!"

@app.route("/sangi")
def hello_sangi():
    return "Hello, Sangi!"

@app.route("/python/flask")
def hello_python_flask():
    return "Hello, Python, flask!"
