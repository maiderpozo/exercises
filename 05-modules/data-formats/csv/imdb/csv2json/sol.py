import json
import csv
import sys


#with open ("modules.csv", encoding="utf-8-")
#conv = list(csv.DictReader(sys.stdin))
#print(json.dumps(conv))

from urllib.request import urlopen

url = ""

with urlopen(url) as response:
    print(response)
    data = response.read().decode("utf-8")
    data = json.loads(data)
