# ansible-role-haproxy [![Build Status](https://travis-ci.com/izumimatsuo/ansible-role-haproxy.svg?branch=master)](https://travis-ci.com/izumimatsuo/ansible-role-haproxy)

CentOS 7 に haproxy を導入する ansible role です。

SSL 通信するためには、以下のとおりにリスナー設定と証明書が配置されていること

- haproxy_listeners: [{listen_port: 443, protocol: 'https', ssl_certificate: '/etc/haproxy/cert/server.pem', default_backend: 'default'}]

## 設定項目

以下の設定項目は上書き可能。

| 項目名                     | デフォルト値       | 説明               |
| -------------------------- | ------------------ | ------------------ |
| haproxy_always_on_ssl      | no                 | 常時SSL化          |
| haproxy_frontend_listeners | [{listen_port: 80, protocol: 'http', ssl_certificate:, default_backend: 'default'}] | リスナー |
| haproxy_backend_targets    | [{name: 'default', listen_port: 80, protocol: 'http', servers: ['127.0.0.1']}] | 振分け先グループ |
