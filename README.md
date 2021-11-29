## zabbix-api

This small project for Zabbix API examples

## Dependencies

- Zabbix API Perl script has been tested on FreeBSD 
- Package - Perl - p5-JSON-RPC - JSON::RPC::Legacy::Client

- Zabbix API Python script has been tested on FreeBSD
- Package - Python - zabbix-api

### Installation

```console
# Perl
cd /usr/ports/devel/p5-JSON-RPC && make install clean
man JSON::RPC::Legacy::Client

# Python
cd /usr/ports/devel/py-pip && make install clean
pip install zabbix-api
Requirement already satisfied: zabbix-api in /usr/local/lib/python3.8/site-packages (0.5.4)

pip list | grep zabbix
zabbix-api                    0.5.4
```

## Examples

```console
./auth.pl
Authentication successful. Auth ID: 8bf1e5e70bddb2bec567e267cc314dfd
```

```console
./group.pl
Authentication successful. Auth ID: 13f9bc7ec7beffd994b8f748783fff4e
List of hostgroup
-----------------------------
Group ID: 1 Host group: Templates
Group ID: 2 Host group: Linux servers
Group ID: 4 Host group: Zabbix servers
Group ID: 5 Host group: Discovered hosts
Group ID: 6 Host group: Virtual machines
Group ID: 7 Host group: Hypervisors
```

```console
./hosts.pl
Authentication successful. Auth ID: c0750acbd3dd3ca7f380e8a32c9dfb56
List of hosts
-----------------------------
Host ID: 75086 Host: Zabbix-proxy-HW-01
Host ID: 10084 Host: Zabbix-server-HW
Host ID: 76844 Host: zabbix-proxy-VM-01
Host ID: 76845 Host: zabbix-proxy-VM-02
Host ID: 76846 Host: zabbix-proxy-VM-03
```

```console
./users.pl
Authentication successful. Auth ID: 7c158c569b91e3fa0627afdf98556d40
List of users
-----------------------------
User ID: 1 Alias: Admin Name: Zabbix Surname: Administrator
```

```console
./auth.py
20: url: https://zabbix.pfsense.cz/api_jsonrpc.php
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

## To do

- other languages
