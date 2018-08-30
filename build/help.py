#!/usr/bin/env python
import sys
import json
with open(sys.argv[1]) as f:
	print json.dumps(json.load(f),indent=2)
