d = {1: 10, 3: 5, 2: 30, 4: 15}

for k, v in sorted(d.items(), key=lambda t: t[1]):
    print(k, v)
