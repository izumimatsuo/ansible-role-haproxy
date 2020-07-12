# ansible-role-haproxy [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-haproxy)

CentOS 7 に haproxy/keepalived を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名             | デフォルト値| 説明               |
| ------------------ | ----------- | ------------------ |
| haproxy_frontend_bind | *:80     | LISTENポート番号   |
| haproxy_balance_logic | roundrobin | 振分けロジック   |
| haproxy_backend_servers | []     | 振分け先サーバ     |
| keepalived_check_interface | none | チェックするNIC   |
| keepalived_virtual_ipaddr | none | VIP                |
