#!/usr/bin/python
import datetime
import sys
def main():
    path = sys.argv[1]
    time  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('srv/nginx/time.txt','w') as f:
        f.write("Time last updated: "+time)

if __name__ == "__main__":
    main()