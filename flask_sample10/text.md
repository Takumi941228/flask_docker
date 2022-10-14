# Webアプリ（IoTシステム）の制作

## flask_python10

- イメージ作成

```shell
docker build ./ -t flask_python:10
```

- コンテナ作成と起動

```shell
docker run -it -p 8080:8080 --name flask10 flask_python:10
```

- powershellでjsonデータをPOSTリクエスト

```powrshell
Invoke-RestMethod -Headers @{"Content-type"="application/json"} -Method POST -Body '{"ID":"01","Temp":25.6,"Humi":55.4,"Press":999.3}' http://localhost:8080/post
```

- 以下のアドレスにアクセス

    - <http://localhost:8080/get>

- コンテナ停止

```shell
docker stop flask10
```
