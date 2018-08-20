#!/usr/bin/python
import datetime
import sys
def main():
    task = sys.argv[1]
    path = sys.argv[2]
    time  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(path+task+'time.txt','w') as f:
        f.write("Time last updated: "+time)

if __name__ == "__main__":
    main()