# Prime number

num = int(input("Enter a number  :"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print("Not a prime number!")
        break
else:
    print("Prime Number")
