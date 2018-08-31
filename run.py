#!/usr/bin/env python
import os
with open('run.txt','r') as f:
    lines = f.read().splitlines()
cmd = 'ansible-playbook get_show_commands.yml --tags "'
for tag in lines[:-1]:
    cmd += tag+","
cmd += lines[-1]
cmd += '"'
os.system(cmd)

