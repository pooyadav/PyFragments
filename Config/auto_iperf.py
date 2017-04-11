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

font=25 #'x-large'
params = {'legend.fontsize': font,
          'figure.figsize': (15, 6),
         'axes.labelsize': font,
         'axes.titlesize': font,
         'xtick.labelsize':font,
         'ytick.labelsize':font}
pylab.rcParams.update(params)

ERRORCODE=256
N = 5
speed = []
# server = "ping.online.net" # Could be a list
server = "207.154.194.38"
command = "/usr/bin/iperf3 --json -4 -t 100 -c " + server
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
        speed_cut = map(lambda x: x[:6], speed)
        # print speed_cut
        speed = list(map(float, speed_cut))
        return speed

    sp1 = getlist(fn1)
    sp2 = getlist(fn2)

    mean1 = np.mean(sp1)
    mean2 = np.mean(sp2)

    n, bins, patches = plt.hist(sp1, bins=50, normed=1, histtype='step', linewidth=2, color='g',
                               cumulative=True, linestyle='--', label='Direct Connection')
    n, bins, patches = plt.hist(sp2, bins=50, normed=1, histtype='step', linewidth=2, color='r',
                               cumulative=True, label='Connection via VPN')
    plt.axvline(x=mean1, color='g', linestyle=':')
    plt.axvline(x=mean2, color='r', linestyle=':')

    plt.xlim(0,80)
    plt.grid(False)
    ax = plt.axes()
    ax.set_aspect(.38 /ax.get_data_ratio())
    plt.xlabel("Bandwidth (Mbps)")
    plt.ylabel("Percentile")
    plt.legend(loc='upper left', frameon=False)
    plt.show()

# iperf('directiperf.csv')
# iperf('vpniperf.csv')
plot('directiperf.csv', 'vpniperf.csv')