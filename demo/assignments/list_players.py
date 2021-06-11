from datetime import datetime

f = open("players.txt", "rt")
players = []
today = datetime.today()
for line in f:
    if ',' not in line:
        continue

    name, dobstr = line.split(",")
    dob = datetime.strptime(dobstr.strip(), "%d-%m-%Y")
    years = (today - dob).days // 365
    players.append((name, years))

f.close()

for name, years in sorted(players, key=lambda t: t[1]):
    print(f"{name:30} {years:2}")
