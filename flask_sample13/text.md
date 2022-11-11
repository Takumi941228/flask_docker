# EM%マイコンを使ったIoTシステムの製作

## flask_python13

### Webアプリの環境構築

- webとproxyのイメージ作成

```shell
docker-compose build --no-cache
```

- flaskとnginxのコンテナ作成と起動

```shell
docker-compose up -d
```

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
