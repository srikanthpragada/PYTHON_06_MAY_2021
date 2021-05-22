def isvalidnumber(s):
    if len(s) == 0:
        return False

    if s[0] in ['-', '+'] and s[1:].isdigit():
        return True
    else:
        return s.isdigit()


data = ["45,56,abc,89", "89,66,,88,75", "80,-10,80,70"]

for m in data:
    marks = map(int, filter(isvalidnumber, m.split(",")))
    print(sum(marks))
