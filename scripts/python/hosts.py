#!/usr/bin/env python3.8

server="http://localhost"
username="Admin"
password="zabbix"

from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server=server, path="", log_level=0)
zapi.login(username, password)

print("Connected to Zabbix API Version %s" % zapi.api_version())

hosts = zapi.host.get({"groupids": "4", "output": ["hostid","name", "host"]}) # for host and name
print (hosts)