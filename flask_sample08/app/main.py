from flask import Flask, request

app = Flask(__name__)

@app.route("/post", methods=['POST'])
def http_post():
    if request.method == 'POST':
        json_data =  request.json
        print(json_data)
    return 'response_json'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)