# Display deptname and avg. salary from employees.txt

def isnumber(s):
    try:
        v = float(s)
        return True
    except:
        return False


f = open("employees.txt", "rt")  # read text
for line in f:
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    # salaries =  map(int, filter(str.isdigit, parts[1:]))
    salaries = [float(v) for v in parts[1:] if isnumber(v)]
    total = sum(salaries)
    avg = total / len(salaries)
    print(f"{name:15} {len(salaries):3}  {total:10.2f} {avg:10.2f}")

f.close()
