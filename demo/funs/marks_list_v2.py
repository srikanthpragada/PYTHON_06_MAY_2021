data = ["45,56,abc,89", "89,66,,88,75", "81,-10,80,75"]

for m in data:
    marks = map(int, [v for v in m.split(",") if v.isdigit()])
    print(sum(marks))

for m in data:
    marks = map(int, filter(str.isdigit, m.split(",")))
    print(sum(marks))
