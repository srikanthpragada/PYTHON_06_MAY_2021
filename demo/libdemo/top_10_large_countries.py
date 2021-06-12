import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit(1)

countries = resp.json()

for country in sorted(countries, key=lambda c: (c['area'] if c['area'] else 0), reverse=True)[:10]:
    print(f"{country['name']:50}  {country['area']:8.0f}")
