PI = 3.14


def iseven(n):
    """
        Returns true if given number is palindrome
    """
    return n % 2 == 0


def ispalindrome(n):
    """
        Returns true if given number is palindrome
    """
    s = str(n)
    return s == s[::-1]  # Reverse the string and compare with original


if __name__ == '__main__':  # Invoked
    print(iseven(10))
    print(ispalindrome(110))
