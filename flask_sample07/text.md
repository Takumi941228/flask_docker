# Jinja2のテンプレートエンジンを学ぶ

## flask_python07

- イメージ作成

```shell
docker build ./ -t flask_python:7
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask07 flask_python:7
```

- 以下のアドレスにアクセス
    - <http://localhost:8080/flask/Sangi>

- コンテナ停止

```shell
docker stop flask07
```
