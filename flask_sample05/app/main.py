from flask import Flask

app = Flask(__name__)

@app.route("/html")
def html():
    return "<!DOCTYPE html><head><title>FlaskをDockerで構築</title></head><body>Flaskを学びましょう!</body><html>"

@app.route("/json")
def json():
    return {"name": "Sangi"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)