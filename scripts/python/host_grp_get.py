#!/usr/bin/env python3.8

server="http://localhost"
username="Admin"
password="zabbix"

from pyzabbix import ZabbixAPI
zapi = ZabbixAPI(server=server)
zapi.login(username, password)

# Get list of available host groups
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
    print (group['groupid'],group['name'])
