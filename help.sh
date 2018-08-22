#!/bin/bash
for role in roles/*; do
    for main in $role/scripts/show.py; do
        sudo rmate $main
    done
done