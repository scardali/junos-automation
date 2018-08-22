#!/bin/bash
for task in *; do
    for file in $task/*.html; do
        sudo git rm $file
    done
done