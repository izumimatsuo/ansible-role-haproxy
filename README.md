# ansible-role-haproxy [![Build Status](https://travis-ci.com/izumimatsuo/ansible-role-haproxy.svg?branch=master)](https://travis-ci.com/izumimatsuo/ansible-role-haproxy)

CentOS 7 に haproxy を導入する ansible role です。
SSL 通信するためには、以下のとおりに証明書が配置されていること
（配置されていなかった場合は、自己署名証明書を作成して配置します）

- /etc/haproxy/cert/server.pem

## 設定項目

以下の設定項目は上書き可能。

| 項目名                  | デフォルト値       | 説明               |
| ----------------------- | ------------------ | ------------------ |
| haproxy_ssl_on          | yes                | SSL通信を適用する  |
| haproxy_listen_port     | 443                | ポート番号（SSL通信適用を設定しない場合は 80 に自動変更）|
| haproxy_backend_servers | ['127.0.0.1:8080'] | 振分け先サーバ 例 ['192.168.33.21:8080', '192.168.33.22:8080'] |
