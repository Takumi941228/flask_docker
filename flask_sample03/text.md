# flask_python03

- イメージ作成

```shell
docker build ./ -t flask_python:3
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask03 flask_python:3
```

- <http://localhost:8080/username/sangi>

- <http://localhost:8080/userid/021500>

- コンテナ停止

```shell
docker stop flask03
```
