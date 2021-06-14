import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com"
# website = "https://www.w3schools.com"

resp = requests.get(website)
if resp.status_code != 200:
    print("Sorry! Could not retrieve content!")
    exit()

bs = BeautifulSoup(resp.text, 'html.parser')

links = bs.find_all("a")

for t in links:
    href = t['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = website + "/" + href
        else:
            href = website + href

    print(href)
