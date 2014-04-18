__author__ = 'dsilalahi'

import urllib
from xml.etree.cElementTree import parse

candidates = ['1857', '4131', '4184']
my_latitude = 41.980262

def distance(lat1, lat2):
    'Return distance in miles between two lats'
    return 69*abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, my_latitude)
            print busid, dis, 'miles'
    print '-'*10

import time
while True:
    monitor()
    time.sleep(60)