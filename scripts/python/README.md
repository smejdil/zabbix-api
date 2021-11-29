## zabbix-api Python - zabbix-api

### Examples

```console
./auth.py
20: url: http://localhost/api_jsonrpc.php
10: Trying to login with 'Admin':'md5(d947a125599f62d7bf378bd4e76a32cb)'
10: json_obj: {'jsonrpc': '2.0', 'method': 'user.login', 'params': {'user':'Admin', 'password': 'zabbix'}, 'id': 0}
20: Sending: {"jsonrpc": "2.0", "method": "user.login", "params": {"user":"Admin", "password":"zabbix"}, "id": 0}
10: Sending headers: {'Content-Type': 'application/json-rpc', 'User-Agent': 'python/zabbix_api'}
20: Response Code: 200
10: Response Body: {'jsonrpc': '2.0', 'result': 'adb84cb506db2dd79fdc02528a902d37', 'id': 0}
10: json_obj: {'jsonrpc': '2.0', 'method': 'apiinfo.version', 'params': {}, 'id': 1}
20: Sending: {"jsonrpc": "2.0", "method": "apiinfo.version", "params": {}, "id": 1}
10: Sending headers: {'Content-Type': 'application/json-rpc', 'User-Agent': 'python/zabbix_api'}
20: Response Code: 200
10: Response Body: {'jsonrpc': '2.0', 'result': '5.0.17', 'id': 1}
Connected to Zabbix API Version 5.0.17
```