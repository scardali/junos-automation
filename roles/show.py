#!/usr/bin/env python
import sys
import json
import ast
import csv
from helpers import *

def main():
    """Convert argument to list"""
    hosts = sys.argv[1]
    path = sys.argv[2]
    role = sys.argv[3]

    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    """Put data for all hosts in json"""
    all_host_data = []
    for host in hosts:
        filename = 'build/'+host+'/'+role+'-information.json'
        try:
            with open(filename,'r') as f:
                data = json.load(f)
                all_host_data.append(parse_data(host, role, data))
        except:
            all_host_data.append(parse_data(host, role, None))
    """specific to ethernet"""
    vlans = []
    if role == 'ethernet':
        get_vlans(vlans, hosts)

    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        parse_web_data(role, host, webdata, vlans)

    with open(path+role+'/'+role+'-table.json','w') as f:
        f.write(json.dumps(webdata,indent=2))

    get_csv(role, path, webdata)

if __name__ == "__main__":
    main()