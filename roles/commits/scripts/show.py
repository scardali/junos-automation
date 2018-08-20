#!/usr/local/bin/python
import sys
import json
import ast

def main():
    """Commit Information"""
    hosts = sys.argv[1]
    path = sys.argv[2]
    hosts = ast.literal_eval(hosts)
    hosts = [n.strip() for n in hosts]
    all_host_data = []
    for host in hosts:
        filename = 'build/'+host+'/commit-information.json'
        with open(filename,'r') as f:
            data = json.load(f)
            data['hostname'] = host
            all_host_data.append(data)

    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        commit_history = []
        if type(host['commit-history']) == dict:
            commit_history.append(host['commit-history'])
        elif type(host['commit-history']) == list:
            commit_history = host['commit-history']

        for commit in commit_history:
            newlist = []
            newlist.append(host['hostname'])
            newlist.append(commit['client'])
            newlist.append(commit['sequence-number'])
            newlist.append(commit['user'])
            newlist.append(commit['date-time'])
            webdata['data'].append(newlist)
            
    with open(path+'/commits/commit-table.json','w') as f:
            json.dump(webdata,f)
if __name__ == "__main__":
    main()