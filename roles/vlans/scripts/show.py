#!/usr/local/bin/python
import json
import sys
import ast

def main():
    """Get vlan information"""
    hosts = sys.argv[1]
    path = sys.argv[2]
    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    """Put data for all hosts in json"""
    all_host_data = []

    for host in hosts:
        filename = 'build/'+host+'/vlan-information.json'
        with open(filename,'r') as f:
            newval = {}
            newval['hostname'] = host
            newval['vlans'] = json.load(f)
            all_host_data.append(newval)
       
    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        vlans = []
        if type(host['vlans']) == dict:
            vlans.append(host['vlans'])
        elif type(host['vlans']) == list:
            vlans = host['vlans']
        for vlan in vlans:
            newlist = []
            newlist.append(host['hostname'])
            newlist.append(vlan['l2ng-l2rtb-vlan-name'])
            newlist.append(vlan['l2ng-l2rtb-name'])
            newlist.append(vlan['l2ng-l2rtb-vlan-tag'])
            try:
                if vlan['l2ng-l2rtb-vlan-member']['l2ng-l2rtb-vlan-member-interface'] == "":
                    newlist.append("No interfaces in this vlan")
                    webdata['data'].append(newlist)
                    continue
            except:
                interface_list = []
                if type(vlan['l2ng-l2rtb-vlan-member']) == dict:
                    interface_list.append(vlan['l2ng-l2rtb-vlan-member'])
                elif type(vlan['l2ng-l2rtb-vlan-member']) == list:
                    interface_list = vlan['l2ng-l2rtb-vlan-member']
                for interface in interface_list:
                    newlist.append(interface['l2ng-l2rtb-vlan-member-interface'])
                    webdata['data'].append(newlist)
                    newlist = newlist[:-1]
            
    with open(path+'/vlans/vlan-table.json','w') as f:
        json.dump(webdata,f)
    
    
    


if __name__ == "__main__":
    main()