# POSTリクエストとGETリクエストを学ぶ

## flask_python09

- イメージ作成

```shell
docker build ./ -t flask_python:9
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask09 flask_python:9
```

- powershellでjsonデータをPOSTリクエスト

```powrshell
Invoke-RestMethod -Headers @{"Content-type"="application/json"} -Method POST -Body '{"Name":"Sangi","ID":"022500","Age":19}' http://localhost:8080/post
```

- 以下のアドレスにアクセス
    - <http://localhost:8080/get>

- コンテナ停止

```shell
docker stop flask09
```
