import requests


inr = int(input("Enter amount : "))

resp = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/inr.json")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit(1)

details = resp.json()
rate = details["inr"]
print("USD = ", inr // rate)