# M5マイコンを使ったIoTシステムの製作

## flask_python13

### M5マイコンの環境構築

- M5Bunnerのインストール
    - [Windows](https://m5burner.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)

    - [Linux](https://m5burner.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip)

![回路図](/flask_sample13/figure2.png)

- 手順
  - 使用するボードのファイルをダウンロードする。
  - USBシリアルケーブルでPCとボードを接続する.
  - configurationでCOMポートの設定
  - BurnでSSIDとPASSWORDの設定

- M5Flow
  - 以下のアドレスから開発環境にアクセス
    - <https://flow.m5stack.com/>

![回路図](/flask_sample13/figure.png)

sample.m5fを開く、ボードにダウンロードする。
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
