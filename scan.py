#!/usr/bin/env python

import time
from pprint import pprint
from zapv2 import ZAPv2
import params
import subprocess

############## This is the place for parameters #################
target = params.target
apikey = params.apikey
zap = params.zap
logfile_zap = params.logfile_zap
logfile_alerts = params.logfile_alerts
##################### / ###########################

print 'Launching the ZAP proxy. Wait a few seconds'
#this launching process is on Mac. If you're using on Windows, please modify the path to the ZAP executable
subprocess.Popen('/Applications/OWASP\ ZAP.app/Contents/MacOS/OWASP\ ZAP.sh %s' % (str('-daemon')), shell=True, stdout=logfile_zap) 
time.sleep(10)

# do stuff
print 'Accessing target %s' % target
# try have a unique enough session...
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)

print 'Spidering target %s' % target
scanid = zap.spider.scan(target, apikey=apikey)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    print 'Spider progress %: ' + zap.spider.status(scanid)
    time.sleep(2)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(5)

print 'Scanning target %s' % target
scanid = zap.ascan.scan(target, apikey=apikey)
while (int(zap.ascan.status(scanid)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(5)

print 'Scan completed'

# Report the results

print 'Host that was scanned: ' + ', '.join(zap.core.hosts)
print 'Alerts can be found in this file: ' + str(logfile_alerts)
pprint (zap.core.alerts(), logfile_alerts)

# Shuttting down ZAP scanner
print 'Shutting down ZAP Scanner, wait 10s'
zap.core.shutdown(apikey=apikey)
time.sleep(10)