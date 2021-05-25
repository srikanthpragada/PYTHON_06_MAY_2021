#  table.py number [length]

import sys

if len(sys.argv) < 2:
    num = int(input("Enter number :"))
else:
    num = int(sys.argv[1])

if len(sys.argv) > 2:  # Length is given on command line
    length = int(sys.argv[2])
else:
    length = 10

for i in range(1, length + 1):
    print(f"{num:3} * {i:2} = {num * i:5}")
