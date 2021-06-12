import requests


resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit(1)

countries = resp.json()

for c in countries:
    print(f"{c['name']:50}  - {c['capital']}")