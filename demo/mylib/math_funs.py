PI = 3.14


def iseven(n):
    return n % 2 == 0


def ispalindrome(n):
    s = str(n)
    return s == s[::-1]


print(iseven(10))
print(ispalindrome(110))