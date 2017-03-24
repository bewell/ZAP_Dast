from zapv2 import ZAPv2

target = 'http://192.168.1.115/bWAPP/login.php'

logfile_zap = open('logfile_zap.log', 'w') # change this the where you want to log the zap output
logfile_alerts = open('logfile_alerts.log', 'w') #change this to where you want to log the alerts output
apikey = 'e0loiosplmf6sru4cmfmutj5i4' # Change to match the API key set in ZAP, or use None if the API key is disabled
# By default ZAP API client will connect to port 8080
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:9090', 'https': 'http://127.0.0.1:9090'})
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090. OR running on other machine than you're developing
# zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})