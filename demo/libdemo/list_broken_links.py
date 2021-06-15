import requests
from bs4 import BeautifulSoup

# website = "http://www.srikanthtechnologies.com/"
website = "https://www.w3schools.com/"

resp = requests.get(website)
if resp.status_code != 200:
    print("Sorry! Could not retrieve content!")
    exit()

bs = BeautifulSoup(resp.text, 'html.parser')

links = bs.find_all("a")
count = 0
for t in links:
    href = t['href'].strip()
    if href == '#' or 'javascript:void' in href:
        continue

    href = href.strip()

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = website + href
        else:
            href = website + href[1:]

    # If it ends with / then remove it
    if href.endswith("/"):
        href = href[:-1]  # Remove right most char

    # Check whether link is valid
    print(href)
    try:
        resp = requests.get(href)
        if resp.status_code == 404:
            count += 1
            print(href + " - Invalid")
    except Exception as ex:
        print("Error :", ex)

print(f"Found {count} broken links")
