# Print contents of topics.txt

f = open("topics.txt", "rt")
for line in f.readlines():
    print(line.strip())

f.close()
