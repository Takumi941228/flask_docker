# ESP32マイコンを使ったIoTシステムの製作

## flask_python12

### Arduinoの環境構築

- USBドライバのインストール
    - [Windows](https://www.silabs.com/documents/public/software/CP210x_VCP_Windows.zip)

    - [Linux](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)

- ESP32-DevKit-VEとAE-BME280の接続

![回路図](/flask_sample12/fig.jpg)

- Arduino IDEボードマネージャー

```shell
https://dl.espressif.com/dl/package_esp32_index.json
```

- esp32用のボードを追加
    - <https://github.com/espressif/arduino-esp32>

- 各種ライブラリの追加
    - ArduinoJSON
        - <https://arduinojson.org>

    - SparkFun_BME280
        - <https://github.com/sparkfun/SparkFun_BME280_Arduino_Library>

    - Ticker
        - <https://github.com/sstaub/Ticker>

- Arduino Code
```c++
// 各種ライブラリ
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <SparkFunBME280.h>
#include <WiFi.h>
#include <Ticker.h>

// Wi-Fiの設定
#define WIFI_SSID "SSID"
#define WIFI_PASSWORD "PASSWORD"

// IPアドレスの設定
IPAddress local_ip(XX,XX,XX,XX);
IPAddress subnet(XX,XX,XX,XX);
IPAddress gateway(XX,XX,XX,XX);

//　BME280クラスをインスタンス名bmeとしてインスタンスを生成
BME280 bme;

// BME280_SensorMeasurements構造体名をmeasurementsとして宣言
BME280_SensorMeasurements measurements;

// Tickerクラスをインスタンス名tickerMeasureとしてインスタンスを生成
Ticker tickerMeasure;

//　HTTPClientクラスをインスタンス名httpとしてインスタンスを生成
HTTPClient http;

// JSONを作成する
StaticJsonDocument<JSON_OBJECT_SIZE(5)> json_array;
char json_string[255];

//WiFiへの接続
void setupWiFi() {
  WiFi.config(local_ip, gateway, subnet);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println(".");
    delay(100);
  }

  Serial.println("");
  Serial.print("Connected : ");
  Serial.println(WiFi.localIP());
}

void sendSensorData() {
  //センサからデータの取得
  bme.readAllMeasurements(&measurements);
  Serial.println("Humidity,Pressure,BME-Temp");
  Serial.print(measurements.humidity, 2);
  Serial.print(",");
  Serial.print(measurements.pressure / 100, 2);
  Serial.print(",");
  Serial.println(measurements.temperature, 2);

  // ペイロードを作成してデータを格納
  json_array.clear();
  json_arry["ID"] = String("XX")
  json_array["humid"] = String(measurements.humidity, 2);
  json_array["press"] = String(measurements.pressure / 100, 2);
  json_array["temp"] = String(measurements.temperature, 2);
  serializeJson(json_array, json_string, sizeof(json_string));
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  bme.setI2CAddress(0x77);

  // Begin communication over I2C
  if (bme.beginI2C() == false) {
    Serial.println("The sensor did not respond. Please check wiring.");
  }

  // WiFi接続
  setupWiFi();

  // 5secごとにセンサデータを送信する
  tickerMeasure.attach_ms(5000, sendSensorData);
}

void loop() {
  // if WiFi is down, try reconnecting
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Reconnecting to WiFi...");
    WiFi.disconnect();
    WiFi.reconnect();
  }

  //Check WiFi connection status
  if (WiFi.status() == WL_CONNECTED) {
    http.begin("http://XX.XX.XX.XX:XX/post");
    http.addHeader("Content-Type", "application/json");

    int httpResponseCode = http.POST((uint8_t *)json_string, strlen(json_string));

    if (httpResponseCode > 0) {
      Serial.println(httpResponseCode);
      Serial.println(json_string);
    } else {
      Serial.println("Error on sending POST");
    }
    http.end();

  } else {
    Serial.println("Error in WiFi connection");
  }
  delay(10000);
}
```
- コードの変更点
  - SSID及びPASSWORDの変更
  - ESP32のIPアドレスの設定
  - IDの変更
  - HTTP通信のPOSTリクエスト先のアドレス設定

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
