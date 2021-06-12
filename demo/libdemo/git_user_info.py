import requests

user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print('Sorry! Could not get details of user!')
    exit(1)

details = resp.json()

for key, value in details.items():
    print(f"{key:20}  {value}")
