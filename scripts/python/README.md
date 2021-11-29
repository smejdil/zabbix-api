## zabbix-api Python


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

```console
./host_grp_get.py 
1 Templates
2 Linux servers
4 Zabbix servers
5 Discovered hosts
6 Virtual machines
7 Hypervisors
```

```console
./hosts_get.py
10084 Zabbix server
10728 Zabbix A remote
10729 Zabbix B remote
10730 Zabbix C remote
```

```console
./items_get.py
...
29200 CPU utilization system.cpu.util
29165 CPU guest time system.cpu.util[,guest]
29164 CPU guest nice time system.cpu.util[,guest_nice]
29173 CPU idle time system.cpu.util[,idle]
29167 CPU interrupt time system.cpu.util[,interrupt]
29162 CPU iowait time system.cpu.util[,iowait]
29169 CPU nice time system.cpu.util[,nice]
29166 CPU softirq time system.cpu.util[,softirq]
29168 CPU steal time system.cpu.util[,steal]
29172 CPU system time system.cpu.util[,system]
29171 CPU user time system.cpu.util[,user]
...
```
