import urllib, os, json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np

font=25 #'x-large'
params = {'legend.fontsize': font,
          'figure.figsize': (15, 6.2),
         'axes.labelsize': font,
         'axes.titlesize': font,
         'xtick.labelsize':font,
         'ytick.labelsize':font}
pylab.rcParams.update(params)

def download_alexa():

    testfile = urllib.URLopener()
    testfile.retrieve("http://s3.amazonaws.com/alexa-static/top-1m.csv.zip", "top-1m.csv.zip")
    os.system('unzip top-1m.csv.zip && cut -d "," -f2 top-1m.csv > top-1m.txt && rm top-1m.csv*')

def topN(n):
    command = 'head -n ' + str(n) + ' top-1m.txt 1<> top-' + str(n) + '-sites.txt'
    os.system(command)

def speedIndex(filename):
    param_prefix = 'docker run --privileged --shm-size=1g --rm -v \"$(pwd)\":/browsertime-results sitespeedio/browsertime -n 2 --skipHar http://www.'
    with open(filename, 'r') as f:
        for site in f.readlines():
            command = param_prefix + site + ' > /dev/null'
            try:
                os.system(command)
            except:
                continue

def getResults(filename='SI-result.txt'):
    rootDir = '.'
    speedindexes = []
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        # print('Found directory: %s' % dirName)
        for fname in fileList:
            if fname == 'browsertime.json':
                #print '\t%s' % dirName+fname
                file = dirName+ '/' + fname
                # print file
                with open(file, 'r') as result:
                    data = json.load(result)
                    speedindex_med = data["statistics"]["timings"]["rumSpeedIndex"]["median"] 
                    speedindexes.append(speedindex_med)

    with open(filename, 'w') as f:
        for item in speedindexes:
            f.write("%s, " % item)
    return speedindexes

def plotSI(f1, f2):
    def getdata(filename):
        df = pd.read_csv(filename, index_col=False, header=0)
        data = df.columns[:-1]
        speedindex = data.tolist()
        speedindex = list(map(float, speedindex))
        return speedindex

    speedindex = getdata(f1)
    speedindex2 = getdata(f2)
    mean = np.mean(speedindex)
    mean2 = np.mean(speedindex2)
   
    n, bins, patches = plt.hist(speedindex, bins=1000, normed=1, histtype='step', linewidth=2, color='g',
                               cumulative=True, linestyle='--', label='Direct Connection')
    n, bins, patches = plt.hist(speedindex2, bins=1000, normed=1, histtype='step', linewidth=2, color='r',
                               cumulative=True, label='Connection Via VPN')

    plt.axvline(x=mean, color='g', linestyle=':')
    plt.axvline(x=mean2, color='r', linestyle=':')

    plt.xlim([0, 10000])
    #plt.grid(True)
    plt.legend(loc='lower right', frameon=False)
    ax = plt.axes()
    ax.set_aspect(.38 /ax.get_data_ratio())
    # plt.title('Speed Index Distribution (VPN vs. Direct) -- Top 500 sites')
    plt.xlabel('Speed Index')
    plt.ylabel('Percentile')
    plt.show()

# topN(500)
# speedIndex('../top-500-sites.txt')
# getResults('SI-result.txt')
# getResults('direct-si.csv')
## cd ..
plotSI('./vpnSI/SI-result.txt', './directSI/SI-result.txt')

# in ./browsertime-results, run `python ../testspeedi)ndex.py`
