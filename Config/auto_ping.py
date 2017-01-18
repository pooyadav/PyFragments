#!/usr/bin/python

from os import system
import commands
import json
import numpy as np
import time

speed = []
N = 50

# server = "ping.online.net" # Could be a list
server = "128.232.110.215"
command = "ping -q -c" + str(N) +  " " + server + " | sed -e '$!d' | cut -d ' ' -f4"

_, result = commands.getstatusoutput(command)
result = result.split('/')
result = map(float, result)
mu = result[1]
sigma = result[3]

#print "Bandwidth Measurements:" speed
print "mu: %.3f" % mu 
print "std: %.3f" % sigma
