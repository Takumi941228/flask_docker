# flask_python06

- イメージ作成

```shell
docker build ./ -t flask_python:6
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask06 flask_python:6
```

- <http://localhost:8080/html>

```shell
docker stop flask06
```