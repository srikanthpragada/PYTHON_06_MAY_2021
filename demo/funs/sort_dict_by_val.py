def get_value(t):
    return t[1]


d = {1: 10, 3: 5, 2: 30, 4: 15}

for k, v in sorted(d.items(), key=get_value):
    print(k, v)
