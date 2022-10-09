from flask import Flask

app = Flask(__name__)

@app.route("/html")
def html():
    return "<h1>hello, World!</h1>"

@app.route("/json")
def json():
    return {"name": "Sangi"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)