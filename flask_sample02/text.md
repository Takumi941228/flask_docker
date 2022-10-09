# flask_python02

- イメージ作成

```shell
docker build ./ -t flask_python:2
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask02 flask_python:2
```

- pythonから`ctrl+D`で抜ける

- コンテナ起動

```shell
docker start flask02
```

- /bin/bashで`Debian`に入る

```shell
docker exec -it flask02 /bin/bash
```

- プログラム名`main`を環境変数FLASK_APPに設定

```shell
export FLASK_APP=main
```

- flaskを実行

```shell
flask run -h 0.0.0.0 -p 8080
```

- <http://localhost:8080/world>

- <http://localhost:8080/python>

- <http://localhost:8080/sangi>

- <http://localhost:8080/python/flask>

- ルーティングの追加

```shell
vim main.py
```

```python
@app.route("/name")
def name():
    return "Hello, Takumi!"
```

- コンテナ停止

```shell
docker stop flask02
```
