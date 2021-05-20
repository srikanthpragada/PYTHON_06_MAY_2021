data = ["45,56,abc,89", "89,66,88,75", "81,68,80,75"]

for m in data:
    marks = map(int, m.split(","))
    # print(marks)
    print(sum(marks))
