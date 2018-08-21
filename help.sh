#!/bin/bash
for role in roles/*; do
    for main in $role/tasks/main.yml; do
        sudo rmate $main
    done
done