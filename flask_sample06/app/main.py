from flask import Flask

app = Flask(__name__)

html = '''
<h1>FlaskでWebアプリ開発</h1>
<ul>
    <li>Dockerで開発環境を構築</li>
    <li>FlaskでHello World!</li>
    <li>Pythonを学ぶ</li>
</ul>
'''
@app.route("/html")
def index():
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)