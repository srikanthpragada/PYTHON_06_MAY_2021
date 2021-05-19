def iseven(n):
    return n % 2 == 0


def ispalindrome(n):
    return str(n) == str(n)[::-1]


def number_type(num, func):
    if func(num):
        print("Yes")
    else:
        print("No")


number_type(10, iseven)
number_type(101, ispalindrome)



def math_op(a, b, operation):
    return operation(a, b)


def multiply(a, b):
    return a * b


print(math_op(10, 20, multiply))
