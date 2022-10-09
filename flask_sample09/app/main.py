import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/post", methods=['POST'])
def http_post():
    if request.method == 'POST':
        json_data =  request.json
        print(json_data)

        # jsonデータを辞書型としてJSON形式でファイルに書き込む
        with open('json_file.json', 'w', encoding='UTF-8') as file:
            json.dump(json_data, file)

        return 'response_json'

@app.route("/get", methods=['GET'])
def http_get():
    if request.method == 'GET':
        # JSONファイルからjsonデータを読み込む
        with open('json_file.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)

        return render_template(
            'index.html', 
            name=data["Name"],
            id=data["ID"],
            age=data["Age"]
        )
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)