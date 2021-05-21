def zero(v):
    print(id(v))
    v = 0
    print(id(v))


def prepend(lst, num):
    lst.insert(0, num)


n = 100
print(id(n))
zero(n)
print(n)
nums = [1, 2, 3]
prepend(nums, 10)
print(nums)
