# Nginxでリバースプロキシ（未完成）

## flask_python11

- イメージ作成

```shell
docker build ./ -t flask_python:11
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask11 flask_python:11
```

- powershellでjsonデータをPOSTリクエスト

```powrshell
Invoke-RestMethod -Headers @{"Content-type"="application/json"} -Method POST -Body '{"Name":"Sangi","ID":"022500","Age":19}' http://localhost:8080/post
```

- 以下のアドレスにアクセス

    - <http://localhost:8080/get>

- コンテナ停止

```shell
docker stop flask10
```
