#!/usr/local/bin/python
import json
import sys
import ast
def main(): 
    """Convert argument to list"""
    hosts = sys.argv[1]
    path = sys.argv[2]
    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    """Put data for all hosts in json"""
    all_host_data = []
    for host in hosts:
        filename = 'build/'+host+'/igmp_snooping_membership.json'
        with open(filename,'r') as f:
            newval = {}
            newval['hostname'] = host
            newval['snooping-information-per-vlan'] = json.load(f)
            all_host_data.append(newval)
    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        vlans = host['snooping-information-per-vlan']
        vlanlist = []
        if type(vlans) == dict:
            vlanlist.append(vlans)
        elif type(vlans) == list:
            vlanlist = vlans
        
        for vlan in vlanlist:
            newlist =  []
            newlist.append(host['hostname'])
            newlist.append(vlan['vlan'])
            newlist.append("")
            try:
                newlist.append(vlan['igmp-snooping-group']['destination'])
            except:
                newlist.append("")
            try:
                newlist.append(vlan['igmp-snooping-group']['igmp-group-interface']['last-reporter'])
                newlist.append(vlan['igmp-snooping-group']['igmp-group-interface']['snooping-interface-name'])
            except:
                newlist.append("")
                newlist.append("")
            webdata['data'].append(newlist)

    with open(path+'/multicast/multicast-table.json','w') as f:
        json.dump(webdata,f)


if __name__ == "__main__":
    main()