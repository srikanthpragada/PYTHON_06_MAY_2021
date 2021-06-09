# usage : python list_python_files.py  [searchstring]  [startdir]

import os
import sys

if len(sys.argv) > 1:
    searchstring = sys.argv[1]
else:
    searchstring = None

if len(sys.argv) > 2:
    startdir = sys.argv[2]
else:
    startdir = os.getcwd()

allfiles = os.walk(startdir)
count = 0
for (dirname, dirs, files) in allfiles:
    for filename in files:
        if filename.endswith(".py"):
            if searchstring is None or searchstring in filename:
            #if (searchstring is None) or (searchstring is not None and searchstring in filename):
                count += 1
                print(dirname + "\\" + filename)

print(f"Count : {count}")
