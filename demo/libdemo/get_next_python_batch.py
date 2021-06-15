import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com"
course = "PYTHON"

resp = requests.get(website)
if resp.status_code != 200:
    print("Sorry! Could not retrieve content!")
    exit()

bs = BeautifulSoup(resp.text, 'html.parser')

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
count = 0
for row in rows[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    if title.strip().upper() == course:
        print(f"[{course}] starts on {cols[2].text} at {cols[1].text}")
        count += 1

if count == 0:
    print(f"Sorry! No [{course}] batch is in schedule!")
