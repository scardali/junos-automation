#!/usr/local/bin/python
import sys
import json
import ast

def main():
    """Interface Information"""
    hosts = sys.argv[1]
    path = sys.argv[2]
    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    all_host_data = []
    for host in hosts:
        filename = 'build/'+host+'/interface-information.json'
        with open(filename,'r') as f:
            data = json.load(f)
            data['hostname'] = host
            all_host_data.append(data)

    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        for interface in host['physical-interface']:
            newlist = []
            newlist.append(host['hostname'])
            newlist.append(interface['name'])
            """Get the interface description"""
            try:
                newlist.append(interface['description'])
            except:
                newlist.append('')
            newlist.append(interface['oper-status'])
            newlist.append(interface['admin-status'])
            try:
                newlist.append(interface['logical-interface']['address-family']['address-family-name'])
            except:
                newlist.append('')
            webdata['data'].append(newlist)

    with open(path+'/interface/interface-info.json','w') as f:
        json.dump(webdata,f)

if __name__ == "__main__":
    main()
