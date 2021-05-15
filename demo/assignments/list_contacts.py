data = ['Abc,29393933', 'Xyz,19199333', 'Pqr,39393311',
        'Def,39392222', 'Abc,994949444', 'Abc,29393933', 'Bbc']

contacts = {}
for entry in data:
    parts = entry.split(",")
    if len(parts) != 2:
        continue

    name, mobile = parts
    contacts[name] = mobile

for name, mobile in sorted(contacts.items()):
    print(f"{name:20} {mobile:10}")
