#!/usr/bin/python

from os import system
import commands
import json
import numpy as np
import time
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

ERRORCODE=256
N = 5
speed = []
# server = "ping.online.net" # Could be a list
server = "207.154.194.38"
command = "/usr/bin/iperf3 --json -4 -t 10 -c " + server
cmd = command.split(" ")

def iperf(output):
    
    for _ in range(N):
        #code, result = commands.getstatusoutput(command)
        try:
            result = subprocess.check_output(cmd)
            print result
        except Exception as e:
            print e
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

    # Output list to file for later loading
    with open(output, 'w') as f:
        for item in speed:
            f.write("%s, " % item)

    mu = np.mean(speed)
    sigma = np.std(speed)
    print "Bandwidth Measurements:", speed
    print "mu: %.2f" % mu 
    print "std: %.2f" % sigma
    
    return speed


def plot(fn1, fn2):
    # Input: two filenames 
    def getlist(filename) :
        df = pd.read_csv(filename, index_col=False, header=0)
        data = df.columns[:-1]
        speed = data.tolist()
        speed = list(map(float, speed))
        return speed

    sp1 = getlist(fn1)
    sp2 = getlist(fn2)

    n, bins, patches = plt.hist(sp1, bins=30, normed=1, histtype='step', linewidth=2, color='g',
                               cumulative=True, linestyle='--', label='Direct Connection')
    n, bins, patches = plt.hist(sp2, bins=30, normed=1, histtype='step', linewidth=2, color='r',
                               cumulative=True, label='Connection Via VPN')
    plt.legend(loc='lower right')
    plt.show()

#iperf('directiperf.csv')
# iperf('vpniperf.csv')
plot('directiperf.csv', 'vpniperf.csv')