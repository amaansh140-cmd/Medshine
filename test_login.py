import urllib.request
import json
import urllib.error

data = json.dumps({"email": "admin@medshineclinic.com", "password": "admin123"}).encode('utf-8')
req = urllib.request.Request("https://medshineclinic.com/api/login.php", data=data, headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        print(response.getcode(), response.read().decode())
except urllib.error.HTTPError as e:
    print(e.code, e.read().decode())
