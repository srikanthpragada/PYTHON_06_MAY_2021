# Removing blank lines using list

lines = []
with open("names.txt", "rt") as f:
    for line in f:
        if len(line.strip()) > 0:
            lines.append(line)

with open("names.txt", "wt") as f:
    for line in lines:
        f.write(line)
