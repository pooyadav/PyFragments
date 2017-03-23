#!/bin/bash
# Input parameter: process name, repeat time
cp /dev/null count.txt

for i in $(seq 1 $2) 
do 
    top -b -n 1 | grep $1 | tee >(wc -l >> count.txt) | awk '{print $6, $9}' | awk '{a += $1; b += $2} END {print a,b}' 
sleep 2 
done
