import sys

print(sys.path)  # module search path
sys.path.insert(0, r'c:\classroom\may6\demo\stlib')

import math_funs as mf
from math_funs import ispalindrome

print(ispalindrome(101))
print(mf.iseven(101))
