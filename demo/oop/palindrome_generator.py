def palindrome(start, end):
    for n in range(start, end + 1):
        s = str(n)
        if s == s[::-1]:
            yield n


def palindrome_list(start, end):
    nums = []
    for n in range(start, end + 1):
        s = str(n)
        if s == s[::-1]:
            nums.append(n)

    return nums


nums = palindrome(10, 50)
print(next(nums))

for n in palindrome(100, 150):
    print(n)

palins = palindrome_list(10, 100)
print(palins)
print(palins[:5])
