total = 0
i = 1
while i <= 5:
    try:
        num = int(input("Enter a number :"))
        total += num
        i += 1
    except ValueError:
        print("Invalid number!")

print("Total = ", total)
