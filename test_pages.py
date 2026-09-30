import urllib.request
import json
import urllib.error

req = urllib.request.Request("https://medshineclinic.com/api/pages.php", headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
except urllib.error.HTTPError as e:
    print(e.code, e.read().decode())
