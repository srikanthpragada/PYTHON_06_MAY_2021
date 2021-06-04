# Print contents of topics.txt

f = open("topics.txt", "rt")  # read text
lines = map(str.strip, f.readlines())  # strip all lines
for line in sorted(set(lines)):
    print(line)

f.close()
