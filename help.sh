#!/bin/bash
for role in roles/*; do
    for main in $role/scripts; do
        sudo rm -ri $main
    done
done