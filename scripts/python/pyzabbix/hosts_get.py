#!/usr/bin/env python3.8

server="http://localhost/zabbix/"
username="Admin"
password="zabbix"

from pyzabbix import ZabbixAPI
zapi = ZabbixAPI(server=server)
zapi.login(username, password)

# Get list of hosts in a host group
hosts = zapi.host.get(groupids=4, output=['hostid','name'])
for host in hosts:
    print (host['hostid'],host['name'])