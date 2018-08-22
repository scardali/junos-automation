#!/usr/bin/env python
import json

def main():
    filename = 'tasks/ethernet/ethernet-info.json'
    with open(filename,'r') as f:
        data = json.load(f)
    print json.dumps(data,indent=2)

if __name__ == "__main__":
    main()