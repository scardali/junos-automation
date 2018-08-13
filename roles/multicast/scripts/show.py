#!/usr/local/bin/python
import json
import sys
import ast
import itertools
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
            newval['snooping-information'] = json.load(f)
            all_host_data.append(newval)

    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        vlans = host['snooping-information']
        vlanlist = []
        if type(vlans) == dict:
            vlanlist.append(vlans)
        elif type(vlans) == list:
            vlanlist = vlans
        
        for vlan in vlanlist:
            newlist =  []
            newlist.append(host['hostname'])
            newlist.append(vlan['vlan'])
            igmp_info = vlan['igmp-snooping-group-information-per-learning-domain']
            if igmp_info == "":
                newlist.append("No Multicast interfaces on this vlan")
                for _ in itertools.repeat(None, 2):
                    newlist.append("")
                webdata['data'].append(newlist)

            else:
                groups = igmp_info['mgm-interface-groups']
                group_list = []
                if type(groups) == dict:
                    group_list.append(groups)
                else:
                    group_list = groups
                
                for interface in group_list:
                    newlist = []
                    newlist.append(host['hostname'])
                    newlist.append(vlan['vlan'])
                    newlist.append(interface['interface-name'])
                    try:
                        newlist.append(interface['mgm-group']['multicast-group-address'])
                        newlist.append(interface['mgm-group']['last-address'])
                    except:
                        for _ in itertools.repeat(None,2):
                            newlist.append("")
                    webdata['data'].append(newlist)
            
    with open(path+'/multicast/multicast-table.json','w') as f:
        json.dump(webdata,f)


if __name__ == "__main__":
    main()