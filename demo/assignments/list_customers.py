import re

f = open("customers.txt", "rt")
customers = {}

for line in f:
    # Name
    m = re.search("[A-Za-z ]+", line)
    if m is None:
        continue
    name = m.group(0).strip()

    # Number
    m = re.search(r"\d+", line)
    if m is None:
        continue
    mobile = m.group(0)

    customers[name] = mobile

f.close()

for name, mobile in sorted(customers.items()):
    print(f"{name:30} {mobile}")
