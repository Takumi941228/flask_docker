# flask_python01

- イメージ作成

```shell
docker build ./ -t flask_python:1
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask01 flask_python:1
```

- pythonから`ctrl+D`で抜ける

- コンテナ起動

```shell
docker start flask01
```

- /bin/bashで`Debian`に入る

```shell
docker exec -it flask01 /bin/bash
```

- プログラム名`main`を環境変数FLASK_APPに設定

```shell
export FLASK_APP=main
```

- flaskを実行

```shell
flask run -h 0.0.0.0 -p 8080
```

- <http://localhost:8080>

- コンテナ停止(ポート使用を解放)

```shell
docker stop flask01
```
