# Returns smallest and largest factors of the given number
def largest_smallest_factors(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return (i, num // i)

    return (None, None)


print(largest_smallest_factors(255))
print(largest_smallest_factors(257))
