# GETリクエストの違いを学ぶ

## flask_python04

- イメージ作成

```shell
docker build ./ -t flask_python:4
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask04 flask_python:4
```

- 以下のアドレスにアクセス
    - <http://localhost:8080/method>

    - <http://localhost:8080/url>

    - <http://localhost:8080/host>

- コンテナ停止

```shell
docker stop flask04
```
