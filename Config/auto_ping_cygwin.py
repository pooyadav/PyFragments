import os
import subprocess
import commands
import numpy as np

# os.system("ping www.google.com | cut -d ' ' -f 7")
# os.system(" ping www.google.com | gawk -F' ' '{print $7}'")
server = "128.232.110.215"
N = 200
# command = "ping " + server + " 56 " + str(N) + " | gawk '{gsub(\"time=\",\"\",$0); split($0, a, \" \"); print $7}' "
command = "ping " + server + " 56 " + str(N)

os.system(command + " > test.txt") 
#code, result = commands.getstatusoutput(command)
#print result

ms = []

counter = 0
with open('test.txt') as fp:
	next(fp)
	for line in fp:
		if counter >= N: break;
		try:
			time = line.split(' ')[6][5:]
			print time
			time = int(time)
			ms.append(time)
			counter += 1;
		except :
			continue
print ms

mu = np.mean(ms)
std = np.std(ms)

print "mean: %.2f" % mu
print "std: %.2f" % std