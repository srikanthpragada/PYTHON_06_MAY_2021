even_nums = []
odd_nums = []

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

for n in sorted(even_nums) + sorted(odd_nums):
    print(n)
