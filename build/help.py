import json
import sys
with open(sys.argv[1],'r+') as f:
    data = json.load(f)
    print json.dumps(data,indent=2)