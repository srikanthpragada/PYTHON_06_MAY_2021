import requests
from bs4 import BeautifulSoup

f = open("courses.xml", "rt")
bs = BeautifulSoup(f.read(), 'xml')
f.close()

for course in bs.find_all("course"):
    title = course.find("title").text
    fee = course.find("fee").text
    duration = course.find("duration").text
    print(f"{title:30} {duration:2} {fee:5}")
