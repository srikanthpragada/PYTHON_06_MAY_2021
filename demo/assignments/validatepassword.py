# Validate passwords
# validatepassword.py  password ...

import sys


def isvalidpassword(s):
    if len(s) < 6:
        return False

    upper = digit = special = False
    for c in s:
        if c.isupper():
            upper = True
        elif c.isdigit():
            digit = True
        elif not (c.islower() or c.isspace()):
            special = True

    return upper and digit and special


for s in sys.argv[1:]:
    print(f"{s:10}  {isvalidpassword(s)}")
