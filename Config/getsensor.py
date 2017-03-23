#!/usr/bin/python

import csv
import socket
import requests
import sys
from contextlib import closing

# BASE_URL = 'http://' + socket.gethostbyname(socket.gethostname()) + ':8080/'

# How to get the mobilephone's addr?
BASE_URL = 'http://IP:8080/'

def query_sensor(url, sensor=''):
    r = requests.get(url + sensor, stream=True)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        with open("sensor", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1):
                if chunk: f.write(chunk)
            # for i in r: print "getting:", i
        return 1
    else:
        r.raise_for_status()

def main(argv):
    print argv
    results = query_sensor(BASE_URL, argv[1])
    
if __name__ == '__main__':
    main(sys.argv)
