# Take numbers until 0 is given and display them in sorted order
nums = []

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    nums.append(num)

# nums.sort()

for n in sorted(nums):
    print(n)