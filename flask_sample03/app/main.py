from flask import Flask, escape

app = Flask(__name__)

@app.route("/username/<name>")
def user_name(name):
    print(name)
    return f'Name:{escape(name)}'

@app.route("/userid/<int:id>")
def user_id(id):
    print(id)
    return f'ID:{id}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)