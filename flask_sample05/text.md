# GETリクエストでHTMLとjsonを表示する

## flask_python05

- イメージ作成

```shell
docker build ./ -t flask_python:5
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask05 flask_python:5
```

- 以下のアドレスにアクセス
    - <http://localhost:8080/html>

    - <http://localhost:8080/json>

- コンテナ停止

```shell
docker stop flask05
```