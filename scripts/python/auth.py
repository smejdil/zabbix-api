#!/usr/bin/env python3.8

server="http://localhost/zabbix/"
username="Admin"
password="zabbix"

from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server=server, path="", log_level=1)
zapi.login(username, password)

print("Connected to Zabbix API Version %s" % zapi.api_version())
