# POSTリクエストを学ぶ

## flask_python08

- イメージ作成

```shell
docker build ./ -t flask_python:8
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask08 flask_python:8
```

- powershellでjsonデータをPOSTリクエスト

```powrshell
Invoke-RestMethod -Headers @{"Content-type"="application/json"} -Method POST -Body '{"Name":"Sangi","ID":"022500","Age":19}' http://localhost:8080/post
```

- コンテナ停止

```shell
docker stop flask08
```
