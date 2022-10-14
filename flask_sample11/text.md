# Nginxでリバースプロキシ

## flask_python11

- webとproxyのイメージ作成

```shell
docker-compose build --no-cache
```

- flaskとnginxのコンテナ作成と起動

```shell
docker-compose up -d
```

- powershellでjsonデータをPOSTリクエスト

```powrshell
Invoke-RestMethod -Headers @{"Content-type"="application/json"} -Method POST -Body '{"ID":"01","Temp":25.6,"Humi":55.4,"Press":999.3}' http://localhost:8080/post
```

- 以下のアドレスにアクセス

    - <http://localhost:8080/get>

- nginxのコンテナに/bin/bashで入る

```shell
docker exec -it nginx /bin/bash
```

- nginxのサービスを再起動

```shell
service nginx restart
```

- 以下のアドレスにアクセス(xはコンテナのIPアドレス(WSl))

    - <http://xx.xx.xx.xx/sangi>
    - <http://localhst/sangi>

- コンテナ停止

```shell
docker-compose down
```
