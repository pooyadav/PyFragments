#!/usr/bin/python

# Suppose (browsertime)[https://github.com/sitespeedio/browsertime] is installed under home dir
# Installation: npm install --production in the source directory

from os import system 
import commands
import json

# param_prefix = "docker run --privileged --shm-size=1g --rm -v \"$(pwd)\":/browsertime-results sitespeedio/browsertime http://www."

# We only test the http connection here
param_prefix = "home/sam/browsertime/bin/browsertime.js http://www."
_, pwd = commands.getstatusoutput("pwd")
results = pwd + '/browsertime-results/www.'
alexa = open('top5.txt', 'r')
sites = []
for site in alexa.readlines():
    sites.append(site)
    command = param_prefix+site
    try:
        # This command should only run once
        # Consider seperate this part out.
        system(command + ' > /dev/null')
    except:
        continue

speedindexes = []

for site in sites:
    # Use the newst results, which does not have to be the case everytime
    # Tune the sort part
    command = "ls " + results + site.rstrip() + " | sort -r | head -n1"
    # os.system leads to getting result code rather than output on stdout
    _, subdir = commands.getstatusoutput(command)
    prefix = results + site.rstrip() + "/" + subdir 
    
    
    with open(prefix+"/browsertime.json", 'r') as result:
        data = json.load(result) # A big json file. More memory-friendly solution?
        speedindex_med = data["statistics"]["timings"]["rumSpeedIndex"]["median"] 
        speedindexes.append(speedindex_med)

with open(pwd+'/speedindex.txt', 'w') as f:
    for item in speedindexes:
        f.write("%s\t" % item)
