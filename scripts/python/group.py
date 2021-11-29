#!/usr/bin/env python3.8

server="http://localhost/zabbix/"
username="Admin"
password="zabbix"

from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server=server, path="", log_level=0)
zapi.login(username, password)

print("Connected to Zabbix API Version %s" % zapi.api_version())

hostgroups = zapi.hostgroup.get({"output": "extend", "sortfield": "name"}) # for groupid
print (hostgroups)
