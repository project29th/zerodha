import requests
import json

url = 'http://127.0.0.1:5000/webhook'

data = {
    "stocks": "SEPOWER,ASTEC,EDUCOMP,KSERASERA,IOLCP,GUJAPOLLO,EMCO",
    "trigger_prices": "3.75,541.8,2.1,0.2,329.6,166.8,1.25",
    "triggered_at": "2:34 pm",
    "scan_name": "Short term breakouts",
    "scan_url": "short-term-breakouts",
    "alert_name": "Alert for Short term breakouts",
    "webhook_url": "http://your-web-hook-url.com"
}

r = requests.post(url, data=json.dumps(data))
