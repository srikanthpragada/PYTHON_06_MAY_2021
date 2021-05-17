data = ['Jack,40,60', 'Roberts,87,83,77', 'Scott,76,56']

students = {}
for entry in data:
    parts = entry.split(",")
    name = parts[0]
    marks = [int(v) for v in parts[1:]]
    print(marks)
    avg_marks = sum(marks) / len(marks)
    students[name] = avg_marks

for name, avg in sorted(students.items()):
    print(f"{name:15} {avg:3.2f}")
