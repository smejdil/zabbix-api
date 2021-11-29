#!/usr/bin/env python3

server="http://localhost"
username="Admin"
password="zabbix"

from pyzabbix import ZabbixAPI
zapi = ZabbixAPI(server=server)
zapi.login(username, password)

# Get list of hosts in the host group
groupid = 4
hosts = zapi.host.get(groupids=groupid, output=['hostid'])

# Get list of items for the hosts
host_ids = [host['hostid'] for host in hosts]
for host_id in host_ids:
    items = zapi.item.get(hostids=[host_id], output=['itemid','name','key_'])
    for item in items:
        print (item['itemid'],item['name'],item['key_'])
