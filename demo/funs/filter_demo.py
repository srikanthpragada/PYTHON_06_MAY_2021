def iseven(n):
    return n % 2 == 0


def hasupper(st):
    for c in st:
        if c.isupper():
            return True

    return False


nums = [10, 20, 15, 43, 55, 66, 31]

for n in filter(iseven, nums):
    print(n)

names = ['Python', 'java', 'c', 'C#', 'JavaScript']

for n in filter(hasupper, names):
    print(n)
