#!/usr/local/bin/python
import sys
import json
import ast

def main():
    """Convert argument to list"""
    hosts = sys.argv[1]
    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    path = sys.argv[2]
    """Put data for all hosts in json"""
    all_host_data = []
    for host in hosts:
        filename = 'build/'+host+'/lacp_table.json'
        newval = {}
        try:
            with open(filename,'r') as f:
                newval['hostname'] = host
                newval['lag-lacp-protocol'] = json.load(f)
        except:
            newval['hostname'] = host
            newval['msg'] = "LACP subsystem is not running - not needed by configuration"

        all_host_data.append(newval)
    """LACP Data"""
    webdata = {}
    webdata['data'] = []
    
    for host in all_host_data:
        hostname = host['hostname']
        try: 
            for lacp in host['lag-lacp-protocol']:
                newlist = []
                newlist.append(hostname)
                newlist.append(lacp['lacp-receive-state'])
                newlist.append(lacp['name'])
                newlist.append(lacp['lacp-transmit-state'])
                newlist.append(lacp['lacp-mux-state'])
                webdata['data'].append(newlist)
        except:
            newlist = []
            newlist.append(hostname)
            newlist.append(host['msg'])
            [newlist.append("") for _ in range(0,3)]
            webdata['data'].append(newlist)

        
    with open(path+'/lacp/lacp-table.json','w') as f:
        json.dump(webdata,f)

if __name__ == "__main__":
    main()