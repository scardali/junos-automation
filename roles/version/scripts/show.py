#!/usr/local/bin/python
import sys
import json
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
        filename = 'build/'+host+'/version_table.json'
        with open(filename,'r') as f:
            newval = {}
            newval['hostname'] = host
            newval['package-information'] = json.load(f)
            all_host_data.append(newval)

    """Version Data"""
    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        newlist = []
        newlist.append(host['hostname'])
        for item in host['package-information']:
            if item['name'] == 'junos':
                comment = item['comment'].split('[')
                comment[1] = comment[1][:-1]
                newlist.append(comment[1])
        webdata['data'].append(newlist)


    with open(path+'/version/version-table.json','w') as f:
        json.dump(webdata,f)
if __name__ == "__main__":
    main()