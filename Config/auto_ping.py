#!/usr/bin/python

import os
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

speed = []
N = 500

# server = "ping.online.net" # Could be a list
server = "207.154.194.38"
# command = "ping -q -c" + str(N) +  " " + server + " | sed -e '$!d' | cut -d ' ' -f4"
command1 = "ping -c" + str(N) + " " + server + ' | tee ping.log'
command2 = 'tail -n +2 ping.log > ping.tmp; head -n -4 ping.tmp > ping.log; rm ping.tmp'
command3 = 'cut -d \' \' -f7 ping.log | cut -c 6-'


def ping(output): 
    try:
        #_, result = commands.getstatusoutput(command)
        # print result
        os.system(command1); 
        os.system(command2); 
        _, result = commands.getstatusoutput(command3)
    except Exception as e:
        print e
    result = result.split('\n')
    result = map(float, result)

    with open(output, 'w') as f:
        for item in result:
            f.write("%s, " % item)

    #print "Bandwidth Measurements:" speed
    print "mu: %.3f" % np.mean(result)
    print "std: %.3f" % np.std(result)

    return result

def plot(fn1, fn2):
    # Input: two filenames 
    def getlist(filename) :
        df = pd.read_csv(filename, index_col=False, header=0)
        data = df.columns[:-1]
        speed = data.tolist()
        # print speed_cutspeed_cut = map(lambda x: x[:4], speed)
        speed_cut = map(lambda x: x[:4], speed)
        speed = list(map(float, speed_cut))
        
        return speed

    sp1 = getlist(fn1)
    sp2 = getlist(fn2)

    mean1 = np.mean(sp1)
    mean2 = np.mean(sp2)

    n, bins, patches = plt.hist(sp1, bins=10000, normed=1, histtype='step', linewidth=2, color='g',
                               cumulative=True, linestyle='--', label='Direct Connection')
    n, bins, patches = plt.hist(sp2, bins=10000, normed=1, histtype='step', linewidth=2, color='r',
                               cumulative=True, label='Connection via VPN')
    plt.axvline(x=mean1, color='g', linestyle=':')
    plt.axvline(x=mean2, color='r', linestyle=':')

    plt.xlim(20,45)
    plt.grid(False)
    ax = plt.axes()
    ax.set_aspect(.38 /ax.get_data_ratio())
    plt.xlabel("Ping (ms)")
    plt.ylabel("Percentile")
    plt.legend(loc='lower right',frameon=False)
    plt.show()

#ping('directping.csv')
# ping('vpnping.csv')
plot('directping.csv', 'vpnping.csv')