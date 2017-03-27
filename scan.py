#!/usr/bin/env python
import sys
sys.path.append("zapv2")

import json
import time
from pprint import pprint
from zapv2 import ZAPv2
import subprocess

############## parameters #################
startZapPath = '/Users/g01059639/software/ZAP_2.5.0/zap.sh -daemon -port 9090 -config api.disablekey=true'
target = sys.argv[1]
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:9090', 'https': 'http://127.0.0.1:9090'})
logfile_zap = open('logfile_zap.log', 'w')
logfile_alerts = open('logfile_alerts.log', 'w')
##################### / ###########################

print 'Launching the ZAP. Wait a few seconds'
subprocess.Popen( startZapPath, shell=True, stdout=logfile_zap)
time.sleep(10)

print 'Accessing target %s' % target
zap.urlopen(target)
time.sleep(3)

print 'Spidering target %s' % target
scanid = zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(3)
try:
    while (int(zap.spider.status(scanid)) < 100):
        print 'Spider progress %: ' + zap.spider.status(scanid)
        time.sleep(0.5)
except:
    print "Oops"
    zap.core.shutdown()
    sys.exit(0)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(3)



print 'Scanning target %s' % target
scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(0.5)

print 'Scan completed'



# Report the results

print 'Host that was scanned: ' + ', '.join(zap.core.hosts)
print 'Alerts can be found in this file: ' + str(logfile_alerts)


jsonOutput = zap.core.alerts()
jsonOutputString = json.dumps(jsonOutput)

try:
    #print jsonOutput[0]["name"]
    for i in jsonOutput:
        print i["risk"] + " -- " + i["url"] + " -- " + i["name"]

    pprint (jsonOutputString, logfile_alerts)
except:
    print "Oops!"



print 'Shutting down ZAP Scanner, wait 4s'
zap.core.shutdown()
time.sleep(4)
