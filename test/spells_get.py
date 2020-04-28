import bs4
import requests
import json

print("Getting request")
r = requests.get('http://dnd5eapi.co/api/races/')
print("Request came back")
resp = r.json()
res = resp['results']

spells_list = []
for result in res:
    print(result['url'])
    spells_list.append({'name': result['name'], 'url': f"http://dnd5eapi.co{result['url']}"})

with open(r'F:\Innkeeper\resources\races.json', 'w+') as file:
    json.dump(spells_list, file)