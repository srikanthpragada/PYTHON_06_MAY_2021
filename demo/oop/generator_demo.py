def numbers():
    for n in range(2):
        yield n


nums = numbers()
print(type(nums))
print(next(nums))
print(next(nums))
print(next(nums))