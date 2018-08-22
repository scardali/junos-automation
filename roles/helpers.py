#!/usr/local/env python
import json
import itertools
import csv
def get_csv(role, path, webdata):
    csvdata = open(path+role+'/'+role+'.csv','w')
    csvwriter = csv.writer(csvdata)
    count = 0
    for datalist in webdata['data']:
        if count == 0:
            if role == 'version':
                header = ['Switch','Version']
            elif role == 'vlan':
                header = ['Switch','Vlan Name','VXLAN Name','Vlan Tag','Interface']
            elif role == 'commit':
                header = ['Switch','Client','Sequence Number','User','Date/Time']
            elif role == 'interface':
                header = ['Switch','Interface','Description','Operational Status','Admin Status','Address Family']
            elif role == 'alarm':
                header = ['Switch','Alarm Class','Alarm Description','Alarm Time','Alarm Type']
            elif role == 'ethernet':
                header = ['Switch','Vlan Name','Vlan ID','Interface','Mac']
            elif role == 'multicast':
                header = ['Switch','Vlan Name','Multicast Interface','Multicast Group Address','Multicast Listener Address']
            elif role == 'lacp':
                header = ['Switch','AE Interface','Receive Status','Interface Name','Transmit Status','Mux State']
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(datalist)
    csvdata.close()



def parse_data(hostname, role, data):
    newval = {}
    newval['hostname'] = hostname
    if role == 'version':
        newval['package-information'] = data
    elif role == 'vlan':
        newval['vlans'] = data
    elif role == 'commit':
        newval['commit-history'] = data
    elif role == 'interface':
        newval['physical-interface'] = data
    elif role == 'alarm':
        newval['alarm-information'] = data
    elif role == 'ethernet':
        newval['mac-table'] = data
    elif role == 'multicast':
        newval['snooping-information'] = data
    elif role == 'lacp':
        newval['interface-information'] = data
    elif data == None:
        pass
    return newval

def parse_web_data(role, host, webdata, vlans):
    if role == 'version':
        newlist = []
        newlist.append(host['hostname'])
        for item in host['package-information']:
            if item['name'] == 'junos' or item['name'] == 'os-kernel':
                comment = item['comment'].split('[')
                comment[1] = comment[1][:-1]
                newlist.append(comment[1])
                webdata['data'].append(newlist)

    elif role == 'vlan':
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
    elif role == 'commit':
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
    elif role == 'interface':
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
    elif role == 'alarm':
        newlist = []
        newlist.append(host['hostname'])
        try:
            if host['alarm-information']['alarm-summary']['no-active-alarms'] == "":
                newlist.append("No Active Alarm for this Device")
                newlist.append("")
                newlist.append("")
                newlist.append("")
                webdata['data'].append(newlist)
                return
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
    elif role == 'ethernet':

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
    elif role == 'multicast':
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
    elif role == 'lacp':
        hostname = host['hostname']
        ae = host['interface-information']['lag-lacp-header']['aggregate-name']
        try: 
            for lacp in host['interface-information']['lag-lacp-protocol']:
                newlist = []
                newlist.append(hostname)
                newlist.append(ae)
                newlist.append(lacp['lacp-receive-state'])
                newlist.append(lacp['name'])
                newlist.append(lacp['lacp-transmit-state'])
                newlist.append(lacp['lacp-mux-state'])
                webdata['data'].append(newlist)
        except:
            newlist = []
            newlist.append(hostname)
            newlist.append("LACP subsystem is not running - not needed by configuration")
            [newlist.append("") for _ in range(0,4)]
            webdata['data'].append(newlist)
    elif role == None:
        pass

        
def get_vlans(vlans, hosts):
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


