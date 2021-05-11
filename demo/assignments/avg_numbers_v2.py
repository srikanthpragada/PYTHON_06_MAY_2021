# Take numbers util 0 and display average of the numbers

total = count = 0
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    total += num
    count += 1

print(total / count)
