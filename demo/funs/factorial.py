def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def iseven(n):
    return n % 2 == 0


print(iseven(11))
print(factorial(5))
print(isprime(13), isprime(10000))
