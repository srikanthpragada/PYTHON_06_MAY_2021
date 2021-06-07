# Display deptname and avg. salary from dept_employees.txt

def isnumber(s):
    try:
        v = float(s)
        return True
    except:
        return False


depts = {}
f = open("dept_employees.txt", "rt")  # read text
for line in f:
    parts = line.strip().split(",")
    if len(parts) < 2:  # Blank line
        continue

    name = parts[0]
    salaries = [float(v) for v in parts[1:] if isnumber(v)]
    if name in depts:
        depts[name].extend(salaries)  # Add new salaries to existing list
    else:
        depts[name] = salaries  # Add new dept with salaries

f.close()
print(depts)

for name, salaries in sorted(depts.items()):
    total = sum(salaries)
    avg = total / len(salaries)
    print(f"{name:15} {len(salaries):3}  {total:10.2f} {avg:10.2f}")
