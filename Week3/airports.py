import requests
import json

managers = {}
response = requests.get("https://api.aviationapi.com/v1/airports?apt=DCA,IAD,BWI")
file = response.json()

for apt in file:
    man = file[apt][0]['manager'] 
    managers[apt]=man

print(managers)