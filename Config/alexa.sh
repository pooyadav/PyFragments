#!/bin/bash

FILE='top-1million-sites'
N=1000

wget https://statvoo.com/dl/$(FILE).csv.zip
unzip $(FILE).csv.zip
cut -d "," -f2 $(FILE).csv > ($FILE).txt
rm $(FILE).csv*

head -n $N $(FILE).txt 1<> top-$N-sites.txt
