#!/usr/bin/env python3.8

server="http://localhost/zabbix/"
username="Admin"
password="zabbix"

from pyzabbix import ZabbixAPI
zapi = ZabbixAPI(server=server)
zapi.login(username, password)

# Get list of items on the host
items = zapi.item.get(hostids=10084, output=['itemid','name','key_'])
for item in items:
    print (item['itemid'],item['name'],item['key_'])
