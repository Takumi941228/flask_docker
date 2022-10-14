import json
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/post", methods=['POST'])
def http_post():
    if request.method == 'POST':
        json_data = request.json
        print(json_data)

        # 現在時刻を取得
        now_time=datetime.now()
        # str型にエンコード
        str_time=str(now_time)
        # dict型にエンコード
        dict_time = {"Time": str_time}
        # dict型に結合
        json_data.update(dict_time)

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
            id=data["ID"],
            time=data["Time"],
            temp=data["Temp"],
            humi=data["Humi"],
            press=data["Press"]
        )
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)