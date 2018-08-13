#!/bin/bash
for directory in roles/*; do
    for taskfolder in "$directory/scripts"; do
        for mainfile in "$taskfolder/show.py"; do
             sudo rmate "$mainfile"
        done
    done
done
    
