#!/usr/local/bin/python
import sys
import json
import ast

"""This script prepares vlan, mac, and interface info
   for each device in the hosts file """
def main():
    """Convert argument to list"""
    hosts = sys.argv[1]
    path = sys.argv[2]
    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    """Put data for all hosts in json"""
    all_host_data = []

    for host in hosts:
        filename = 'build/'+host+'/ethernet_switching_table.json'
        with open(filename,'r') as f:
            newval = {}
            newval['hostname'] = host
            newval['mac-table'] = json.load(f)
            all_host_data.append(newval)
    
    """Get the vlan tag info"""
    vlans = []
    for host in hosts:
        filename = 'build/'+host+'/vlan-information.json'
        with open(filename,'r') as f:
            data = json.load(f)
            for vlan in data:
                newval = {}
                try:
                    newval['vlan-name'] = vlan['l2ng-l2rtb-vlan-name']
                    newval['vlan-tag'] = vlan['l2ng-l2rtb-vlan-tag']
                except:
                    newval['vlan-name'] = vlan['vlan-name']
                    newval['vlan-tag'] = vlan['vlan-tag']
                
                vlans.append(newval)

    """Get vlan,interface,and mac data"""
    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        mactable =  []
        if type(host['mac-table']) == dict:
            mactable.append(host['mac-table'])
        else:
            mactable = host['mac-table']

        for entry in mactable:
            newlist = []
            newlist.append(host['hostname'])
            newlist.append(entry['l2ng-l2-mac-vlan-name'])
            """Find the right vlan id for the name"""
            for vlan in vlans:
                entryvlan = entry['l2ng-l2-mac-vlan-name']
                if vlan['vlan-name'] == entryvlan:
                    newlist.append(vlan['vlan-tag'])
                    break

            newlist.append(entry['l2ng-l2-mac-logical-interface'])
            newlist.append(entry['l2ng-l2-mac-address'])
            webdata['data'].append(newlist)

    with open(path+'/ethernet/ethernet-info.json','w') as f:
        json.dump(webdata,f)


if __name__ == "__main__":
    main()