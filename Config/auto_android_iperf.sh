#!/bin/bash

# Store the results from "Magic iPerf" to a file called "iperf" via Email
# In the form of 
# [  4]   4.03 5.01   sec  6.25 MBytes  53.8 Mbits/sec
cat iperf | tr -s " " | cut -d " " -f 7 | awk '{for(i=1;i<=NF;i++) {sum[i] += $i; sumsq[i] += ($i)^2}} END {for (i=1;i<=NF;i++) {printf "%f %f \n", sum[i]/NR, sqrt((sumsq[i]-sum[i]^2/NR)/NR)}}'
