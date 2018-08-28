#!/usr/bin/env python
import subprocess
import sys,os
with open('run.txt','r') as f:
    lines = f.read().splitlines()
cmd = 'sudo docker run --rm -v $PWD:$PWD -w $PWD -it juniper/pyez-ansible ansible-playbook get_show_commands.yml --tags "'
for tag in lines[:-1]:
    cmd += tag+","
cmd += lines[-1]
cmd += '"'
os.system(cmd)

