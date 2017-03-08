#!/bin/bash
# Backup.sh	shell script to backup log file
# version	5.1.2                    
# Auther	Roger Stark              
# date   	2013-01-09

# Copy all the files in /var/log to ./log
# Backup important log files in ./log to ./storage
mkdir log
mkdir storage
LOG='./log'
COPY='./storage'

#Use the namelist to select the important log file
printf "kern.log\nmail.err\nmail.log\ndmesg\ndmesg0\nsyslog.1\n" > RESERVE

checklist()
{
	cp -R /var/log/* $LOG

	find $LOG -size +50k | sed 's;^./log/;;'|						#Get the log file name
		while IFS='' read name 										#Read in the filename one-by-one
		do
			if grep ^$name$ < RESERVE > /dev/null					#Check it with the namelist
			then
				cp $LOG/$name $COPY/$name$(date +%Y%m%d%H%M%S)		#Timestamp
				cat /dev/null > $LOG/$name
			else
				cat /dev/null > $LOG/$name 							#Clear the original file in ./log
			fi
		done
}


while [ true ]; do
	checklist

	#Assuming that there is no sub-dir in the COPY dir
	if [ $(du -ks $COPY | cut -f 1) -gt 500k ]						#check the total size of the ./storage dir
	then
		rm $(ls -lt --time-style=long-iso $COPY | 					#Use --time-style=long-iso option to unify the result of 'ls'
			tail -1 | cut -d ' ' -f 9)								#Remove the last file
	fi

	sleep 10
done