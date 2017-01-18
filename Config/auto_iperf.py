#!/usr/bin/python

from os import system
import commands
import json
import numpy as np
import time

ERRORCODE=256
N = 5
speed = []

# server = "ping.online.net" # Could be a list
server = "128.232.110.215"
command = "iperf3 --json -4 -t 10 -c " + server

while N > 0 :
    
    code, result = commands.getstatusoutput(command)
    # for interval in result["intervals"]:
    # print result["intervals"]
    if code == ERRORCODE:
        print "The server is busy running a test";
        time.sleep(1)
        continue

    json_acceptable_string = result.replace("'", "\"")
    data = json.loads(json_acceptable_string)

    for interval in data['intervals']:
        bps = interval['streams'][0]['bits_per_second']
        mbps = bps / 1e6
        speed.append(mbps)
        # print mbps, "Mbps"
    N = N - 1

mu = np.mean(speed)
sigma = np.std(speed)
print "Bandwidth Measurements:", speed
print "mu: %.2f" % mu 
print "std: %.2f" % sigma
