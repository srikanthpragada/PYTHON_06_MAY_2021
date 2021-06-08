# Removing blank lines using temp file
import os

source = "names.txt"
target = "temp.txt"

with open(source, "rt") as sf, open(target, "wt") as tf:
    for line in sf:
        if len(line.strip()) > 0:
            tf.write(line)

# Delete source file
os.remove(source)
# Rename target as source
os.rename(target, source)
