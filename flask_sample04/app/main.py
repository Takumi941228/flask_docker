from flask import Flask, request

app = Flask(__name__)

@app.route("/method")
def receive_method():
    method=request.method
    return method

@app.route("/url")
def receive_url():
    url=request.url
    return url

@app.route("/host")
def receive_host():
    host=request.host
    return host

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)