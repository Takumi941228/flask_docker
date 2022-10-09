# flask_python07

- イメージ作成

```shell
docker build ./ -t flask_python:7
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask07 flask_python:7
```

- <http://localhost:8080/flask/Sangi>

```shell
docker stop flask07