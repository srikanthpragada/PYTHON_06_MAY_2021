import os

startdir = r"c:\classroom\may6"

allfiles = os.walk(startdir)
count = 0
for (dirname, dirs, files) in allfiles:
    for filename in files:
        if filename.endswith(".py"):
            count += 1
            print(dirname + "\\" + filename)

print(f"Count : {count}")