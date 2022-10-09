from flask import Flask, render_template

app = Flask(__name__)

@app.route("/flask/<name>")
def index(name):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)