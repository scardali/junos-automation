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
        filename = 'build/'+host+'/alarm_table.json'
        with open(filename,'r') as f:
            newval = {}
            newval['hostname'] = host
            newval['alarm-information'] = json.load(f)
            all_host_data.append(newval)

    """Alarm Data"""
    webdata = {}
    webdata['data'] = []
    for host in all_host_data:
        newlist = []
        newlist.append(host['hostname'])
        try:
            if host['alarm-information']['alarm-summary']['no-active-alarms'] == "":
                newlist.append("No Active Alarm for this Device")
                newlist.append("")
                newlist.append("")
                newlist.append("")
                webdata['data'].append(newlist)
                continue
        except:
            alarm_detail = host['alarm-information']['alarm-detail']
            alarm_list = []
            if type(alarm_detail) == dict:
                alarm_list.append(alarm_detail)
            for alarm in alarm_list:
                newlist.append(alarm['alarm-class'])
                newlist.append(alarm['alarm-description'])
                newlist.append(alarm['alarm-time'])
                newlist.append(alarm['alarm-type'])

        webdata['data'].append(newlist)


    with open(path+'/alarm/alarm-table.json','w') as f:
        json.dump(webdata,f)
if __name__ == "__main__":
    main()